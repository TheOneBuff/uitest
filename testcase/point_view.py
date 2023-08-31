import unittest
from page.point_view import point_view


class TestPointView(unittest.TestCase):
    def setUp(self):
        self.page = point_view()

    def tearDown(self) -> None:
        self.page.close()

    def test_point_view(self):
        assertresult = self.page.point_view()
        self.assertEquals('中国宏观(冰洁专用)', assertresult)