import unittest
from collections import Counter
from text_pipeline import spelling_correction
import re


class TestSpellingCorrection(unittest.TestCase):


    def test_insert(self):
        self.assertEqual(spelling_correction.correction('speling'), 'spelling')


    def test_replace(self):
        self.assertEqual(spelling_correction.correction('prscticr'), 'practice')

    def test_replace_insert(self):
        self.assertEqual(spelling_correction.correction('pschologi'),'psychology')

    def test_replace_twice(self):
        self.assertEqual(spelling_correction.correction('inconvineent'), 'inconvenient')

    def test_delete(self):
        self.assertEqual(spelling_correction.correction('salmoon'),'salmon')

    def test_transpose(self):
        self.assertEqual(spelling_correction.correction('baer'), 'bear')

    def test_tranpose_delete(self):
        self.assertEqual(spelling_correction.correction('poetryy'), 'poetry')

    def test_known(self):
        self.assertEqual(spelling_correction.correction('dummy'),'dummy')

    def test_split_lower(self):
        self.assertEqual(spelling_correction.words("the tree fell on IT and squashed IT"), ["the", "tree", "fell", "on", "it", "and", "squashed", "it"])

    def test_word_count(self):
        self.assertEqual(Counter(spelling_correction.words('I wrote unit test, I finished UNIT TEST')),(Counter({'i':2,'unit':2 ,'test':2,'wrote':1, 'finished':1})))


if __name__ == '__main__':
    unittest.main()



