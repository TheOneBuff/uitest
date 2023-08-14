import unittest
from page.add_point import add_point
from utils.take_screenshot import take_screenshot

class TestAddPoint(unittest.TestCase):
    def setUp(self):
        self.page = add_point()

    def tearDown(self) -> None:
        self.page.close()
    def test_add_point_success(self):
        self.page.add()

        #self.assertIn('sucess', self.page.driver.title)
