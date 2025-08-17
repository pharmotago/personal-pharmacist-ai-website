from .algorithm import CommercialProperty

# A list of fictional commercial properties for the Penrith, NSW area.
# This data is used to test and validate the scoring algorithm.
sample_properties = [
    CommercialProperty(
        name="123 High Street, Penrith NSW 2750",
        price=2_500_000,
        weekly_rental_income=2800,  # Yield ~5.8%
        area_sqm=400,               # Price/sqm = 6250
        capital_growth_pa=0.07,     # 7%
        vacancy_rate_pa=0.02,       # 2%
        location_score=9.5,
    ),
    CommercialProperty(
        name="15 Industrial Drive, Jamisontown NSW 2750",
        price=1_800_000,
        weekly_rental_income=2000,  # Yield ~5.7%
        area_sqm=1000,              # Price/sqm = 1800
        capital_growth_pa=0.05,     # 5%
        vacancy_rate_pa=0.04,       # 4%
        location_score=6.0,
    ),
    CommercialProperty(
        name="Suite 5, 45 King Street, Penrith NSW 2750",
        price=950_000,
        weekly_rental_income=800,   # Yield ~4.4%
        area_sqm=300,               # Price/sqm = 3166
        capital_growth_pa=0.04,     # 4%
        vacancy_rate_pa=0.10,       # 10%
        location_score=7.0,
    ),
    CommercialProperty(
        name="22 Queen Street, St Marys NSW 2760",
        price=1_500_000,
        weekly_rental_income=1600,  # Yield ~5.5%
        area_sqm=500,               # Price/sqm = 3000
        capital_growth_pa=0.055,    # 5.5%
        vacancy_rate_pa=0.03,       # 3%
        location_score=7.5,
    ),
]
