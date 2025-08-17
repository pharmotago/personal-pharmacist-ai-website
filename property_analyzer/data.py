from .algorithm import CommercialProperty

# A list of fictional commercial properties for the Penrith, NSW area.
# This data is used to test and validate the scoring algorithm and is structured
# to align with the API-driven CommercialProperty dataclass.
sample_properties = [
    CommercialProperty(
        id=2013949740,
        headline="High St Retail Gem with Great Exposure",
        url="https://www.commercialrealestate.com.au/property/123-high-street-penrith-nsw-2750-2013949740",
        address="123 High Street, Penrith NSW 2750",
        property_type="Retail",
        price=2_500_000,
        weekly_rental_income=2800,
        area_sqm=400,
        capital_growth_pa=0.07,
        vacancy_rate_pa=0.02,
        location_score=9.5,
    ),
    CommercialProperty(
        id=2015887891,
        headline="Modern Industrial Warehouse in Jamisontown",
        url="https://www.commercialrealestate.com.au/property/15-industrial-drive-jamisontown-nsw-2750-2015887891",
        address="15 Industrial Drive, Jamisontown NSW 2750",
        property_type="Industrial/Warehouse",
        price=1_800_000,
        weekly_rental_income=2000,
        area_sqm=1000,
        capital_growth_pa=0.05,
        vacancy_rate_pa=0.04,
        location_score=6.0,
    ),
    CommercialProperty(
        id=2014556789,
        headline="Office Space Opportunity with Fit-Out Potential",
        url="https://www.commercialrealestate.com.au/property/suite-5-45-king-street-penrith-nsw-2750-2014556789",
        address="Suite 5, 45 King Street, Penrith NSW 2750",
        property_type="Offices",
        price=950_000,
        weekly_rental_income=800,
        area_sqm=300,
        capital_growth_pa=0.04,
        vacancy_rate_pa=0.10,
        location_score=7.0,
    ),
    CommercialProperty(
        id=2017123456,
        headline="Solid Mixed-Use Building in St Marys",
        url="https://www.commercialrealestate.com.au/property/22-queen-street-st-marys-nsw-2760-2017123456",
        address="22 Queen Street, St Marys NSW 2760",
        property_type="Retail",
        price=1_500_000,
        weekly_rental_income=1600,
        area_sqm=500,
        capital_growth_pa=0.055,
        vacancy_rate_pa=0.03,
        location_score=7.5,
    ),
]
