# Tests for the property valuation algorithm.
import unittest
from property_analyzer.algorithm import calculate_value_score, CommercialProperty

class TestAlgorithm(unittest.TestCase):
    def test_calculate_value_score_handles_zero_area(self):
        """
        Tests that the score calculation handles a property with zero area
        to prevent a ZeroDivisionError.
        """
        property_with_zero_area = CommercialProperty(
            name="Test Property with Zero Area",
            price=500_000,
            weekly_rental_income=500,
            area_sqm=0,  # This should cause a failure
            capital_growth_pa=0.05,
            vacancy_rate_pa=0.03,
            location_score=8,
        )
        # Expect 0.0 as a safe fallback score, and no exception.
        score = calculate_value_score(property_with_zero_area)
        self.assertEqual(score, 0.0)
