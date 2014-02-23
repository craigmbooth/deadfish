import unittest
from StringIO import StringIO
import deadfish as mod_ut

class TestParenFinder(unittest.TestCase):
    """Tests of the method that checks for unbalanced parens"""

    def test_parens__balanced(self):
        """Test that we find well balanced parens"""
        self.assertEqual(mod_ut.find_matching_paren("AAA)", "(", ")"),
                         3)
        self.assertEqual(mod_ut.find_matching_paren("A()AA)", "(", ")"),
                         5)

    def test_parens_unbalanced(self):
        """Test that we register unbalanced parens"""
        self.assertEqual(mod_ut.find_matching_paren("((AA)", "(", ")"),
                         -1)

        self.assertEqual(mod_ut.find_matching_paren("(A()A)", "(", ")"),
                         -1)

    def test_parens__empty(self):
        """Test that finding parens on an empty string returns -1"""
        self.assertEqual(mod_ut.find_matching_paren("", "(", ")"),
                         -1)

    def test_parens__symbol(self):
        """Test that finding parens works with arbitrary symbols"""
        self.assertEqual(mod_ut.find_matching_paren("1a1df222", "1", "2"),
                         7)


class TestUtilFuncs(unittest.TestCase):
    """Various tests of utility functions for deadfish"""

    def test_reset_accum(self):
        """Test that we reset the accumulator at -1 and 256"""
        self.assertEqual(mod_ut.reset_accum((-1, "")), (0, ""))
        self.assertEqual(mod_ut.reset_accum((0, "")), (0, ""))
        self.assertEqual(mod_ut.reset_accum((1, "")), (1, ""))
        self.assertEqual(mod_ut.reset_accum((2, "")), (2, ""))
        self.assertEqual(mod_ut.reset_accum((256, "")), (0, ""))

    def test_w(self):
        """Test that we can write Hello, World! to the output target,
        and that the function passes the first input options through"""
        out = StringIO()
        retval = mod_ut.print_world(1, 2, out=out)
        result = out.getvalue().strip()
        self.assertEqual(result, "Hello, World!")
        self.assertEqual(retval, (1, 2))

    def test_o(self):
        """Test printing the accumulator to the output target"""
        out = StringIO()
        mod_ut.print_accum(0, out=out)
        result = out.getvalue().strip()
        self.assertEqual(result, "0")

        out = StringIO()
        mod_ut.print_accum(70, out=out)
        result = out.getvalue().strip()
        self.assertEqual(result, "70")

    def test_c(self):
        """Test printing the accumulator as a character to the output"""
        out = StringIO()
        mod_ut.print_accum(98, out=out, char=True)
        result = out.getvalue().strip()
        self.assertEqual(result, "b")

        out = StringIO()
        mod_ut.print_accum(73, out=out, char=True)
        result = out.getvalue().strip()
        self.assertEqual(result, "I")

class TestDeadfish(unittest.TestCase):
    """Tests of the Deadfish method"""

    def test_deadfish__simple(self):
        """Test simple cases for deadfish"""
        self.assertEqual(mod_ut.deadfish("ii"), 2)
        self.assertEqual(mod_ut.deadfish("dd"), 0)
        self.assertEqual(mod_ut.deadfish("iiddi"), 1)
        self.assertEqual(mod_ut.deadfish("iisss"), 0)
        self.assertEqual(mod_ut.deadfish("iissis"), 289)

    def test_deadfish__loop(self):
        """Test the {} construct for looping"""
        self.assertEqual(mod_ut.deadfish("{{i}}"), 100)
        self.assertEqual(mod_ut.deadfish("{{i}}i{d}"), 91)

    def test_deadfish__loop_broken(self):
        """Test that the {} construct is ignored if parens are not nested"""
        self.assertEqual(mod_ut.deadfish("{{i}"), 10)
        self.assertEqual(mod_ut.deadfish("}}}}}iid"), 1)

    def test_deadfish__cond(self):
        """Test that things inside of () are executed only if the
        the accumulator is non-zero"""
        self.assertEqual(mod_ut.deadfish("i(iii)"), 4)
        self.assertEqual(mod_ut.deadfish("id(iii)i"), 1)

if __name__ == "__main__":
    unittest.main()
