import dataclasses
from typing import Optional

@dataclasses.dataclass
class CommercialProperty:
    """
    Represents a commercial property, aligned with fields available from the Domain API.
    Some fields are optional as they may not be present in all listings or require
    data from other API endpoints.
    """
    # Core fields from Domain API
    id: int
    headline: str
    url: str
    address: str
    property_type: str

    # Key metrics for our algorithm (may be missing from API)
    price: Optional[float] = None
    weekly_rental_income: Optional[float] = None
    area_sqm: Optional[float] = None
    capital_growth_pa: Optional[float] = None # e.g., 0.05 for 5%
    vacancy_rate_pa: Optional[float] = None   # e.g., 0.03 for 3%

    # Our internally-derived score
    location_score: Optional[float] = None    # A score from 1 to 10

def calculate_value_score(property_data: CommercialProperty) -> float:
    """
    Calculates a "Value for Money" score for a single property.
    This version is more robust and handles missing data gracefully.
    """
    # --- 1. Check for essential data ---
    # If price is missing, we cannot perform a meaningful analysis.
    if property_data.price is None or property_data.price == 0:
        return 0.0

    # --- 2. Calculate intermediate metrics, with fallbacks ---
    yield_pa = 0.0
    if property_data.weekly_rental_income is not None:
        annual_rental_income = property_data.weekly_rental_income * 52
        yield_pa = annual_rental_income / property_data.price

    price_per_sqm = float('inf') # Use infinity if area is unknown
    if property_data.area_sqm is not None and property_data.area_sqm > 0:
        price_per_sqm = property_data.price / property_data.area_sqm

    # --- 3. Normalize factors (v0.1 - based on assumptions) ---
    BASELINE_YIELD = 0.055
    BASELINE_CAPITAL_GROWTH = 0.06
    BASELINE_VACANCY_RATE = 0.03
    BASELINE_LOCATION_SCORE = 10
    BASELINE_PRICE_PER_SQM = 4000

    norm_yield = yield_pa / BASELINE_YIELD

    # Use a default of 1.0 (average) if data is missing
    norm_capital_growth = (property_data.capital_growth_pa / BASELINE_CAPITAL_GROWTH) if property_data.capital_growth_pa is not None else 1.0
    norm_vacancy_rate = (property_data.vacancy_rate_pa / BASELINE_VACANCY_RATE) if property_data.vacancy_rate_pa is not None else 1.0
    norm_location_score = (property_data.location_score / BASELINE_LOCATION_SCORE) if property_data.location_score is not None else 0.5 # Default to average if no score

    norm_price_per_sqm = BASELINE_PRICE_PER_SQM / price_per_sqm

    # --- 4. Define weights for the formula ---
    weights = {
        "yield": 0.40,
        "capital_growth": 0.25,
        "vacancy_rate": -0.15,
        "location": 0.10,
        "price_per_sqm": 0.10,
    }

    # --- 5. Calculate final score ---
    score = (
        (norm_yield * weights["yield"]) +
        (norm_capital_growth * weights["capital_growth"]) +
        (norm_vacancy_rate * weights["vacancy_rate"]) +
        (norm_location_score * weights["location"]) +
        (norm_price_per_sqm * weights["price_per_sqm"])
    )

    return score
