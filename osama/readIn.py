# This will read in images as they are sent to the folder.

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import cv2
import numpy as np

i = 0


class Watcher:
    directory = "images"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.directory, recursive = True)
        self.observer.start()

        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print "Error"

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        global i
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            print "Image ", i, " taken!"
            image = cv2.imread('output' + str(i) + '.png')
            i += 1

if __name__ == '__main__':
    w = Watcher()
    w.run()
