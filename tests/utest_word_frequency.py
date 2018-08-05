import unittest
from text_pipeline import word_frequency


class TestCountWordFrequency(unittest.TestCase):

    def test_count_word_frequency(self):
        self.assertEqual(word_frequency.count_word_frequency(
            ['Alice is lost the wonderland', 'rabbit tells Alice this is not the Wonderland'])
                         , {'rabbit': 1, 'this': 1, 'not': 1, 'wonderland': 1, 'the': 2, 'lost': 1, 'tells': 1,
                            'Alice': 2, 'is': 2, 'Wonderland': 1})

        self.assertEqual(
            word_frequency.count_word_frequency(['rabbit took the key from ALICE', 'Alice is looking for the key']),
            {'took': 1, 'for': 1, 'looking': 1, 'is': 1, 'rabbit': 1, 'from': 1, 'Alice': 1, 'ALICE': 1, 'key': 2,
             'the': 2})


if __name__ == '__main__':
    unittest.main()
