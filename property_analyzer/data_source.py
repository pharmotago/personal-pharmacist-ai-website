import requests
from .config import DOMAIN_API_KEY
from .data import sample_properties
from .algorithm import CommercialProperty
from typing import List

def fetch_properties(suburb: str) -> List[CommercialProperty]:
    """
    Fetches commercial property listings for a given suburb.

    This function is designed to fetch data from the Domain API.
    For this MVP, it returns static sample data and simulates the API structure.
    """
    print(f"INFO: Using mock data for suburb: {suburb}. Real API call is not implemented.")

    # In a real implementation, this function would do the following:
    # 1. Define the API endpoint and headers
    # endpoint = "https://api.domain.com.au/v1/listings/commercial/_search"
    # headers = {"X-Api-Key": DOMAIN_API_KEY}

    # 2. Define the search query based on the suburb
    # query = {
    #     "searchMode": "forSale",
    #     "locations": [
    #         {
    #             "state": "NSW",
    #             "suburb": suburb,
    #             "includeSurroundingSuburbs": True
    #         }
    #     ]
    # }

    # 3. Make the HTTP request
    # try:
    #     response = requests.post(endpoint, json=query, headers=headers)
    #     response.raise_for_status()  # Raise an exception for bad status codes
    #     api_data = response.json()
    # except requests.exceptions.RequestException as e:
    #     print(f"ERROR: Could not fetch data from Domain API: {e}")
    #     return []

    # 4. Parse the response and map it to our CommercialProperty dataclass
    # properties = []
    # for listing in api_data:
    #     # ... mapping logic here ...
    #     # Note: The API does not provide all our required fields directly (e.g., rental income).
    #     # This would require additional logic, perhaps scraping the listing URL.
    #     prop = CommercialProperty(...)
    #     properties.append(prop)
    # return properties

    # For now, just return the static sample data
    return sample_properties
