from property_analyzer.algorithm import calculate_value_score
from property_analyzer.data_source import fetch_properties

def main():
    """
    Main function to run the property analysis.
    It fetches property data and prints a ranked list based on value score.
    """
    TARGET_SUBURB = "Penrith"

    print("--- Commercial Property Value Analysis ---")
    print(f"Fetching properties for {TARGET_SUBURB}, NSW...")

    # Fetch properties from the data source
    properties_to_analyze = fetch_properties(suburb=TARGET_SUBURB)

    if not properties_to_analyze:
        print("No properties found to analyze. Exiting.")
        return

    print(f"Analyzing {len(properties_to_analyze)} properties...")

    results = []
    for prop in properties_to_analyze:
        score = calculate_value_score(prop)
        results.append({"property_name": prop.headline, "score": score})

    # Sort the results by score in descending order (higher is better)
    sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)

    print("\n--- Analysis Results (Ranked by Value Score) ---")
    for i, result in enumerate(sorted_results, 1):
        print(f"{i}. {result['property_name']}")
        print(f"   Value Score: {result['score']:.4f}\n")

    print("--- End of Analysis ---")

if __name__ == "__main__":
    main()
