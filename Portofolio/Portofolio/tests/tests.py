from django.test import TestCase

class GalleryTestCase(TestCase):

    def test_gallery(self):
        gallery = "Gallery"
        self.assertEqual(gallery, "Galery")
