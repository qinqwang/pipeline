import unittest
from text_pipeline import stemming


class TestStemming(unittest.TestCase):

    def setUp(self):
        # list of words
        self.plurals = ['caresses', 'flies', 'dies', 'mules', 'denied',
                        'died', 'agreed', 'owned', 'humbled', 'sized',
                        'meeting', 'stating', 'siezing', 'itemization',
                        'sensational', 'traditional', 'reference', 'colonizer',
                        'plotted']
        self.expected_plurals = ['caress', 'fli', 'die', 'mule', 'deni', 'die',
                                 'agre', 'own', 'humbl', 'size', 'meet', 'state',
                                 'siez', 'item', 'sensat', 'tradit', 'refer', 'colon', 'plot']
        # short string bugs
        self.list_str_bugs = ["father's", "friends"]
        self.list_bugs = ["father", "friend"]

    def test_stemmer(self):
        # check if the list of words works properly
        self.assertEqual(stemming.stemming_list(self.plurals), self.expected_plurals)

    def test_stemmer_stat(self):
        # test the statistic
        self.assertEqual(stemming.stemming_list(self.plurals, static=True, file_name='stemming_test'), self.expected_plurals)

    def test_list_bugs(self):
        self.assertEqual(stemming.stemming_list(self.list_str_bugs), self.list_bugs)


if __name__ == '__main__':
    unittest.main()
