import unittest
from text_pipeline import noise_removal


class TestNoiseRemoval(unittest.TestCase):

    def setUp(self):
        pass

    def test_only_unicode(self):
        # test the unicode noise independently
        text = 'Nº ©'
        result = noise_removal._clean_data(noise_removal.rgx_list, text)
        self.assertEqual(result, ' ')

    def test_mixed_unicode(self):
        # test the noise with other data
        text = 'Nº © Shareholders Meeting of the SICAVs approving, North in particular, the following resolutions'
        expected_text = '  Shareholders Meeting of the SICAVs approving, North in particular, the following resolutions'
        result = noise_removal._clean_data(noise_removal.rgx_list, text)
        self.assertEqual(result, expected_text)

    def test_only_item_list(self):
        # only test the item list such as (i), (iv), (vi)
        text = '(i) (iv) (vi) (vii) 1.1.2 1.2.3 1.'
        result = noise_removal._clean_data(noise_removal.rgx_list, text)
        # 5 withe spaces
        self.assertEqual(result, '      ')

    def test_mixed_item_list(self):
        # test item list with other data
        text = '(i) (iv) (vi) (vii) 1.1.2 1.2.3 1. 12.23.13 01. amended on 8 November 2011) 24 sep 1993'
        expected_text = '         amended on 8 November 2011) 24 sep 1993'
        result = noise_removal._clean_data(noise_removal.rgx_list, text)
        self.assertEqual(result, expected_text)

    def test_only_footpage(self):
        # only test the foot page
        text = 'AMSDAM-1-88460689820-4-51-v8.14 AMSDAM-1-884606-v8'
        result = noise_removal._clean_data(noise_removal.rgx_list, text)
        self.assertEqual(result, ' ')

    def test_mixed_footpage(self):
        # text footpage with data
        text = 'Email: CORPORATEFINANCE@REGGEFIBER.NL AMSDAM-1-88460689820-4-51-v8.14 THE ORIGINAL COMMERCIAL LENDERS AMSDAM-1-884606-v8'
        expected_text = 'Email: CORPORATEFINANCE@REGGEFIBER.NL  THE ORIGINAL COMMERCIAL LENDERS '
        result = noise_removal._clean_data(noise_removal.rgx_list, text)
        self.assertEqual(result, expected_text)

    def test_single_page_number(self):
        # only test the page number
        text = '- 23 -'
        result = noise_removal._clean_data(noise_removal.rgx_list, text)
        self.assertEqual(result, '')

    def test_mixed_page_number(self):
        # test page number with data
        text = 'corresponding Dutch terms in the relevant Minimum Penetration Guarantee. - 23 -'
        expected_text = 'corresponding Dutch terms in the relevant Minimum Penetration Guarantee. '
        result = noise_removal._clean_data(noise_removal.rgx_list, text)
        self.assertEqual(result, expected_text)

    def test_single_catalogue(self):
        # get rid of the single catalogue
        text = 'Role of Security Agent............................................................................................... 115'
        result = noise_removal._clean_data(noise_removal.rgx_list, text)
        self.assertEqual(result, '')

    def test_single_dots(self):
        # get rid of the single dots
        text = '..............................'
        result = noise_removal._clean_data(noise_removal.rgx_list, text)
        self.assertEqual(result, '')


if __name__ == '__main__':
    unittest.main()
