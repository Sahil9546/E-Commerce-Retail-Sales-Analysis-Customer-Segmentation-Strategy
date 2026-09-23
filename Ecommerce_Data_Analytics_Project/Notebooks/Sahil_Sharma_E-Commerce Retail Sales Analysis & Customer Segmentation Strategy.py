import datetime as dt
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def main():
    print("=== Step 1: Loading Dataset ===")
    # Handles execution whether run from the project root or inside Notebooks/
    data_path = (
        "../Data/OnlineRetail.csv"
        if os.path.exists("../Data/OnlineRetail.csv")
        else "Data/OnlineRetail.csv"
    )

    df = pd.read_csv(data_path, encoding="ISO-8859-1")
    print(f"Raw dataset loaded. Total rows: {len(df)}")

    print("\n=== Step 2: Data Cleaning & Preprocessing ===")
    df = df.dropna(subset=["CustomerID"])
    df["CustomerID"] = df["CustomerID"].astype(int)
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

    # Feature engineering
    df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["InvoiceMonth"] = df["InvoiceDate"].dt.to_period("M")
    print(f"Cleaned dataset. Active valid rows: {len(df)}")

    print("\n=== Step 3: Performing RFM Segmentation ===")
    snapshot_date = df["InvoiceDate"].max() + dt.timedelta(days=1)

    rfm = (
        df.groupby("CustomerID")
        .agg(
            {
                "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
                "InvoiceNo": "nunique",
                "TotalAmount": "sum",
            }
        )
        .rename(
            columns={
                "InvoiceDate": "Recency",
                "InvoiceNo": "Frequency",
                "TotalAmount": "Monetary",
            }
        )
    )

    # Calculate RFM quantile scores safely using rank to handle duplicate values
    rfm["R_Score"] = pd.qcut(
        rfm["Recency"].rank(method="first"), 3, labels=[3, 2, 1]
    )
    rfm["F_Score"] = pd.qcut(
        rfm["Frequency"].rank(method="first"), 3, labels=[1, 2, 3]
    )
    rfm["M_Score"] = pd.qcut(
        rfm["Monetary"].rank(method="first"), 3, labels=[1, 2, 3]
    )

    rfm["RFM_Score"] = (
        rfm["R_Score"].astype(str)
        + rfm["F_Score"].astype(str)
        + rfm["M_Score"].astype(str)
    )

    # Export output datasets
    clean_out = (
        "../Data/Cleaned_Online_Retail.csv"
        if os.path.exists("../Data")
        else "Data/Cleaned_Online_Retail.csv"
    )
    rfm_out = (
        "../Data/RFM_Segmentation_Results.csv"
        if os.path.exists("../Data")
        else "Data/RFM_Segmentation_Results.csv"
    )

    df.to_csv(clean_out, index=False)
    rfm.to_csv(rfm_out)
    print(f"Cleaned data saved to {clean_out}")
    print(f"RFM segmentation results saved to {rfm_out}")

    print("\n=== Step 4: Generating Visualizations ===")
    sns.set_theme(style="whitegrid")

    # Chart 1: Monthly Revenue Trend
    monthly_revenue = (
        df.groupby("InvoiceMonth")["TotalAmount"].sum().reset_index()
    )
    monthly_revenue["InvoiceMonth"] = monthly_revenue["InvoiceMonth"].astype(
        str
    )

    plt.figure(figsize=(10, 5))
    sns.lineplot(
        data=monthly_revenue,
        x="InvoiceMonth",
        y="TotalAmount",
        marker="o",
        color="navy",
    )
    plt.title("Monthly Revenue Performance Trend")
    plt.xticks(rotation=45)
    plt.ylabel("Revenue ($)")
    plt.tight_layout()
    plt.savefig("monthly_revenue_trend.png")
    plt.close()

    # Chart 2: Top 10 Best Sellers
    top_products = (
        df.groupby("Description")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    plt.figure(figsize=(10, 5))
    sns.barplot(
        data=top_products, y="Description", x="TotalAmount", palette="Blues_r"
    )
    plt.title("Top 10 Products by Total Generated Revenue")
    plt.xlabel("Total Revenue ($)")
    plt.tight_layout()
    plt.savefig("top_10_products.png")
    plt.close()

    print("Charts saved: 'monthly_revenue_trend.png' & 'top_10_products.png'")
    print("\n=== Execution Complete! ===")


if __name__ == "__main__":
    main()