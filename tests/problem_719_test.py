
"""
Purpose: Testing problem 719
Date created: 2020-06-07

Contributor(s):
    Mark M.
"""



import unittest
from math import sqrt

from incomplete.problem_719 import (
        Element, split_eval, fsplitter, sq_eval
        )


class ProjEuler719Case(unittest.TestCase):

    def test_element_class_instance(self):
        """Test Element instantiation."""
        el_inst = Element(81, 9.0)
        self.assertTrue(isinstance(el_inst, Element))


    def test_element_class_repr(self):
        """Test Element instantiation."""
        el_inst = Element(81, 9.0)
        self.assertEqual(el_inst.__repr__(), "<Element (81) />")


    def test_element_class_n_value(self):
        """Test Element instantiation and n value."""
        el_inst = Element(81, 9.0)
        self.assertEqual(el_inst.n, 81)


    def test_element_class_nstr_value(self):
        """Test Element instantiation and nstr value."""
        el_inst = Element(81, 9.0)
        self.assertEqual(el_inst.nstr, '81')


    def test_element_class_root_value(self):
        """Test Element instantiation and root value."""
        el_inst = Element(81, 9.0)
        self.assertEqual(el_inst.root, 9.0)

    
    def test_true_func_split_eval(self):
        """Test True result for split_eval()."""
        n = 81
        e_tst = Element(n, sqrt(n))
        self.assertTrue(split_eval(e_tst))

    def test_false_func_split_eval(self):
        """Test False result for split_eval()."""
        n = 82
        e_tst = Element(n, sqrt(n))
        self.assertFalse(split_eval(e_tst))




if __name__ == "__main__":
    unittest.main()