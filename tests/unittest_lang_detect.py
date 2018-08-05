from text_pipeline import lang_detect
import unittest


class TestLangDetect(unittest.TestCase):

    def test_lang_detect(self):
        # test english
        lang = lang_detect.detect_language('I do not speak english')
        self.assertEqual(lang, 'en')

    def test_lang_detect_upper_case(self):
        # test upper case
        lang = lang_detect.detect_language('I DO NOT SPEAK ENGLISH')
        self.assertEqual(lang, 'en')

    def test_empty(self):
        # input empty value
        with self.assertRaises(ValueError):
            lang_detect.detect_language('')

    def test_None(self):
        # input None
        with self.assertRaises(ValueError):
            lang_detect.detect_language(None)

    def test_type_wrong(self):
        # input integer
        with self.assertRaises(ValueError):
            lang_detect.detect_language(123)


if __name__ == '__main__':
    unittest.main()
