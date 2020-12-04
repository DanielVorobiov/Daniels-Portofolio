import os
from django.test import TestCase


class GalleryTestCase(TestCase):

    def test_gallery(self):
        gallery = "Gallery"
        self.assertEqual(gallery, "Gallery")

    def test_file(self):
        for filename in os.listdir("./media/gallery"):
            self.assertEqual(filename.endswith(".jpg"), True)

    def test_number_of_files(self):
        total = 0
        for file in os.listdir("./media/gallery"):
            total+=1
        self.assertEqual(total, 18)

    def test_registration(self):
        files= os.listdir("./registration")
        self.assertEqual("apps.py" in files, True)










