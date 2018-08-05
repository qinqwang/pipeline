import unittest
from text_pipeline import statistic


class TestStatistic(unittest.TestCase):
    def setUp(self):
        self.original_data = ['working', 'working', 'works', 'worked', 'works', 'working']
        self.affected_data = ['work', 'work', 'work', 'work', 'work', 'work']
        # expected data = {original words: [word_frequency, affected_word]}
        self.expected_data = {'worked': [1, 'work'], 'working': [3, 'work'], 'works': [2, 'work']}

    def test_construct_type(self):
        # test type
        self.assertTrue(isinstance(statistic.reconstruct_dic(self.original_data, self.affected_data), dict))

    def test_construct_value(self):
        # test value
        result = statistic.reconstruct_dic(self.original_data, self.affected_data)
        self.assertEqual(result['working'][0], 3)

    def test_construct_all(self):
        # test all result
        result = statistic.reconstruct_dic(self.original_data, self.affected_data)
        self.assertEqual(result, self.expected_data)


if __name__ == '__main__':
    unittest.main()
