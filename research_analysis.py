"""
Research Data Analyzer

Author: Dr. Mustafa Simsek
"""

data = [72, 85, 91, 78, 88]


def calculate_statistics(values):

    average = sum(values) / len(values)

    return {
        "average": average,
        "maximum": max(values),
        "minimum": min(values)
    }


if __name__ == "__main__":

    results = calculate_statistics(data)

    print("Average:", results["average"])
    print("Maximum:", results["maximum"])
    print("Minimum:", results["minimum"])
