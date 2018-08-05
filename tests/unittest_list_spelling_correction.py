import unittest
from text_pipeline import spell_check


class TestListSpellingCorrection(unittest.TestCase):

    def setUp(self):
        # list of all wrong words
        self.data = ['peotryy', 'speling', 'korrectud', 'bycycle']
        self.cor_data = ['poetry', 'spelling', 'corrected', 'bicycle']
        # single word with wrong spelling data
        self.single_data = ['E', 'peotryy', 'speling', 'a', 'korrectud', 'bycycle']
        self.cor_single = ['poetry', 'spelling', 'corrected', 'bicycle']
        # mix data (right words + wrong spelling words)
        self.mix_data = ['peotryy', 'speling', 'test', 'korrectud', 'bycycle']
        self.mix_cor_data = ['poetry', 'spelling', 'test', 'corrected', 'bicycle']
        # right spelling data
        self.right_data = ['poetry', 'spelling', 'corrected', 'bicycle']

    def test_list_spell_check(self):
        # correct the list of spelling mistakes
        self.assertEqual(spell_check.spell_check_list(self.data), self.cor_data)
        # filter out the single words and correct spell mistake
        self.assertEqual(spell_check.spell_check_list(self.single_data), self.cor_single)
        # only correct the wrong spelling words
        self.assertEqual(spell_check.spell_check_list(self.mix_data), self.mix_cor_data)

    def test_list_right_data(self):
        # right bunch of words
        self.assertEqual(spell_check.spell_check_list(self.right_data), self.right_data)

    def test_list_check_statistic(self):
        # only correct the wrong spelling words
        self.assertEqual(spell_check.spell_check_list(self.mix_data, True, file_name='spell_check_test'), self.mix_cor_data)


if __name__ == '__main__':
    unittest.main()
