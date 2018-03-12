import paramiko
import cv2
import time

# Set username, password, and IP address of host computer
# ip = raw_input("Host IP: ")
# usr = raw_input("Host Username: ")
# pw = raw_input("Host Password: ")

pw = "C0rs9ir-PC"
usr = "tensorgroup"
ip = "10.42.0.1"

# Set width and height for image resolution (IE 640 x 480)
width = 640
height = 480

# Change fps (frames per second) depending on neural network performance. See while loop.
fps = 10
t = 0

# Set x and y for crop
x = 200
y = 200


# Setting up SSH protocol
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(ip, 22, username = usr, password = pw, timeout = 4)

# Opens SFTP Protocol to actually send the image
# sftp = ssh.open_sftp()

# Begin video capture and set resolution to width x height
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)


if (not cap.isOpened()):
    print "Unable to read camera feed"

"""
While the video capture is active, take an image from the camera, and send it over to the host computer.
Note: Will need to change source and destination depending on computers being used.
time.sleep is used to send images every n seconds.
Put code in the for loop to send images every x frames per second
"""

print y + height
print x + width


while cap.isOpened():
    # time.sleep(1)
    # for i in range(fps):

    ret, frame = cap.read()

    file_name = "images/output" + str(t) + ".png"
    file_name.replace(" ", "")
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # image = cv2.resize(image, (height, width))
    image = image[y:y + height, x:x + width]
    cv2.imwrite(file_name, image)

    # source = '/Users/osama/OneDrive - University of Essex/Masters/CE903/code/images/output' + str(t) + '.png'
    # destination = '/home/tensorgroup/Desktop/images/output' + str(t) + '.png'
    # sftp.put(source, destination)

    print "Image ", t, "sent."
    t += 1


# When everything done, release the video capture and close all frames
cap.release()
cv2.destroyAllWindows()
