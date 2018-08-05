import unittest
from collections import Counter
from text_pipeline import lemmatization_pos
import re
import nltk
import warnings


class TestPOS_Lemmatization(unittest.TestCase):

    def test_lemmatization(self):
        warnings.simplefilter("ignore")
        self.assertEqual(lemmatization_pos.lemma(['fruits', 'are', 'unhealthy'], False, False), ['fruit', 'be', 'unhealthy'])

    def test_lemmatization(self):
        warnings.simplefilter("ignore")
        self.assertEqual(lemmatization_pos.lemma(['none', 'of', 'the', 'vegetables','is','untasty'], True, False),
                         (['none', 'of', 'the', 'vegetable', 'be', 'untasty'],
                          [('none', 'NN'), ('of', 'IN'), ('the', 'DT'),
                           ('vegetables', 'NNS'), ('is', 'VBZ'), ('untasty', 'JJ')]))

    def test_adjective_POS_tag(self):
        warnings.simplefilter("ignore")
        self.assertEqual(lemmatization_pos.get_wordnet_pos_tag('JJ'), 'a')

    def test_verb_POS_tag(self):
        warnings.simplefilter("ignore")
        self.assertEqual(lemmatization_pos.get_wordnet_pos_tag('VERB'), 'v')

    def test_noun_POS_tag(self):
        warnings.simplefilter("ignore")
        self.assertEqual(lemmatization_pos.get_wordnet_pos_tag('NOUN'), 'n')

    def test_adverb_POS_tag(self):
        warnings.simplefilter("ignore")
        self.assertEqual(lemmatization_pos.get_wordnet_pos_tag('RN'), 'r')


if __name__ == '__main__':
    unittest.main()