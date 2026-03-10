import pandas as pd
import matplotlib.pyplot as plt
import locale

df = pd.read_csv("./amazon-analysis/amazon_sales_dataset.csv")

def task1(df: pd.DataFrame):
    print(df.head())
    print(df.info())

# task1(df)

def task2(df: pd.DataFrame):
    total_sales = round(df["total_revenue"].sum(), 2)
    avg_sales = round(df["total_revenue"].mean(), 2)

    print(f"The total sales is £{total_sales:,} and the avearage revnue per oreder is £{avg_sales:,}")

# task2(df)

def task3(df: pd.DataFrame):
    total_sales = df.groupby("product_category")["total_revenue"].sum().sort_values(ascending=False)

    plt.bar(total_sales.index, total_sales)

    plt.xlabel("Product Category")
    plt.ylabel("Total Revenue £")

    plt.show()

# task3(df)

def task4(df: pd.DataFrame):
    total_sales_by_reigon = df.groupby("customer_region")["total_revenue"].sum().sort_values(ascending=False)

    plt.bar(total_sales_by_reigon.index, total_sales_by_reigon)

    plt.xlabel("Customer Reigon")
    plt.ylabel("Total Sales £")

    plt.show()

# task4(df)

def getAvgModifiers(df: pd.DataFrame):
    avg_discount = df["discount_percent"].mean()
    avg_payment = df.groupby("payment_method")["order_id"].count()
    avg_rating = df["rating"].mean()
    avg_reviews = df["review_count"].mean()

    print(f"the average discount is £{avg_discount} and the avg rating is {avg_rating} stars comapred to {avg_reviews} reviews.")

    # plt.pie(avg_payment, labels=avg_payment.index)
    # plt.show()

# getAvgModifiers(df)
