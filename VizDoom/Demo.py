from Helper import *
from vizdoom import *
import tensorflow as tf

from A3CNetwork import *

# Create Instance of Doomdoom
doom = DoomGame()

# set doom properties
doom.set_doom_scenario_path("basic.wad")  # This corresponds to the simple task we will pose our agent
doom.set_doom_map("map01")
doom.set_screen_resolution(ScreenResolution.RES_160X120)
doom.set_screen_format(ScreenFormat.GRAY8)
doom.set_render_hud(False)
doom.set_render_crosshair(False)
doom.set_render_weapon(True)
doom.set_render_decals(False)
doom.set_render_particles(False)
doom.add_available_button(Button.MOVE_LEFT)
doom.add_available_button(Button.MOVE_RIGHT)
doom.add_available_button(Button.ATTACK)
doom.add_available_game_variable(GameVariable.AMMO2)
doom.add_available_game_variable(GameVariable.POSITION_X)
doom.add_available_game_variable(GameVariable.POSITION_Y)
doom.set_episode_timeout(100000)
doom.set_episode_start_time(0)
doom.set_window_visible(True)  # Set visible to True
doom.set_sound_enabled(False)
doom.set_living_reward(-1)
doom.set_mode(Mode.PLAYER)
doom.init()

checkpoints_to_keep = 5
ckpt = tf.train.get_checkpoint_state('./model')

input_size = 7056
action_size = 3

a3c = A3CNetwork(input_size, action_size, 'global', None)
saver = tf.train.Saver(max_to_keep=checkpoints_to_keep)
actions = np.identity(action_size, dtype=bool).tolist()
with tf.Session() as sess:
    saver.restore(sess, ckpt.model_checkpoint_path)

    rnn_state = a3c.state_init

    doom.new_episode()
    s = doom.get_state().screen_buffer
    s = process_frame(s)
    while doom.is_episode_finished() == False:
        # Take an action using probabilities from policy network output.
        a_dist, v, rnn_state = sess.run(
            [a3c.policy, a3c.value, a3c.state_out],
            feed_dict={a3c.inputs: [s],
                       a3c.state_in[0]: rnn_state[0],
                       a3c.state_in[1]: rnn_state[1]})
        a = np.random.choice(a_dist[0], p=a_dist[0])
        a = np.argmax(a_dist == a)

        r = doom.make_action(actions[a]) / 100.0

# with tf.Session() as sess:
#     print('# \'with tf.session()\'')
#     coord = tf.train.Coordinator()
#     if load_model:
#
#         print('Loading Model...')
#         ckpt = tf.train.get_checkpoint_state(model_path)
#         saver.restore(sess, ckpt.model_checkpoint_path)
#     else:
#         sess.run(tf.global_variables_initializer())
