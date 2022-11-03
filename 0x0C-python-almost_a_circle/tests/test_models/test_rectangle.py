#!/usr/bin/python3/
"""
test_rectangle
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_init(unittest.TestCase):
    """ defines the test cases initialization of Rectangle """

    def test_no_args(self):
        """ test with no argument """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """ test with one argument """
        with self.assertRaises(TypeError):
            Rectangle(2)

    def test_rightly(self):
        """ test with the right amount of required arguments """
        r = Rectangle(2, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)

    def test_three_args(self):
        """ test with three args """
        r = Rectangle(2, 10, 4)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 4)

    def test_four_args(self):
        """ test with three args """
        r = Rectangle(2, 10, 4, 3)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 3)

    def test_for_all_attributes(self):
        """ testing all attributes """
        r = Rectangle(2, 10, 4, 3, 12)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 12)

    def test_six_args(self):
        """ test with three args """
        with self.assertRaises(TypeError):
            Rectangle(2, 10, 4, 3, 12, 6)

    def test_instance(self):
        """ test the instance of Rectangle """
        self.assertIsInstance(Rectangle(2, 10), Base)

    def test_id_None(self):
        """ test id using the base attribute """
        r1 = Rectangle(2, 10)
        r2 = Rectangle(10, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_width_privacy(self):
        """ test attr width privacy """
        with self.assertRaises(AttributeError):
            Rectangle(2, 10).__width

    def test_height_privacy(self):
        """ test attr height privacy """
        with self.assertRaises(AttributeError):
            Rectangle(2, 10).__height

    def test_x_privacy(self):
        """ test attr x privacy """
        with self.assertRaises(AttributeError):
            Rectangle(2, 10, 4).__x

    def test_y_privacy(self):
        """ test width attr privacy """
        with self.assertRaises(AttributeError):
            Rectangle(2, 10, 4, 3).__y

    def test_id_privacy(self):
        """ test width attr privacy """
        with self.assertRaises(AttributeError):
            Rectangle(2, 10, 4, 3, 12).__id

    def test_width_getter(self):
        """ tests width getter """
        r = Rectangle(2, 10, 4, 3, 12)
        self.assertEqual(r.width, 2)

    def test_width_setter(self):
        """ tests width setter """
        r = Rectangle(2, 10, 4, 3, 12)
        r.width = 5
        self.assertEqual(r.width, 5)

    def test_height_getter(self):
        """ tests height getter """
        r = Rectangle(2, 10, 4, 3, 12)
        self.assertEqual(r.height, 10)

    def test_height_setter(self):
        """ tests width setter """
        r = Rectangle(2, 10, 4, 3, 12)
        r.height = 7
        self.assertEqual(r.height, 7)

    def test_x_getter(self):
        """ tests x getter """
        r = Rectangle(2, 10, 4, 3, 12)
        self.assertEqual(r.x, 4)

    def test_x_setter(self):
        """ tests x setter """
        r = Rectangle(2, 10, 4, 3, 12)
        r.x = 6
        self.assertEqual(r.x, 6)

    def test_y_getter(self):
        """ tests width getter """
        r = Rectangle(2, 10, 4, 3, 12)
        self.assertEqual(r.y, 3)

    def test_y_setter(self):
        """ tests y setter """
        r = Rectangle(2, 10, 4, 3, 12)
        r.y = 8
        self.assertEqual(r.y, 8)

    def test_id_getter(self):
        """ tests width getter """
        r = Rectangle(2, 10, 4, 3, 12)
        self.assertEqual(r.id, 12)

    def test_id_setter(self):
        """ tests width setter """
        r = Rectangle(2, 10, 4, 3, 12)
        r.id = 9
        self.assertEqual(r.id, 9)



class TestRectangle_width(unittest.TestCase):
    """ defines test cases of the width attribute of Rectangle """

    # Testing different types of width
    def test_width_int(self):
        """ int type """
        self.assertEqual(Rectangle(2, 10).width, 2)

    def test_width_string(self):
        """ string type """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", 10)

    def test_width_byte(self):
        """ string type """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b"Two", 10)

    def test_width_float(self):
        """ float type """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(2.0, 10)

    def test_width_complex(self):
        """ complex type """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(2), 10)

    def test_width_bool(self):
        """ bool type """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 10)

    def test_width_list(self):
        """ list type """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([2], 10)

    def test_width_tuple(self):
        """ tuple type """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((2,), 10)

    def test_width_set(self):
        """ set type """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({2}, 10)

    def test_width_dict(self):
        """ dict type """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({'two': 2}, 10)

    def test_width_None(self):
        """ None type """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 10)

    def test_width_range(self):
        """ range type """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(2), 10)

    def test_width_bytearray(self):
        """ bytearray type """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'two'), 10)

    def test_width_frozenset(self):
        """ frozenset type """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({2, }), 10)

    def test_width_memoryview(self):
        """ memoryview type """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'two'), 10)

    # Testing different values for width
    def test_width_zero(self):
        """ width of value 0 """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 10)

    def test_width_negative(self):
        """ width of negative value """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 10)


class TestRectangle_height(unittest.TestCase):
    """ defines test cases for the height attribute of Rectangle """

    # Testing different types for height
    def test_height_int(self):
        """ int type """
        self.assertEqual(Rectangle(2, 10).height, 10)

    def test_height_string(self):
        """ string type """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, '10')

    def test_height_byte(self):
        """ string type """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, b'Ten')

    def test_height_float(self):
        """ float type """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 10.0)

    def test_height_complex(self):
        """ complex type """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, complex(10))

    def test_height_bool(self):
        """ bool type """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, False)

    def test_height_list(self):
        """ list type """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, [10])

    def test_height_tuple(self):
        """ tuple type """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, (10,))

    def test_height_set(self):
        """ set type """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {10, })

    def test_height_dict(self):
        """ dict type """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {'ten': 10})

    def test_height_None(self):
        """ None type """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_height_range(self):
        """ range type """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, range(10))

    def test_height_bytearray(self):
        """ bytearray type """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, bytearray(b'ten'))

    def test_height_frozenset(self):
        """ frozenset type """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, frozenset({10, }))

    def test_height_memoryview(self):
        """ memoryview type """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, memoryview(b'ten'))

    # Testing different values for height
    def test_height_zero(self):
        """ height of value 0 """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

    def test_height_negative(self):
        """ height of negative value """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -10)


class TestRectangle_x(unittest.TestCase):
    """ defines test cases for the x attribute of Rectangle """

    # Testing different types for height
    def test_x_int(self):
        """ int type """
        self.assertEqual(Rectangle(2, 10, 4).x, 4)

    def test_x_string(self):
        """ string type """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 10, '4')

    def test_x_byte(self):
        """ string type """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 10, b'four')

    def test_x_float(self):
        """ float type """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 10, 4.0)

    def test_x_complex(self):
        """ complex type """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 10, complex(4))

    def test_x_bool(self):
        """ bool type """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 10, True)

    def test_x_list(self):
        """ list type """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 10, [4])

    def test_x_tuple(self):
        """ tuple type """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 10, (4, ))

    def test_x_set(self):
        """ set type """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 10, {4, })

    def test_x_dict(self):
        """ dict type """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 10, {'four': 4})

    def test_x_None(self):
        """ None type """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 10, None)

    def test_x_range(self):
        """ range type """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 10, range(4))

    def test_x_bytearray(self):
        """ bytearray type """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 10, bytearray(b'four'))

    def test_x_frozenset(self):
        """ frozenset type """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 10, frozenset({4, }))

    def test_x_memoryview(self):
        """ memoryview type """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 10, memoryview(b'four'))

    # Testing different negative value for x
    def test_x_negative(self):
        """ x of negative value """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 10, -4)


class TestRectangle_y(unittest.TestCase):
    """ defines test cases for the x attribute of Rectangle """

    # Testing different types for height
    def test_y_int(self):
        """ int type """
        self.assertEqual(Rectangle(2, 10, 4, 3).y, 3)

    def test_y_string(self):
        """ string type """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 10, 4, '3')

    def test_y_byte(self):
        """ string type """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 10, 4, b'three')

    def test_y_float(self):
        """ float type """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 10, 4, 3.0)

    def test_y_complex(self):
        """ complex type """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 10, 4, complex(3))

    def test_y_bool(self):
        """ bool type """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 10, 4, True)

    def test_y_list(self):
        """ list type """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 10, 4, [3])

    def test_y_tuple(self):
        """ tuple type """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 10, 4, (3, ))

    def test_y_set(self):
        """ set type """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 10, 4, {3, })

    def test_y_dict(self):
        """ dict type """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 10, 4, {'three': 3})

    def test_y_None(self):
        """ None type """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 10, 4, None)

    def test_y_range(self):
        """ range type """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 10, 4, range(3))

    def test_y_bytearray(self):
        """ bytearray type """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 10, 4, bytearray(b'three'))

    def test_y_frozenset(self):
        """ frozenset type """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 10, 4, frozenset({3, }))

    def test_y_memoryview(self):
        """ memoryview type """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 10, 4, memoryview(b'three'))

    # Testing different negative value for x
    def test_y_negative(self):
        """ y of negative value """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 10, 4, -3)


class TestRectangle_initialization_order(unittest.TestCase):
    """ test the order of initialization """

    def test_width_before_height(self):
        """ test invalid width before invalid height """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", "height")

    def test_width_before_x(self):
        """ test invalid width before invalid x """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", 10, "x")

    def test_width_before_y(self):
        """ test invalid width before invalid y """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", 10, 4, "y")

    def test_height_before_x(self):
        """ test invalid height before invalid x """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "height", "x", 3)

    def test_height_before_y(self):
        """ test invalid height before invalid y """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "height", 4, "y")

    def test_x_before_y(self):
        """ test invalid x before invalid y """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 10, "x", "y")


class TestRectangle_area(unittest.TestCase):
    """ defines test cases for the area method Rectangle instance """

    def test_area_small(self):
        """ test with right data types and values """
        r = Rectangle(2, 10, 4, 3, 12)
        self.assertEqual(r.area(), 20)

    def test_area_large(self):
        r = Rectangle(999999999999999, 999999999999999, 1, 2, 1)
        self.assertEqual(r.area(), 999999999999998000000000000001)

    def test_area_with_one_arg(self):
        r = Rectangle(2, 10, 4, 3, 12)
        with self.assertRaises(TypeError):
            r.area(1)

class TestRectangle_stdout(unittest.TestCase):
    """ test cases for __str__ and display methods of Rectangle instances """

    @staticmethod
    def redirect_stdout(rectangle, method):
        """ redirect and returns the text printed to stdout """

        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rectangle)
        else:
            rectangle.display()
        sys.stdout = sys.__stdout__
        return capture

    # Test display method
    def test_display_width_height(self):
        """ testing the display method with only width and height """
        r = Rectangle(2, 2)
        capture = TestRectangle_stdout.redirect_stdout(r, "display")
        self.assertEqual(capture.getvalue(), "##\n##\n")

    def test_display_width_height_x(self):
        """ testing the display method with width, height and x"""
        r = Rectangle(4, 2, 2, 0, 0)
        capture = TestRectangle_stdout.redirect_stdout(r, "display")
        self.assertEqual(capture.getvalue(), "  ####\n  ####\n")

    def test_display_width_height_x_y(self):
        """ testing the display method with width, height, x and y """
        r = Rectangle(4, 2, 2, 3, 0)
        capture = TestRectangle_stdout.redirect_stdout(r, "display")
        self.assertEqual(capture.getvalue(), "\n\n\n  ####\n  ####\n")

    def test_display_with_args(self):
        """ testing the display method with arguments """
        r = Rectangle(4, 3, 2, 1, 0)
        with self.assertRaises(TypeError):
            r.display(5)

    # Test __str__ method
    def test_str_width_height(self):
        """ test __str__ with print using width and height only """
        r = Rectangle(4, 6)
        capture = TestRectangle_stdout.redirect_stdout(r, "print")
        text = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(capture.getvalue(), text)

    def test_str_width_height_x(self):
        """ test __str__ using default dictionary with width, height, and x """
        r = Rectangle(4, 6, 2)
        text = "[Rectangle] ({}) 2/0 - 4/6".format(r.id)
        self.assertEqual(r.__str__(), text)

    def test_str_width_height_x_y(self):
        """ test __str__ typecasting - str - with width, height, x, and y """
        r = Rectangle(4, 6, 2, 1)
        text = "[Rectangle] ({}) 2/1 - 4/6".format(r.id)
        self.assertEqual(str(r), text)

    def test_str_width_height_x_y_id(self):
        """ test __str__ typecasting - str - with width, height, x, and y """
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_with_one_arg(self):
        r = Rectangle(4, 6, 2, 1, 12)
        with self.assertRaises(TypeError):
            r.__str__(1)


class TestRectangle_update_args(unittest.TestCase):
    """ defines test cases for the method update of Rectangle instance """

    def test_update_args_zero(self):
        """ call update with no argument """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_one(self):
        """ call update with one argument """
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_args_two(self):
        """ call update with two args """
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_args_three(self):
         """ call update with three args """
         r = Rectangle(10, 10, 10, 10)
         r.update(89, 2, 3)
         self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_args_four(self):
         """ call update with four args """
         r = Rectangle(10, 10, 10, 10)
         r.update(89, 2, 3, 4)
         self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_args_five(self):
        """ call update with five args """
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_more_than_five(self):
        """ call update with more than 5 args """
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 7)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_twice(self):
        """ update the attributes twice """
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        r.update(98, 5, 4, 3, 2)
        self.assertEqual("[Rectangle] (98) 3/2 - 5/4", str(r))

    def test_update_args_none_type_id(self):
        """ test update with None type id """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_none_type_id_and_others(self):
        """ test update with None type id """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (10) 4/5 - 2/3", str(r))

    def test_update_args_order_width_before_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "width", "height", 4, 5)

    def test_update_args_order_width_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "width", 3, "x", 5)

    def test_update_args_order_width_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "width", 3, 4, "y")

    def test_update_args_order_height_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "height", "x", 5)

    def test_update_args_order_height_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "height", 4, "y")

    def test_update_args_order_x_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "x", "y")


class TestRectangle_update_kwargs(unittest.TestCase):
    """ defines test cases for the method update of Rectangle instance """

    def test_update_kwargs_zero(self):
        """ call update with no kw argument """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_kwargs_one(self):
        """ call update with one kw argument """
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        """ call update with two kw args """
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
         """ call update with three args """
         r = Rectangle(10, 10, 10, 10)
         r.update(width=2, id=89, height=3)
         self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
         """ call update with four kw args """
         r = Rectangle(10, 10, 10, 10)
         r.update(height=3, x=4, id=89, width=2)
         self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_kwargs_five(self):
        """ call update with five kw args """
        r = Rectangle(10, 10, 10, 10)
        r.update(y=5, x=4, height=3, width=2, id=89)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_kwargs_more_than_five(self):
        """ call update with more than 5 args """
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=2, height=3, x=4, y=5, unknown=7)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_kwargs_twice(self):
        """ update the key-worded attributes twice """
        r = Rectangle(10, 10, 10, 10)
        r.update(height=3, x=4, id=89, width=2, y=5)
        r.update(id=98, width=5, height=4, x=3, y=2)
        self.assertEqual("[Rectangle] (98) 3/2 - 5/4", str(r))

    def test_update_args_and_kwarg(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=3, y=5)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_all_absent(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(ab=4, cd=6)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
