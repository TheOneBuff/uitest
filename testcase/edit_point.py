import unittest
from page.edit_point import edit_point


class TestEditPoint(unittest.TestCase):

    def setUp(self):
        self.page = edit_point()

    def tearDown(self) -> None:
        self.page.close()

    # 新增子主题
    def test_add_first_node(self):
        self.page.add_sub_theme()