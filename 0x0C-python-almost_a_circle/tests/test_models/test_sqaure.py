#!/usr/bin/python3
"""
test_sqaure
"""

import io
import sys
from models.rectangle import Rectangle
from models.square import Square

class TestSquare_init(unittest.TestCase):
    """ defines test cases for the initliazation of instance of Square """

    def test_instance(self):
        self.assertIsInstance(Square(4), Rectangle)

    def test_size_privacy(self):
        with self.assertRaises(AttributeError):
            Square(4).__size

    def test_size_getter(self):
        s = Square(4)
        self.assertEqual(s.size, 4)

    def test_size_setter(self):
        s = Square(4)
        s.size = 5
        self.assertEqual(s.size, 5)

    # Testing for each attribute inheritance
    def test_string_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("size")

    def test_size_value(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, [x])

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 2, 3.0)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(4, 2, -3)


class TestSquare_order_of_initialization(unittest.TestCase):
    """ defines test cases for the order of initilization
    of new instance of Square """

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("size", "x", 3)

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be > 0"):
            Square(-4, 2, "y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, "x", "y")

class TestSquare_update_args(unittest.TestCase):
    """ defines test cases for the update method of Square using args """

    def test_zero_args(self):
        s = Square(4, 2, 3, 12)
        s.update()
        self.assertEqual("[Square] (12) 2/3 - 4", str(s))

    def test_one_args(self):
        s = Square(4, 2, 3, 12)
        s.update(5)
        self.assertEqual("[Square] (5) 2/3 - 4", str(s))

    def test_two_args(self):
        s = Square(4, 2, 3, 12)
        s.update(5, 6)
        self.assertEqual("[Square] (5) 2/3 - 6", str(s))

    def test_three_args(self):
        s = Square(4, 2, 3, 12)
        s.update(5, 6, 4)
        self.assertEqual("[Square] (5) 4/3 - 6", str(s))

    def test_four_args(self):
        s = Square(4, 2, 3, 12)
        s.update(5, 7, 8, 4)
        self.assertEqual("[Square] (5) 8/4 - 7", str(s))

    def test_more_than_four_args(self):
        s = Square(4, 2, 3, 12)
        s.update(5, 7, 8, 4)
        self.assertEqual("[Square] (5) 8/4 - 7", str(s))

    def test_update_twice(self):
        s = Square(4, 2, 3, 12)
        s.update(4, 7)
        s.update(8, 4, 3, 2)
        self.assertEqual("[Square] (8) 3/2 - 4", str(s))

    def test_update_None_id(self):
        s = Square(4, 2, 3, 12)
        s.update(None)
        self.assertEqual("[Square] (12) 2/3 - 4", str(s))

    def test_update_None_id_with_others(self):
        s = Square(4, 2, 3, 12)
        s.update(None, 5, 7, 8)
        self.assertEqual("[Square] (12) 7/8 - 5", str(s))

    def test_update_order_size_before_x(self):
        s = Square(4, 2, 3, 12)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(4, "size", "x", 5)

    def test_update_order_size_before_y(self):
        s = Square(4, 2, 3, 12)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(4, "size", 3, "y")

    def test_update_order_x_before_y(self):
        s = Square(4, 2, 3, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(4, 6, "x", "y")


class TestSquare_update_kwargs(self):
    """ defines test cases for the update method of Square using kwargs """

    def test_absent_kwargs(self):
        s = Square(4, 2, 3, 12)
        s.update(origin=5)
        self.assertEqual("[Square] (12) 2/3 - 4", str(s))

    def test_id_kwargs(self):
        s = Square(4, 2, 3, 12)
        s.update(id=5)
        self.assertEqual("[Square] (5) 2/3 - 4", str(s))

    def test_size_id_kwargs(self):
        s = Square(4, 2, 3, 12)
        s.update(size=6, id=7)
        self.assertEqual("[Square] (7) 2/3 - 6", str(s))

    def test_x_id_size_kwargs(self):
        s = Square(4, 2, 3, 12)
        s.update(x=5, size=6, id=4)
        self.assertEqual("[Square] (4) 5/3 - 6", str(s))

    def test_y_size_x_id_kwargs(self):
        s = Square(4, 2, 3, 12)
        s.update(y=5, size=7, id=8, x=4)
        self.assertEqual("[Square] (8) 4/8 - 7", str(s))

    def test_update_absent_and_present_kwargs(self):
        s = Square(4, 2, 3, 12)
        s.update(old=5, id=7, new=8, y=4)
        self.assertEqual("[Square] (7) 8/4 - 7", str(s))

    def test_update_kwargs_twice(self):
        s = Square(4, 2, 3, 12)
        s.update(id=4, x=7)
        s.update(size=8, x=4, y=3, id=2)
        self.assertEqual("[Square] (2) 4/3 - 8", str(s))

    def test_update_args_and_kwargs(self):
        s = Square(4, 2, 3, 12)
        s.update(89, 5, id=7, size=7)
        self.assertEqual("[Square] (89) 2/3 - 5", str(s))

    def test_update_kwargs_all_absent(self):
        s = Square(4, 2, 3, 7)
        s.update(absent="8", key="5", word="7")
        self.assertEqual("[Square] (7) 2/3 - 4",str(s))
