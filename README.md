# generateThumbnail
JSON-based REST API service which resizes images into 100x100px thumbnails.

# Architecture
You will create a JSON-based REST API service which resizes images into 100x100px thumbnails.
Since image processing operations could be time-consuming, this service should have along-running job
architecture. Possible architectures would include queue-based workers or webhooks, but you are free to
design it as you see fit.
You do NOT need to make any frontend UI for this service.
You do NOT need to deploy or host this service anywhere - it just needs to be runnable and testable on any
normal computer - but we do encourage you to think about how you might host your service and discuss it in
your README.
# Tests
You should provide basic tests for your service, and they should be easily runnable.
You are NOT required to implement all corner cases, but we do encourage you to think about them and
discuss them in your README.



# Documentation 

-Python based Architeture

-How To Run
docker-compose up

-How to test
./manage.py test
since it is a Rest API without any business logic, only one unit test is there
Go to this url: http://127.0.0.1:8000/generateThumbnail?url=https://images.pexels.com/photos/2331584/pexels-photo-2331584.jpeg 
expected: should show thumbnail
If image not available should show a black thumbnail of same size i.e. 100*100

-API
This operation generates a thumbnail image
Http Method: GET
Request URL: http://127.0.0.1:8000/generateThumbnail?url=https://images.pexels.com/photos/2331584/pexels-photo-2331584.jpeg
Input Requirements: 1.Supported image formats: JPEG, PNG, GIF, BMP. 2. size > 100*100
Response 200 + [Binary image data]

-Architecture
1. components and the connections
    Only a single view which downloads the remoteUrl and converts to thumbnail
2. libraries/dependencies/tools
    django: more stable and scalable with multiple workers and lot of ready-to-use features like template, admin etc
    PIL: standard library in python for image manipulation
    requests: standard library to download data from url

    Most packages and libraries we dont require for current implementation but if we want to scale then we would require that 

- improvements for production
- scaling
- monitoring