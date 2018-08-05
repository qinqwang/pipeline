import unittest
from text_pipeline import pipe_token
from text_pipeline import string_to_function


class TestStrToFunc(unittest.TestCase):

    def setUp(self):
        self.cor_name = 'remove_punct'
        self.exp_cor_func = (pipe_token,'remove_punct')

    def test_correct_transfer(self):
        # test if return proper function
        self.assertEqual(string_to_function.string_to_function(self.cor_name), self.exp_cor_func)

    def test_exception(self):
        # test the exception: the dictionary doesn't hava the function
        with self.assertRaises(Exception):
            string_to_function.string_to_function('hello')


if __name__ == '__main__':
    unittest.main()
