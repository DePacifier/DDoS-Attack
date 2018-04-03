from threading import Thread
import urllib.request


class ThreadClass(Thread):

    def __init__(self, threadIdentifier):
        Thread.__init__(self)
        self.threadIdentifier = threadIdentifier

    def run(self):
        while True:
            print("Sending Get Request from Thread : ", self.threadIdentifier)
            recieved_file = urllib.request.urlopen("http://192.168.43.1:33455")
            print("Request from %s was successful " % recieved_file.geturl())
            ##local_filename, headers = urllib.request.urlretrieve("http://192.168.43.1:33455")
            ##print("Request Successfully stored :", local_filename)
