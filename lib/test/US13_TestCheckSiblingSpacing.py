import unittest

from lib.test.trees import kristen_tree
from lib.test.trees import michael_tree
from lib.test.trees import sprint_one_tree
from lib.test.trees import sprint_two_tree
from lib.test.trees import us13_mult_sets_close_sibs
from lib.test.trees import us13_mult_sets_close_sibs2


class TestCheckSiblingSpacing(unittest.TestCase):
    def test_michael_tree(self):
        self.assertTrue(michael_tree.check_sibling_spacing())

    def test_kristen_tree(self):
        self.assertTrue(kristen_tree.check_sibling_spacing())

    def test_sprint_one_tree(self):
        self.assertTrue(sprint_one_tree.check_sibling_spacing())

    def test_sprint_two_tree(self):
        self.assertFalse(sprint_two_tree.check_sibling_spacing())

    def test_mult_sets_close_sibs(self):
        self.assertFalse(us13_mult_sets_close_sibs.check_sibling_spacing())

    def test_mult_sets_close_sibs2(self):
        self.assertFalse(us13_mult_sets_close_sibs2.check_sibling_spacing())
