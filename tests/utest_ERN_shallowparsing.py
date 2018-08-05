import unittest
from text_pipeline import ERN_shallow_parse
import re
import nltk



class TestERN_ShallowParsing(unittest.TestCase):

    def test_chunks(self):
        self.assertEqual(ERN_shallow_parse.shallow_parse(
                ["adventure", "movies", "in","2015","featuring",
                    "performanced","by" ,"daniel", "craig"]),
                ['adventure movies', 'featuring', 'daniel craig'])

    def test_chunks(self):
        self.assertEqual(ERN_shallow_parse.shallow_parse(
            ["daniel", "craig","plays","the","role","of","Ian","Fleming's","British",
                "secret", "agent", "character", "James", "Bond"]),
            ['daniel craig', 'role', "ian fleming's british secret agent character james bond"])

    def test_chunks(self):
        self.assertEqual(ERN_shallow_parse.shallow_parse(
            ["craig","has","continued","to","star","in","two","other","films"]),
            ['craig', 'two films'])


if __name__ == '__main__':
    unittest.main()