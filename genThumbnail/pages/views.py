from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import requests
from io import BytesIO

def homePageView(request):
    return HttpResponse('Hello, World!')


def generateThumbnailView(request):
    try:
        url = request.GET['url']
        resp = requests.get(url)
        im = Image.open(BytesIO(resp.content))
        im = im.convert('RGB')
        im.thumbnail((100, 100))
        response = HttpResponse(content_type="image/jpeg")
        im.save(response, "JPEG")
        return response
    except:
        red = Image.new(mode="RGB", size=(100, 100))
        response = HttpResponse(content_type="image/jpeg")
        red.save(response, "JPEG")
        return response
        return HttpResponse('Thumbnail is generated')


