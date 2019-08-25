from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import requests
from io import BytesIO
import logging
logger = logging.getLogger(__name__)
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)

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
        

