import dataclasses
from typing import List

@dataclasses.dataclass
class CommercialProperty:
    """
    Represents a commercial property and its key investment metrics.
    """
    name: str
    price: float
    weekly_rental_income: float
    area_sqm: float
    capital_growth_pa: float  # As a percentage, e.g., 0.05 for 5%
    vacancy_rate_pa: float    # As a percentage, e.g., 0.03 for 3%
    location_score: float     # A score from 1 to 10

def calculate_value_score(property_data: CommercialProperty) -> float:
    """
    Calculates a "Value for Money" score for a single property.

    The formula uses a weighted sum of several normalized factors.
    Note: Normalization in this v0.1 is based on hardcoded expected values.
    A future version should normalize across the entire dataset.
    """
    # --- 1. Calculate intermediate metrics ---
    annual_rental_income = property_data.weekly_rental_income * 52

    # Avoid division by zero if price is not set
    if property_data.price == 0:
        return 0.0

    yield_pa = annual_rental_income / property_data.price
    price_per_sqm = property_data.price / property_data.area_sqm

    # --- 2. Normalize factors (v0.1 - based on assumptions) ---
    # These baseline values represent a "good" or "average" metric.
    # For Penrith, NSW commercial property.
    BASELINE_YIELD = 0.055  # 5.5%
    BASELINE_CAPITAL_GROWTH = 0.06 # 6%
    BASELINE_VACANCY_RATE = 0.03 # 3%
    BASELINE_LOCATION_SCORE = 10 # Max score
    BASELINE_PRICE_PER_SQM = 4000 # An estimated baseline for the area

    norm_yield = yield_pa / BASELINE_YIELD
    norm_capital_growth = property_data.capital_growth_pa / BASELINE_CAPITAL_GROWTH
    norm_vacancy_rate = property_data.vacancy_rate_pa / BASELINE_VACANCY_RATE
    norm_location_score = property_data.location_score / BASELINE_LOCATION_SCORE

    # For price, a lower value is better, so we want the ratio to be inverted.
    # A price_per_sqm equal to baseline gives a score of 1. Cheaper is > 1.
    norm_price_per_sqm = BASELINE_PRICE_PER_SQM / price_per_sqm

    # --- 3. Define weights for the formula ---
    weights = {
        "yield": 0.40,
        "capital_growth": 0.25,
        "vacancy_rate": -0.15,  # Negative weight as it's a penalty
        "location": 0.10,
        "price_per_sqm": 0.10, # A higher score (cheaper) is better
    }

    # --- 4. Calculate final score ---
    score = (
        (norm_yield * weights["yield"]) +
        (norm_capital_growth * weights["capital_growth"]) +
        (norm_vacancy_rate * weights["vacancy_rate"]) +
        (norm_location_score * weights["location"]) +
        (norm_price_per_sqm * weights["price_per_sqm"])
    )

    return score
