import unittest
from text_pipeline import pipeline


class TestPipeline(unittest.TestCase):

    def setUp(self):
        # raw data
        self.text1 = ['I have a dream.']
        # token, stop_words, remove punctuations
        self.expected_text1 = ['I', 'dream']
        # load same module function
        self.function_same_module = [('tokenize_words', {}), ('stop_words_removal', {'language': 'en'}),
                                     ('remove_punct', {})]
        # load different modules function
        self.function_in_diff = [('tokenize_words', {}), ('remove_punct', {}), ('spell_check_list', {}),
                                 ('stemming_list', {})]
        self.text2 = ['caresses flies, dies mules denied\
                        died, agreeed owned humbled sized,\
                        meeting statng ! siezing \
                        senssational traditional reference  plotted']
        self.expected_text2 = ['caress', 'fli', 'die', 'mule', 'deni',
                               'die', 'agre', 'own', 'humbl', 'size', 'meet', 'state',
                               'seiz', 'sensat', 'tradit', 'refer', 'plot']

        self.function_in_diff_args = [('tokenize_words', {}), ('remove_punct', {}),
                                      ('spell_check_list', {'static': True}),
                                      ('stemming_list', {'lang': 'en', 'static': True})]

        self.function_name_file = [('tokenize_words', {}), ('remove_punct', {}),
                                   ('spell_check_list', {'static': True, 'file_name': 'name_spell_check'}),
                                   ('stemming_list', {'lang': 'en', 'static': True, 'file_name': 'name_stemming_file'})]
        # test lemma and word frequency on pipeline
        self.fun_lemma_wordfreq = [('lemma', {'static': True, 'file_name': 'test_lemma'}),
                                   ('count_word_frequency', {'static': True, 'file_name': 'test_word_frequency'})]
        self.text3 = ['fruits', 'are', 'unhealthy']
        self.expected_text3 = {'fruit': 1, 'be': 1, 'unhealthy': 1}

    def test_pipeline_same_module(self):
        # three functions at the same module
        my_pipeline = pipeline.Pipeline(self.function_same_module)
        self.assertEqual(my_pipeline(self.text1), self.expected_text1)

    def test_pipeline_diff_module(self):
        my_pipeline = pipeline.Pipeline(self.function_in_diff)
        self.assertEqual(my_pipeline(self.text2), self.expected_text2)

    def test_pipeline_diff_arguments(self):
        my_pipeline = pipeline.Pipeline(self.function_in_diff_args)
        self.assertEqual(my_pipeline(self.text2), self.expected_text2)

    def test_pipeline_name_statistic(self):
        my_pipeline = pipeline.Pipeline(self.function_name_file)
        self.assertEqual(my_pipeline(self.text2), self.expected_text2)

    def test_pipeline_lemma_wordfreq(self):
        my_pipeline = pipeline.Pipeline(self.fun_lemma_wordfreq)
        self.assertEqual(my_pipeline(self.text3), self.expected_text3)


if __name__ == '__main__':
    unittest.main()
