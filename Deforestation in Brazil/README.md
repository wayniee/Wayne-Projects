# Deforestation in Brazil — Trends, Drivers & Soybean Linkages

*Visual analytics of global deforestation trends with a deep dive on Brazil and the role of soybean production.*

[![R](https://img.shields.io/badge/R-4.x-blue)]()
[![tidyverse](https://img.shields.io/badge/tidyverse-yes-brightgreen)]()

---

## Overview
In this project, we explore **who drives global deforestation**, **how Brazil’s drivers evolved (2001–2013)**, and **whether soybean production correlates with forest loss**. The analysis uses open datasets from *Our World in Data* and follows the workflow described in the project report. :contentReference[oaicite:0]{index=0}

**Core questions**
1. Which countries contributed most to net forest change over time?  
2. Within Brazil, which **activities** (e.g., pasture, crops) drove forest loss?  
3. Do **soybean production trends** align with deforestation patterns?

---

## Data Sources
- **`forest.csv`** — Net change in forest area by country.  
- **`brazil_loss.csv`** — Brazil’s forest loss by **driver**.  
- **`soybean_use.csv`** — Country-level soybean production & allocation.  
(Downloaded via the TidyTuesday repository referenced in the report.) 

---

## Methods & Visualisations

### 1) Faceted Diverging Bars — *Top Re/Deforestation Countries*
- Filter the **top 5** countries by **positive** (reforestation) and **negative** (deforestation) net change, plus **World** totals, across years (1990/2000/2010/2015).  
- Visual: **facet-wrapped diverging bar chart** (green = reforestation, red = deforestation).  
- Purpose: quick identification of leading contributors and how ranks change over time. 

### 2) Stacked Area — *Brazil’s Deforestation Drivers (2001–2013)*
- Reshape driver columns (e.g., **pasture**, **commercial crops**, **logging**, **roads**, **dams**, **fire**) into long format; plot stacked areas in **million hectares**.  
- Purpose: show **relative and absolute** contributions by different activity over time.  
- Styling: minimal theme, viridis palette, ordered legend. 

### 3) Choropleth + Time Series — *Soybean & Deforestation Context*
- **Map (1990)**: world soybean production intensity; label **top 5 producers**.  
- **Time series (1990–2013)**: soybean production trajectories for those producers.  
- Examines alignment between **production leaders** and **deforestation contributors**. 

---

## Key Findings (from the report)
- **Brazil** is consistently the **largest net deforester** across the studied years, while **China** and **India** frequently lead **reforestation**.  
- In **Brazil**, **pasture expansion** dominates forest loss and peaks around **2004**, then declines amid policy interventions.  
- **Soybean**: Brazil and Argentina are simultaneously **top producers** and **major deforesters**; **China** becomes a top producer/processor yet leads **reforestation**, consistent with importing raw soybeans rather than expanding domestic cropland.  
- Global deforestation declines after 1990, but the **2000–2015** period is relatively **flat**, suggesting a **wider dispersion** of contributing countries.

> Interpretation note: Apparent tension between rising soybean output and falling deforestation can reflect **productivity gains** (more output per land) and **other dominant drivers** (e.g., pasture) in specific regions. 

---

