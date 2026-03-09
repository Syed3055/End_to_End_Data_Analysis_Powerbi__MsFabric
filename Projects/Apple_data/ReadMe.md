# 📊 Apple Sales Analysis Project (Microsoft Fabric + Power BI)
#### This project demonstrates a complete end‑to‑end data analytics pipeline built using Microsoft Fabric Lakehouse, Notebooks, and Power BI.
It includes data ingestion, transformation, modeling, and visualization of Apple Sales data.

## 🏗️ Project Architecture
#### Workspace: End_to_End_Data_Analysis
##### -->Folder: Apple (This README belongs ONLY to this folder)
##### This project uses a standard Lakehouse medallion architecture:

Bronze Layer → Raw CSV data
Silver Layer → Curated, cleaned, transformed data
Power BI Reports → Published dashboards connected through DirectQuery


## 📥 1. Data Ingestion (Bronze Layer)

Created Lakehouse: Apple_Data
Created project folder Apple inside workspace.
Uploaded raw CSV Apple dataset into:
Lakehouse → Files → Apple_data


#### Created schema:
apple_data_bronze


Pulled the raw CSV into bronze table using a shortcut.


## 🧹 2. Data Transformation (Silver Layer)
Using Fabric Notebook, the following tasks were completed:

Cleaning and removing invalid rows
Handling nulls
Fixing date formats
Standardizing column names
Adding new columns:

Month_Name
DayName
Quarter
Return_Status


Applying business rules
Saving curated output into:
apple_data_silver




## 📊 3. Power BI Report (DirectQuery)
Power BI Desktop connected to Lakehouse SQL Endpoint in DirectQuery mode.
Created 3 report pages:
### 🔹 Home Page
<img width="1320" height="733" alt="image" src="https://github.com/user-attachments/assets/850337f3-ad41-42b4-b236-f8cd0fd00424" />

<img width="1337" height="741" alt="image" src="https://github.com/user-attachments/assets/f12d58c9-5955-4d6a-8b0e-661d64462c76" />


### 🔹 Detail Page
<img width="1305" height="740" alt="image" src="https://github.com/user-attachments/assets/09cc804f-1de7-4020-a3ba-775884e8b6f5" />


### 🔹 About Apple Page
<img width="1302" height="732" alt="image" src="https://github.com/user-attachments/assets/58cffcf9-3a45-44d6-83f1-72952cd3a751" />


## 📈 4. Key Insights Delivered

Revenue trend across years, quarters & months
Orders by category (Mac, iPhone, iPad, Watch, Accessories…)
Payment method performance
Sales by Weekday pattern
Product-wise sales contribution (TreeMap)
Customer segment analysis (Business vs Education)
Month-on-month revenue comparison


## 🛠 Technologies Used

Microsoft Fabric Lakehouse
OneLake Shortcuts
Fabric Notebooks
Power BI Desktop
DirectQuery SQL Endpoint
GitHub for version control


## 📂 Folder Structure (Apple Folder Only)
Apple/
│
├── Raw_Data/             # -->CSV files

├── Notebooks/            # -->Data Prep Notebook(s)

├── Silver_Tables/        # -->Curated final tables

├── PowerBI_Report/       # -->PBIX and published reports

└── README.md             # -->This file
## ✔ Purpose of This Project
To demonstrate a complete end-to-end analytics pipeline in Microsoft Fabric using real-world Apple dataset and build enterprise-grade dashboards.
