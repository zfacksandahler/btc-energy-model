#!/usr/bin/env python3
"""
Data ingestion script for Bitcoin energy model.
Loads hashrate data from CSV file and returns structured data.
"""

import csv
from typing import List, Dict


def load_hashrate_data(filepath: str) -> List[Dict[str, float]]:
    """
    Load hashrate data from CSV file.
    
    Expected CSV format:
        year,avg_hashrate_PHs
        2016,1.2
        2017,3.4
        ...
    
    Returns:
        List of dictionaries with keys 'year' and 'avg_hashrate_PHs'.
    """
    data = []
    try:
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert numeric fields
                year = int(row['year'])
                hashrate = float(row['avg_hashrate_PHs'])
                data.append({'year': year, 'avg_hashrate_PHs': hashrate})
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
    except KeyError as e:
        print(f"Error: Missing expected column {e} in CSV.")
    except ValueError as e:
        print(f"Error: Data conversion issue: {e}")
    
    return data


if __name__ == "__main__":
    # Example usage
    sample_data = load_hashrate_data("hashrate_data.csv")
    print(f"Loaded {len(sample_data)} records")
    for record in sample_data:
        print(f"Year: {record['year']}, Hashrate: {record['avg_hashrate_PHs']} PH/s")
