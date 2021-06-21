from datetime import datetime
from helper_country import HelperCountry


class Invoice():
    def __init__(self, service_provider, customer, service_amount):
        self.service_provider = service_provider
        self.customer = customer

        if not isinstance(service_amount, (int, float)):
            raise TypeError("Amount must be a number")
        if service_amount < 0:
            raise ValueError("Amount cannot be negative")
        self.service_amount = service_amount
        self.calculate_and_set_vat_and_subtotal()
        self.created_at = datetime.now()

    def calculate_and_set_vat_and_subtotal(self):
        customer_country_data = HelperCountry.get_country_data(self.customer.country)

        if (
            not self.service_provider.is_vat_payer or
            customer_country_data.get('region') != HelperCountry.EUROPE or
            self.customer.is_vat_payer and self.customer.country != self.service_provider.country
        ):
            self.vat = 0
        else:
            self.vat = round(self.service_amount * customer_country_data.get('vat') / 100, 2)

        self.total = self.service_amount + self.vat
