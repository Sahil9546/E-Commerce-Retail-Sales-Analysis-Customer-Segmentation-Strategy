# Project Report: E-Commerce Retail Sales Analysis & Customer Segmentation

**Submitted by:** MCA Student  
**Course/Program:** Masterclass Data Science & Analytics Project  

---

### Executive Summary
Understanding transactional patterns and customer value tiers is essential for modern e-commerce growth. This project analyzes an online retail dataset containing transactional records to evaluate sales trends, product performance, and customer purchasing behaviors using RFM (Recency, Frequency, Monetary) modeling.

### 1. Introduction & Objectives
* Uncover temporal sales patterns and evaluate seasonality trends.
* Classify products by revenue contribution and order volume.
* Perform RFM segmentation to isolate high-value customers from churn-risk customers.
* Build an executive dashboard summarizing commercial KPIs.

### 2. Dataset Description
* **Source:** UCI Machine Learning / Kaggle Online Retail Dataset
* **Attributes:** InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

### 3. Data Cleaning & Preprocessing
1. **Filtering:** Removed null CustomerID records and non-commercial transactions (returns/cancellations).
2. **Feature Engineering:** Calculated TotalAmount = Quantity * UnitPrice.
3. **RFM Metrics:** Extracted purchase recency (days), invoice counts (frequency), and aggregate spend (monetary value) per customer.

### 4. Key Findings & Insights
* **Finding 1 (Seasonal Revenue Spike):** Sales peak dramatically in Q4 due to holiday spending.
* **Finding 2 (Geographic Concentration):** Over 80% of revenue originates from domestic orders.
* **Finding 3 (Pareto Distribution in Products):** Top 20% of stock codes account for majority of overall revenue.
* **Finding 4 (Customer Value Segmentation):** "High-Value Loyalists" (RFM Score 333) represent key core revenue.

### 5. Recommendations
1. Targeted Campaigns for At-Risk Customers
2. Q3 Inventory Preparation for peak season
3. VIP Loyalty Program for Top Customers

### 6. Tools Used
* **Programming Language:** Python 3.x (Pandas, NumPy, Matplotlib, Seaborn)
* **Environment:** Jupyter Notebook (.ipynb)
* **Visualization/Dashboard:** Power BI / Tableau / Matplotlib
