import unittest
from src.services.capital_city import CountryCapitals as cc


class TestCountryCapitals(unittest.TestCase):

    def test_valid_code(self):
        country = cc(country_code='can')
        self.assertEqual(country.capital_city() == 'Ottawa', True)

    def test_valid_name(self):
        country = cc(country_code='Colombia')
        self.assertEqual(country.capital_city() == 'Bogotá', True)

    def test_invalid_code(self):
        country = cc(country_code='iu')
        self.assertEqual(country.capital_city() == 'Not found', True)

    def test_invalid_name(self):
        country = cc(country_code='iuiuoihghhgh')
        self.assertEqual(country.capital_city() == 'Not found', True)

    def test_no_input(self):
        country = cc(country_code='')
        self.assertEqual(country.capital_city() == 'Not found', True)

    def test_very_long_code(self):
        country = cc(country_code='khjkgjfgfghhklkjlkljkhgjhffxdfxbvnbvj,khlij;'';kiuy98798hkjvgvhchhbkn,knlkkjhj')
        self.assertEqual(country.capital_city() == 'Not found', True)

    def test_with_wrong_url(self):
        country = cc(country_code='/an')
        self.assertEqual(country.capital_city() == 'Not found', True)





