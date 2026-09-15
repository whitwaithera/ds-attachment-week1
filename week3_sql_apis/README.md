# Week 3: East African Economic Explorer (Real-World Project)

## Business Problem
I need to analyze macroeconomic trends — **GDP, Population, and Inflation** — for three East African countries (**Kenya, Rwanda, and Tanzania**) from 2000 to 2022. The goal is to collect this data from the World Bank API, clean it, load it into a local SQLite database, and run analytical SQL queries to uncover regional development patterns.

## Data Source
- **API:** World Bank Open Data API
- **Countries:** Kenya (KEN), Rwanda (RWA), Tanzania (TZA)
- **Indicators:**
  - `NY.GDP.MKTP.CD` — GDP (current US$)
  - `SP.POP.TOTL` — Total Population
  - `FP.CPI.TOTL.ZG` — Inflation, consumer prices (annual %)
- **Time Range:** 2000 – 2022

## Methodology
1. **Data Collection:** Used Python's `requests` library to fetch JSON data from the World Bank API.
2. **Data Cleaning:** Flattened nested JSON into a Pandas DataFrame, dropped missing values, and removed duplicates.
3. **Database Design:** Normalized into three SQLite tables — `Countries`, `Indicators`, `EconomicData`.
4. **SQL Analysis:** Used JOINs, GROUP BY, aggregate functions, and subqueries to answer business questions.

## Key SQL Findings
- See `week3_economic_explorer.ipynb` for full queries and outputs.
- **Example insights:**
  - Kenya has the largest GDP in absolute terms, followed by Tanzania and Rwanda.
  - Rwanda shows the highest average inflation rate of the three nations.
  - Tanzania has the fastest population growth rate between 2000 and 2022.

## Project Structure