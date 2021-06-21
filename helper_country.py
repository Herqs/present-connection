class HelperCountry:
    # Countries
    LITHUANIA = "Lithuania"
    LATVIA = "Latvia"
    POLAND = "Poland"
    RUSSIA = "Russia"
    TURKEY = "Turkey"
    USA = "USA"
    MEXICO = "Mexico"

    # Regions
    NORTH_AMERICA = "North America"
    EUROPE = "Europe"
    ASIA = "Asia"

    # Country Object dict
    _COUNTRY_DATA = {
        LITHUANIA: {
            "vat": 21,
            "region": EUROPE
        },
        LATVIA: {
            "vat": 18,
            "region": EUROPE
        },
        POLAND: {
            "vat": 42,
            "region": EUROPE
        },
        RUSSIA: {
            "vat": 69,
            "region": ASIA
        },
        TURKEY: {
            "vat": 2,
            "region": ASIA
        },
        USA: {
            "vat": 5,
            "region": NORTH_AMERICA
        },
        MEXICO: {
            "vat": 17,
            "region": NORTH_AMERICA
        },
    }

    @staticmethod
    def get_country_data(country):
        if not isinstance(country, str):
            raise TypeError("'get_country' method expected a string")
        country_data = HelperCountry._COUNTRY_DATA.get(country)
        if not country_data:
            raise ValueError(f"Country not found, available countries are: {', '.join(HelperCountry._COUNTRY_DATA.keys())}")
        return country_data

    @staticmethod
    def is_country_valid(country):
        return country in HelperCountry._COUNTRY_DATA.keys()