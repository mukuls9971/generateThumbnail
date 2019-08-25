
import threading
from PIL import Image
import time 
import datetime

def createThumbnail(filename): 
    outfile = filename + ".thumbnail.JPEG"
    try:
        im = Image.open(filename)
        im = im.convert('RGB')
        im.thumbnail((100,100))
        im.save(outfile, "JPEG")
    except IOError:
        print("cannot create thumbnail for",filename)


class ProcessThumbnail(object):
    def __init__(self, interval=1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            # More statements comes here
            print(datetime.datetime.now().__str__() +
                  ' : Start task in the background')

            time.sleep(self.interval)



if __name__ == "__main__":
    tr = ProcessThumbnail()
    time.sleep(1)
    print(datetime.datetime.now().__str__() + ' : First output')
    time.sleep(5)
    print(datetime.datetime.now().__str__() + ' : Second output')
