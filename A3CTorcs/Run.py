import threading
import multiprocessing
import os.path
from time import sleep
import tensorflow as tf

from A3CNetwork import A3CNetwork
from Worker import Worker
from vizdoom import *
from gym_torcs import TorcsEnv

print('# Initialising variables ...')

load_model = False
model_path = './model'

# TensorFlow supports both CPU and GPU, as identified below.
# https://www.tensorflow.org/programmers_guide/using_gpu#supported_devices
cpu_identifier = "/cpu:0"  # The CPU of the machine.
gpu_0_identifier = "/device:GPU:0"  # The GPU of the machine machine (if available).
gpu_1_identifier = "/device:GPU:1"  # The second GPU of the machine machine (if available).

#cpu_count = multiprocessing.cpu_count()  # Available CPU threads.
cpu_count=1
print(str(cpu_count))

learning_rate = 1e-4
gamma = 0.99  # Discount rate for advantage estimation and reward discounting.

input_size = 4096  # Number of inputs. # TODO
action_size = 1  # Number of actions that can be taken. # TODO

# Worker agents represented by their own neural network, with their own network parameters and acting within their own
# environment at the same time the other agents are acting in theirs
workers = []

# https://www.tensorflow.org/api_docs/python/tf/train/Saver
checkpoints_to_keep = 5  # Maximum number of recent checkpoint files to keep.

# TODO
max_episode_length = 50

print('# Variable initialisation complete ...')

print('# CPU Count: ' + str(cpu_count))

tf.reset_default_graph()

if not os.path.exists(model_path):
    os.makedirs(model_path)

with tf.device(cpu_identifier):
    print('# \'with tf.device\'')

    global_episodes = tf.Variable(0, dtype=tf.int32, name='global_episodes', trainable=False)
    optimizer = tf.train.AdamOptimizer(learning_rate)
    master_network = A3CNetwork(input_size, action_size, 'global', None)  # Create global network.

    # Create worker for each CPU thread.
    for cpu in range(cpu_count):
        workers.append(Worker(TorcsEnv(vision=True), cpu, input_size, action_size, optimizer, model_path, global_episodes))
    saver = tf.train.Saver(max_to_keep=checkpoints_to_keep)

with tf.Session() as sess:
    print('# \'with tf.session()\'')
    coord = tf.train.Coordinator()
    if load_model:

        print('Loading Model...')
        ckpt = tf.train.get_checkpoint_state(model_path)
        saver.restore(sess, ckpt.model_checkpoint_path)
    else:
        sess.run(tf.global_variables_initializer())

    # This is where the asynchronous magic happens.
    # Start the "work" process for each worker in a separate threat.
    worker_threads = []
    for worker in workers:
        worker_work = lambda: worker.work(max_episode_length, gamma, sess, coord, saver)
        t = threading.Thread(target=worker_work)
        t.start()
        sleep(0.5)
        worker_threads.append(t)
    coord.join(worker_threads)