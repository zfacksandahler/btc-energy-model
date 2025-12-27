# Project Charter: BTC Energy Impact Model

**Date:** December 2025  
**Repository:** `btc-energy-model`

## Objective

Create a reproducible research model for estimating Bitcoin's annual electricity consumption based on historical hashrate data and hardware efficiency assumptions.

## Core Assumptions

1. **Hashrate Data**: We will use historical average network hashrate in petahashes per second (PH/s) for each year from 2016 to 2023.
2. **Hardware Efficiency**: We assume a linear improvement in mining hardware efficiency from 50 J/TH (joules per terahash) in 2016 to 30 J/TH in 2020, and then constant at 30 J/TH beyond 2020.
3. **Annual Operational Hours**: We assume 24/7 operation (8760 hours per year) for all mining hardware.
4. **Energy Conversion**: 1 kWh = 3.6×10⁶ Joules.

## Required Components

- **Data Ingestion Script**: Load and parse CSV file containing `year` and `avg_hashrate_PHs` columns.
- **Calculation Logic**: Compute annual electricity consumption using formula:
  - Annual energy (J) = avg_hashrate_PHs × 10¹² (to TH/s) × efficiency_J_per_TH × hours_per_year
  - Convert to TWh: divide by 3.6×10¹⁵.
- **Output Visualization**: Generate simple plots of annual electricity consumption over time (optional but recommended).
- **Documentation**: README explaining model, assumptions, usage, and limitations.

## Deliverables

1. Python scripts for data ingestion and calculation.
2. Sample data file (`hashrate_data.csv`).
3. Documentation (README.md).
4. Example output (plots, CSV results).

## Task Breakdown

### Task 1: Create Data Ingestion Script
- **Status:** Completed
- **Description:** Write a Python script `ingest_data.py` that loads a CSV file with columns `year` and `avg_hashrate_PHs`. The script should handle missing files, column mismatches, and data conversion errors gracefully.
- **Associated File:** `ingest_data.py`

### Task 2: Develop Core Calculation Logic
- **Status:** Completed
- **Description:** Write a Python script `calculate_energy.py` that implements the energy consumption formula using the loaded hashrate data and the hardware efficiency assumptions. The script should output a table of annual electricity consumption in TWh.
- **Associated File:** `calculate_energy.py`

### Task 3: Write Documentation and README
- **Status:** Completed
- **Description:** Create a comprehensive `README.md` that explains the project's purpose, assumptions, how to run the model, and interpretation of results. Also include a project charter (this file) for traceability.
- **Associated File:** `README.md`, `PROJECT_CHARTER.md`

## Notes

This charter serves as the central planning document for the project. Each task is tracked as a sub‑issue (simulated in this file) and linked to the corresponding deliverables.

**Repository Link:** https://github.com/zfacksandahler/btc-energy-model