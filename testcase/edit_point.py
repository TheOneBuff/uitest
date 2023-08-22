import unittest
from page.edit_point import edit_point


class TestEditPoint(unittest.TestCase):
    def setUp(self):
        self.page = edit_point()

    def tearDown(self) -> None:
        self.page.close()
    def test_edit_point_success(self):
        self.page.edit()