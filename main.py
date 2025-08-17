from property_analyzer.algorithm import calculate_value_score
from property_analyzer.data import sample_properties

def main():
    """
    Main function to run the property analysis.
    It calculates the value score for each sample property and prints a ranked list.
    """
    print("--- Commercial Property Value Analysis ---")
    print(f"Analyzing {len(sample_properties)} properties in the Penrith, NSW area...")

    results = []
    for prop in sample_properties:
        score = calculate_value_score(prop)
        results.append({"property_name": prop.name, "score": score})

    # Sort the results by score in descending order (higher is better)
    sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)

    print("\n--- Analysis Results (Ranked by Value Score) ---")
    for i, result in enumerate(sorted_results, 1):
        print(f"{i}. {result['property_name']}")
        print(f"   Value Score: {result['score']:.4f}\n")

    print("--- End of Analysis ---")

if __name__ == "__main__":
    main()
