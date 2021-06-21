import unittest
from partner import Customer, ServiceProvider
from helper_country import HelperCountry

class TestInvoice(unittest.TestCase):
    def test_local_country(self):
        service_provider = ServiceProvider(is_vat_payer=True, country=HelperCountry.LITHUANIA)
        customer = Customer(is_vat_payer=False, country=HelperCountry.LITHUANIA, legal_entity=False)

        invoice = service_provider.issue_invoice(customer=customer, service_amount=15.2)
        tax = round(HelperCountry.get_country_data(HelperCountry.LITHUANIA).get('vat') / 100 * 15.2, 2)
        self.assertAlmostEqual(invoice.vat, tax)
        self.assertAlmostEqual(invoice.total, 15.2 + tax)

    def test_non_eu(self):
        service_provider = ServiceProvider(is_vat_payer=True, country=HelperCountry.LITHUANIA)
        customer = Customer(is_vat_payer=False, country=HelperCountry.USA, legal_entity=False)

        invoice = service_provider.issue_invoice(customer=customer, service_amount=15.2)
        self.assertAlmostEqual(invoice.total, 15.2)
        self.assertAlmostEqual(invoice.vat, 0)

    def test_foreign_eu_country(self):
        service_provider = ServiceProvider(is_vat_payer=True, country=HelperCountry.LITHUANIA)
        customer = Customer(is_vat_payer=False, country=HelperCountry.LATVIA, legal_entity=False)

        invoice = service_provider.issue_invoice(customer=customer, service_amount=15.2)
        tax = round(HelperCountry.get_country_data(HelperCountry.LATVIA).get('vat') / 100 * 15.2, 2)
        self.assertAlmostEqual(invoice.vat, tax)
        self.assertAlmostEqual(invoice.total, 15.2 + tax)

    def test_provider_not_vat_payer(self):
        service_provider = ServiceProvider(is_vat_payer=False, country=HelperCountry.LITHUANIA)
        customer = Customer(is_vat_payer=False, country=HelperCountry.LITHUANIA, legal_entity=False)

        invoice = service_provider.issue_invoice(customer=customer, service_amount=15.2)
        self.assertAlmostEqual(invoice.vat, 0)
        self.assertAlmostEqual(invoice.total, 15.2)
    
    def test_types(self):
        service_provider = ServiceProvider(is_vat_payer=True, country=HelperCountry.LITHUANIA)
        customer = Customer(is_vat_payer=False, country=HelperCountry.LATVIA, legal_entity=False)
        self.assertRaises(TypeError, service_provider.issue_invoice, {"name": "Cust0m3r"}, 50)
        self.assertRaises(TypeError, service_provider.issue_invoice, customer, "42")
    
    def test_values(self):
        service_provider = ServiceProvider(is_vat_payer=True, country=HelperCountry.LITHUANIA)
        customer = Customer(is_vat_payer=False, country=HelperCountry.LATVIA, legal_entity=False)
        self.assertRaises(ValueError, service_provider.issue_invoice, customer, -42)
