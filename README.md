# E-Commerce Retail Sales Analysis & Customer Segmentation Strategy

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Machine Learning](https://img.shields.io/badge/ML-K--Means%20Clustering-green)

## 📌 Executive Summary
This project analyzes over 500,000 transaction records from an online retail platform to optimize marketing strategies. By leveraging **RFM (Recency, Frequency, Monetary)** feature engineering and **K-Means Clustering**, customers are segmented into 4 actionable cohorts (Champions, Loyal Customers, At-Risk Spenders, and Dormant Buyers).

---

## 🛠️ Tech Stack & Methods
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (`KMeans`, `StandardScaler`)
* **Visualization:** Matplotlib, Seaborn
* **Segmentation Approach:** RFM Scoring + Log Transformation + Z-Score Scaling

---

## 📊 Key Findings & Cluster Segments
| Cluster | Segment | Recency | Frequency | Monetary | Strategy |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0** | **Champions** | ~15 days | High (12+ orders) | High ($3.5k+) | Loyalty Perks, Early Access |
| **1** | **Loyal Customers** | ~40 days | Moderate | Moderate | Cross-sell & Upsell |
| **2** | **At-Risk Spenders** | ~180 days | High (Past) | High (Past) | Targeted Win-Back Offers |
| **3** | **Dormant Buyers** | ~200+ days| Low (1-2 orders)| Low | Automated Low-cost Drips |

---

## 🚀 How to Run locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/E-Commerce-Retail-Sales-Analysis.git](https://github.com/YOUR_USERNAME/E-Commerce-Retail-Sales-Analysis.git)
   cd E-Commerce-Retail-Sales-Analysis
