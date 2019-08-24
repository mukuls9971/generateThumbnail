from django.urls import reverse
from django.test import TestCase


class GenThumbnail(TestCase):
    def serverUp(self):
        response = self.client.get(reverse('pages:generateThumbnailView'))
        self.assertEqual(response.status_code, 200)
        