import os
from django.test import TestCase


class GalleryTestCase(TestCase):


    def test_number_of_files(self):
        total = 0
        for file in os.listdir("./media/gallery"):
            total+=1
        self.assertEqual(total, 18)