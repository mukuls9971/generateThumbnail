from django.urls import path

from .views import homePageView, generateThumbnailView

urlpatterns = [
    path('', homePageView, name='home'),
    path('generateThumbnail', generateThumbnailView, name='generateThumbnail')
    
]
