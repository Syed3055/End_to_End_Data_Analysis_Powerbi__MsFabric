
# 🚗BMW End-to-End Data Analysis (Microsoft Fabric)

--> **Workspace**: `End_TO_End_DataAnalysis`  
--> **Folder**: `BMW_Data`  
--> **Lakehouse**: `BMW_LH`  
--> **Schemas**: `BMW_data_bronze` ➜ `BMW_Silver`  
--> **Period Covered**: 2010–2024  
--> **Report**: Power BI — Pages: **Sales**, **Volume**, **Price (In Progress)**

---

## 📌 Overview
This project implements a full **lakehouse → notebook transformation → semantic/reporting** 
workflow in 
##### Microsoft Fabric for BMW car data (2010–2024). Raw files are staged in Files
##### Tables via Shortcuts for query performance and governance. 
##### A Fabric Notebook** performs cleansing, filtering, and enrichment to produce curated 
##### Silver** tables that power a **Power BI** report with Sales, Volume, and Price analysis.

---

## 🧱 Architecture & Flow
--> mermaid

flowchart LR
  subgraph Fabric Workspace: End_TO_End_DataAnalysis
  A[Files (Raw BMW CSV/Parquet)] -->|Shortcuts| B[(Lakehouse Tables - BMW_data_bronze)]
  ##### B --> C[Notebook: Transform & Enrich]
  ##### C --> D[(Lakehouse Tables - BMW_Silver)]
  ##### D --> E[[Power BI Dataset & Report]]
  --> end


### Key Components
- **Lakehouse**: `BMW_LH`
- **Bronze Schema**: `BMW_data_bronze` (ingested as-is via Shortcuts from Files)
- **Silver Schema**: `BMW_Silver` (clean + modeled output from notebook)
- **Notebook**: filters rows, standardizes types, and adds derived columns required by the report
- **Power BI Report**: three pages (Sales ✅, Volume ✅, Price 🚧)

---

## 📂 Project Structure
```
BMW/
├─ lakehouse/
│  ├─ Files/                  # Raw BMW files (2010–2024) uploaded to Fabric Files
│  └─ Tables/
│     ├─ BMW_data_bronze/     # Shortcut-backed tables from Files
│     └─ BMW_Silver/          # Curated, query-ready tables
├─ notebooks/
│  └─ 01_transform_bmw.ipynb  # Cleansing, filtering, enrichment ➜ writes to BMW_Silver
└─ reports/
   └─ BMW_Car_Sales.pbix      # Power BI report with Sales, Volume, Price pages
```

---

## 🔧 Ingestion & Modeling Details
**Ingestion**
- BMW data files are uploaded to **Files** in the `BMW_LH` lakehouse.
- **Shortcuts** are created from Files to **Tables** under the **`BMW_data_bronze`** schema to enable SQL access and downstream transformations.

**Transformations (Notebook)**
- Filters records to the 2010–2024 window
- Normalizes column types (dates, numeric measures)
- Adds required derived columns (e.g., `Year`, `Region`, price/volume standardization, and model groupings)
- Writes curated output to **`BMW_Silver`** schema



---

## 📊 Report Pages & Insights
Below are snapshots and highlights from the current report build. Replace image paths with your repo paths if needed (see **Images** section).

### 1) **Sales** (Completed)
<img width="1461" height="740" alt="image" src="https://github.com/user-attachments/assets/54b3520e-0e3a-419c-b6c3-d4f8fd289a3e" />

<img width="1438" height="747" alt="image" src="https://github.com/user-attachments/assets/576e215b-5d7b-4d17-9bad-8364e1940160" />



**KPIs**
- **Total Sales**: ~**19.01T**
- **Current Year Sales**: ~**1.31T**

**Visuals**
- **Sales by Model**: Consistently strong across `7 Series`, `3 Series`, `1.8`, `X1`, `5 Series`, `X3`, `M6`, `X6`, `M3` with values around **1.67T–1.97T** per model bar.
- **Total Sales by Region** (tabbed with Color/Region slicer): Region bars (e.g., **Asia ~3.23T**, Europe/North America/Middle East/South America/Africa ~3.1T–3.9T ranges as displayed).
- **Total Sales by Year**: Shows volatility with notable peaks around **2023 (~13.4bn)** and **2024 (~13.1bn)**.

**Filters**
- Slicers for **Car** (Model, Fuel_Type), **Features**, **Location**, and a year strip (2010–2024).

---

### 2) **Volume** (Completed)
<img width="1323" height="742" alt="image" src="https://github.com/user-attachments/assets/6f9a0df0-8b19-4c60-abc9-163025d0ab50" />


**KPIs**
- **Total Volume**: ~**253M**
- **Current Year Volume**: ~**18M**

**Visuals**
- #### Sales_Volume by Model**: Bars in the **23.0M–23.7M** range across major models.
- #### Volume by Color**/**Region** (tabbed): Colors like **Red, Silver, White, Grey, Blue, Black** each approx **41.7M–42.7M**.
- #### Sales_Volume by Year**: Fluctuation with highs around **2018–2019 (~17.0M)** and **2023 (~19.9M)**, rebound in **2024 (~17.5M)**.

---

### 3) **Price** (In Progress)
![Price Page](images/bmw_price_placeholder.png)

**Planned**
- KPIs: **Avg Price (All Time)**, **Current Year Avg Price**, **Median Price**
- Visuals: **Avg Price by Model**, **Avg Price by Year**, **Price Distribution (box/percentiles)**, **Price vs. Volume** scatter
- Slicers aligned with Sales/Volume pages (Year, Model, Fuel_Type, Region, Color)

**Suggested DAX for Price Page**
```DAX
Avg Price := AVERAGE('BMW_Silver'[Price])
CY Avg Price := CALCULATE([Avg Price], KEEPFILTERS('Calendar'[Year] = YEAR(TODAY())))
Median Price := MEDIAN('BMW_Silver'[Price])
Avg Price by Model := AVERAGEX(VALUES('BMW_Silver'[Model]), [Avg Price])
```

---

## 🧮 Sample DAX (Sales & Volume)
> Adjust column/table names to your actual Silver schema output.
```DAX
Total Sales := SUM('BMW_Silver'[SalesAmount])
Current Year Sales :=
  CALCULATE([Total Sales], KEEPFILTERS('Calendar'[Year] = YEAR(TODAY())))---Latest Year from data

Total Volume := SUM('BMW_Silver'[Units])
Current Year Volume :=
  CALCULATE([Total Volume], KEEPFILTERS('Calendar'[Year] = YEAR(TODAY())))

Sales by Year := SUMMARIZE('BMW_Silver', 'Calendar'[Year], "Sales", [Total Sales])
Volume by Year := SUMMARIZE('BMW_Silver', 'Calendar'[Year], "Volume", [Total Volume])
```

---

## 🛠️ How to Run (End-to-End)
1. **Data Upload**: Place BMW data files (2010–2024) in `BMW_LH > Files`.
2. **Create Shortcuts**: From Files to Tables under schema **`BMW_data_bronze`**.
3. **Notebook**: Run `01_transform_bmw.ipynb` to build curated tables in **`BMW_Silver`**.
4. **Power BI Desktop**: Connect to `BMW_LH` (SQL endpoint) and import **`BMW_Silver`** tables.
5. **Modeling**: Add a **Calendar** table, relationships, and DAX measures (see above).
6. **Report**: Build/refresh **Sales** and **Volume** pages. Complete the **Price** page using planned visuals/measures.
7. **Publish**: Publish the PBIX to Fabric and set scheduled refresh as needed.

---

## ✅ Data Quality & Governance Checks
- **Schema Validation**: Ensure expected columns (`Date`, `Model`, `Region`, `Color`, `Fuel_Type`, `Units`, `Price`, `SalesAmount`) exist and types are correct.
- **Deduplication**: Remove duplicates on (`Date`,`Model`,`Region`,`Color`,`VIN?`) as applicable.
- **Outliers**: Winsorize or flag extreme `Price` and `Units` values.
- **Slowly Changing Dimensions**: If model names/segments change over time, maintain mapping.
- **Refresh Policy**: Re-run the notebook for late-arriving data; set Fabric refresh.

---

## 🖼️ Images


- `images/bmw_sales.png` — Sales page screenshot
- `images/bmw_volume.png` — Volume page screenshot
- `images/bmw_price_placeholder.png` — temporary placeholder (replace with final Price page when done)



---


--- Syed with Microsoft Fabric (Lakehouse, Notebooks, Power BI).

### Thank You ........💐💐

