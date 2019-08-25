import redis
from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import requests
from io import BytesIO
import random
import logging
import threading
import time
import datetime 
logger = logging.getLogger(__name__)
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)

queue = redis.Redis(host='127.0.0.1', port=6379)
queueKey = "thumbnail"


class ProcessThumbnail(object):
    def __init__(self, interval=3):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            # More statements comes here
            item = queue.lpop(queueKey)
            logger.info("checking the queue")
            if item: 
                try:
                    item = item.decode('utf-8')
                    logger.info("Async processing is being done for {}".format(item))
                    item = item.split('|')
                    resp = requests.get(item[0])
                    im = Image.open(BytesIO(resp.content))
                    im = im.convert('RGB')
                    im.thumbnail((100, 100))
                    fileLoc = "./genThumbnail/pages/static/"+item[1]
                    im.save(fileLoc, "JPEG")
                    logger.info('file being saved at' +fileLoc)
                except Exception as e:
                    print("cannot create thumbnail",str(e))


            time.sleep(self.interval)


ProcessThumbnail()

def homePageView(request):
    logger.info('Processing is being done for heartbeat message')
    return HttpResponse('Hello, World!')


def generateThumbnailView(request):
    try:
        url = request.GET['url']
        logger.info('Processing is being done for image: %s', url)
        resp = requests.get(url)
        im = Image.open(BytesIO(resp.content))
        im = im.convert('RGB')
        im.thumbnail((100, 100))
        response = HttpResponse(content_type="image/jpeg")
        im.save(response, "JPEG")
        return response
    except:
        logger.error('Something went wrong!')
        red = Image.new(mode="RGB", size=(100, 100))
        response = HttpResponse(content_type="image/jpeg")
        red.save(response, "JPEG")
        return response
        
def generateThumbnailAsync(request):
    try:
        url = request.GET['url']
        filename = str(random.randint(1, 100000))+".jpeg"
        queue.rpush(queueKey, url +"|"+filename)
        msg = 'Please check filename:127.0.0.1/media/' + filename + ' after 10 min or use our sync algorithm ' 
        logger.info(msg)
        return HttpResponse(msg)
    except Exception as e:
        logger.error('Something went wrong!', str(e))
        return HttpResponse('Some error occured')



