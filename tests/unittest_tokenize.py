import unittest
from text_pipeline import pipe_token


class TestPreprocess(unittest.TestCase):

    def test_stopwords(self):
        # english: get rid of english stopwords
        data = ['I', 'have', 'a', 'dream', '.']
        self.assertEqual(pipe_token.stop_words_removal(data, 'en'), ['I', 'dream', '.'])

    def test_stopwords_statistic(self):
        data = ['I', 'have', 'a', 'dream', '.', 'This', 'is', 'the', 'stopwords']
        self.assertEqual(pipe_token.stop_words_removal(data, 'en', True, file_name='stopwords_test'), ['I', 'dream', '.', 'This', 'stopwords'])

    def test_punct_remove(self):
        # punctuation at end
        data = ['I', 'have', 'a', 'dream', '.']
        self.assertEqual(pipe_token.remove_punct(data), ['I', 'have', 'a', 'dream'])
        # punctuation in the middle
        data = ['I', 'have', ',', 'a', 'dream']
        self.assertEqual(pipe_token.remove_punct(data), ['I', 'have', 'a', 'dream'])
        # a lot of punctuations
        data = ['I', ',', 'have', ':', 'a', 'dream', '.']
        self.assertEqual(pipe_token.remove_punct(data), ['I', 'have', 'a', 'dream'])

    def test_tokenize(self):
        # raw data
        text = ['I have a dream.']
        self.assertEqual(pipe_token.tokenize_words(text), ['I', 'have', 'a', 'dream', '.'])

    def test_tokenize_time(self):
        # The list contains the time information
        text = ['2010-10-25 Jan 01 Jun 1st Its Fri']
        self.assertEqual(pipe_token.tokenize_words(text, keep_date=True), ['2010-10-25', 'Jan 01', 'Jun 1st', 'Its', 'Fri'])

    def test_tokenize_times(self):
        # The list of times and other information
        text = ['2010-10-25 Jan 01 Jun 1st Its Fri Jan 1st Jan 3rd 1995-01-13']
        self.assertEqual(pipe_token.tokenize_words(text, keep_date=True),
                         ['2010-10-25', 'Jan 01', 'Jun 1st', 'Its', 'Fri', 'Jan 1st', 'Jan 3rd', '1995-01-13'])

    def test_tokenize_upper_case_times(self):
        # The list of different types of times
        text = ['2010-10-25 Jan 01 JUN 1st Its Fri jan 1st JAn 3rd 1995-01-13']
        self.assertEqual(pipe_token.tokenize_words(text, keep_date=True),
                         ['2010-10-25', 'Jan 01', 'JUN 1st', 'Its', 'Fri', 'jan 1st', 'JAn 3rd', '1995-01-13'])

    def test_empty_tokenize(self):
        with self.assertRaises(ValueError):
            pipe_token.tokenize_words('')

    def test_type_wrong_tokenize(self):
        # wrong type
        with self.assertRaises(ValueError):
            pipe_token.tokenize_words(123)

    def test_None_tokenize(self):
        # None
        with self.assertRaises(ValueError):
            pipe_token.tokenize_words(None)

    def test_code_covert(self):
        # test english
        self.assertEqual(pipe_token.code_convert('en'), 'English')
        # test chinese
        self.assertEqual(pipe_token.code_convert('zh'), 'Chinese')


if __name__ == '__main__':
    unittest.main()
