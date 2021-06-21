import unittest
from partner import Customer, ServiceProvider
from helper_country import HelperCountry


class TestPartner(unittest.TestCase):
    def test_values(self):
        self.assertRaises(ValueError, ServiceProvider, is_vat_payer=True, country="Mažeikiai")
    
    def test_types(self):
        self.assertRaises(TypeError, ServiceProvider, is_vat_payer="Taip", country=HelperCountry.USA)
        self.assertRaises(TypeError, Customer, is_vat_payer=True, country=HelperCountry.USA, legal_entity="Advokatas")
