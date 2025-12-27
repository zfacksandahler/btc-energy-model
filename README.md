# Bitcoin Energy Impact Model

A reproducible research project modeling Bitcoin's annual electricity consumption based on historical hashrate data and hardware efficiency assumptions.

## Overview

This repository contains a simple, well-documented model for estimating Bitcoin's annual electricity consumption. The model uses historical network hashrate data and a set of clearly stated assumptions about the efficiency of mining hardware over time.

## Project Structure

- `ingest_data.py` – Python script to load hashrate data from CSV.
- `hashrate_data.csv` – Sample historical Bitcoin network hashrate (2016–2023).
- `calculate_energy.py` – Core calculation logic for estimating annual electricity consumption.
- `PROJECT_CHARTER.md` – Project charter, assumptions, and task breakdown.

## Assumptions

1. **Hashrate Data**: Historical average network hashrate in petahashes per second (PH/s) for each year.
2. **Hardware Efficiency**: Linear improvement from 50 J/TH in 2016 to 30 J/TH in 2020, constant thereafter.
3. **Operational Hours**: 24/7 operation (8760 hours per year).
4. **Energy Conversion**: 1 kWh = 3.6×10⁶ Joules.

## Usage

1. Install Python 3.x (no external dependencies required).
2. Place your hashrate data in `hashrate_data.csv` (format: `year,avg_hashrate_PHs`).
3. Run the ingestion script to verify data loading:

   ```bash
   python ingest_data.py
   ```

4. Run the energy calculation:

   ```bash
   python calculate_energy.py
   ```

   This will output annual electricity consumption in TWh for each year.

## Example Output

The model will produce a table like:

```
Year  Hashrate (PH/s)  Efficiency (J/TH)  Energy (TWh)
2016  1.2              50.0               0.58
2017  3.4              45.0               1.49
...
```

## License

MIT License – see LICENSE file.

## Acknowledgements

Developed as part of a reproducible research workflow demonstration at the University of Hawaiʻi at Mānoa.