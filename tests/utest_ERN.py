import unittest
from text_pipeline import ERN
import re
import nltk
import warnings


class TestERN_ShallowParsing(unittest.TestCase):

    def test_entity_person(self):
        warnings.simplefilter("ignore")
        self.assertEqual(ERN.entity_recognition("Dr. Henry Walton 'Indiana' Jones Jr. is the character played by Harrison Ford ."
                                                " Corey Carrier , Sean Patrick also played the role Indiana Jones Jr"),

                            [('PERSON', 'Henry Walton'), ('PERSON', 'Jones Jr.'), ('PERSON', 'Harrison Ford'),
                            ('PERSON', 'Corey Carrier'), ('PERSON', 'Sean Patrick'), ('PERSON', 'Indiana Jones Jr')])

    def test_entity_location(self):
        warnings.simplefilter("ignore")
        self.assertEqual(ERN.entity_recognition("Canary Wharf is in East London , it is easy to travel to Canada Water or Stratford from Canary Wharf . "
                                                "Other places I want to visit is Jordan , Le Shan  "),

                         [('GPE', 'East London'), ('GPE', 'Canada'), ('GPE', 'Canary Wharf'),
                          ('GPE', 'Jordan'), ('PERSON', 'Le Shan')])

    def test_entity_organization(self):
        warnings.simplefilter("ignore")
        self.assertEqual(ERN.entity_recognition(" Clifford Chance security questions are from RBS , CitiBank , Swiss Bank , Deutsche bank ."
                                                " Amazon surpassed Walmart as the most valuable retailer "),

                         [('PERSON', 'Clifford'), ('ORGANIZATION', 'RBS'), ('ORGANIZATION', 'CitiBank'),
                          ('PERSON', 'Swiss Bank'), ('ORGANIZATION', 'Deutsche'), ('PERSON', 'Amazon'),
                          ('PERSON', 'Walmart')])

if __name__ == '__main__':
    unittest.main()