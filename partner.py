from abc import ABC, abstractmethod
from helper_country import HelperCountry
from invoice import Invoice

class Partner(ABC):
    @abstractmethod
    def __init__(self, is_vat_payer, country):
        """
        Inits a Partner.
        Country must be a valid country from HelperCountry class.
        """
        if not isinstance(is_vat_payer, bool):
            raise TypeError("is_vat_payer must be a boolean")
        if not HelperCountry.is_country_valid(country):
            raise ValueError("Country is not valid")
        self.is_vat_payer = is_vat_payer
        self.country = country

class Customer(Partner):
    def __init__(self, is_vat_payer, country, legal_entity):
        super().__init__(is_vat_payer, country)
        if not isinstance(legal_entity, bool):
            raise TypeError("legal_entity must be a boolean")
        self.legal_entity = legal_entity

class ServiceProvider(Partner):
    def __init__(self, is_vat_payer, country):
        super().__init__(is_vat_payer, country)
        self.legal_entity = True
        self.issued_invoices = []

    def issue_invoice(self, customer, service_amount):
        invoice = Invoice(self, customer, service_amount)
        self.issued_invoices.append(invoice)
        return invoice
