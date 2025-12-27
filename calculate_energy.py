#!/usr/bin/env python3
"""
Core calculation logic for Bitcoin energy consumption model.
Uses hashrate data and hardware efficiency assumptions to estimate
annual electricity consumption.
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


def efficiency_j_per_th(year: int) -> float:
    """
    Return mining hardware efficiency (J/TH) for a given year.
    
    Assumption: linear improvement from 50 J/TH in 2016 to 30 J/TH in 2020,
    constant at 30 J/TH after 2020.
    """
    if year <= 2016:
        return 50.0
    elif year >= 2020:
        return 30.0
    else:
        # linear interpolation between 2016 and 2020
        slope = (30.0 - 50.0) / (2020 - 2016)  # -5 J/TH per year
        return 50.0 + slope * (year - 2016)


def calculate_energy_twh(hashrate_ph: float, efficiency_j_per_th: float,
                         hours_per_year: float = 8760.0) -> float:
    """
    Calculate annual electricity consumption in TWh.
    
    Formula:
        energy_J = hashrate_PH * 1e12 (to TH/s) * efficiency_J_per_TH * hours_per_year * 3600 (s/hour)
        energy_TWh = energy_J / 3.6e15
    
    Simplified:
        energy_TWh = hashrate_PH * efficiency_J_per_TH * hours_per_year * 1e12 * 3600 / 3.6e15
                   = hashrate_PH * efficiency_J_per_TH * hours_per_year * 1e-3
    
    Because 1e12 * 3600 / 3.6e15 = 1e-3.
    
    Args:
        hashrate_ph: Average hashrate in PH/s.
        efficiency_j_per_th: Hardware efficiency in J/TH.
        hours_per_year: Operational hours per year (default 8760).
    
    Returns:
        Annual electricity consumption in TWh.
    """
    # Convert PH to TH: multiply by 1e12 (since 1 PH = 1000 TH? Wait: 1 PH = 10^15 H/s, 1 TH = 10^12 H/s. Actually 1 PH = 1000 TH.
    # Let's be careful: 1 PH/s = 10^15 hashes/s. 1 TH/s = 10^12 hashes/s. So 1 PH/s = 1000 TH/s.
    # Therefore hashrate_PH * 1000 = hashrate_TH.
    # However earlier we assumed 1e12 conversion. Let's recalc.
    # Our formula: energy_J = hashrate_PH * 1e12 * efficiency_J_per_TH * hours_per_year * 3600.
    # Let's derive: hashrate_PH (PH/s) = hashrate_PH * 10^15 H/s.
    # Efficiency in J/TH = Joules per 10^12 hashes.
    # So energy per second = (hashrate_PH * 10^15 H/s) * (efficiency_J_per_TH / 10^12) = hashrate_PH * efficiency_J_per_TH * 10^3 J/s.
    # Wait that's correct: 10^15 / 10^12 = 10^3.
    # So energy per second (W) = hashrate_PH * efficiency_J_per_TH * 1000.
    # Then energy per year (J) = energy per second * seconds per year.
    # seconds per year = hours_per_year * 3600.
    # So energy_J = hashrate_PH * efficiency_J_per_TH * 1000 * hours_per_year * 3600.
    # Convert to TWh: 1 TWh = 3.6e15 J.
    # energy_TWh = energy_J / 3.6e15.
    # Simplify: energy_TWh = hashrate_PH * efficiency_J_per_TH * hours_per_year * 1000 * 3600 / 3.6e15.
    # 1000 * 3600 = 3.6e6, divided by 3.6e15 = 1e-9.
    # So energy_TWh = hashrate_PH * efficiency_J_per_TH * hours_per_year * 1e-9.
    # Let's use that.
    
    return hashrate_ph * efficiency_j_per_th * hours_per_year * 1e-9


def main():
    """Main execution: load data, compute energy, print results."""
    data = load_hashrate_data("hashrate_data.csv")
    if not data:
        print("No data loaded. Exiting.")
        return
    
    print("Bitcoin Energy Consumption Estimate")
    print("=" * 60)
    print(f"{'Year':<6} {'Hashrate (PH/s)':<16} {'Efficiency (J/TH)':<18} {'Energy (TWh)':<12}")
    print("-" * 60)
    
    total_energy_twh = 0.0
    for record in data:
        year = record['year']
        hashrate = record['avg_hashrate_PHs']
        eff = efficiency_j_per_th(year)
        energy = calculate_energy_twh(hashrate, eff)
        total_energy_twh += energy
        print(f"{year:<6} {hashrate:<16.1f} {eff:<18.1f} {energy:<12.3f}")
    
    print("-" * 60)
    print(f"Total energy consumption (sum over years): {total_energy_twh:.3f} TWh")
    print("\nNote: Assumptions: 24/7 operation, linear efficiency improvement 2016-2020.")
    

if __name__ == "__main__":
    main()