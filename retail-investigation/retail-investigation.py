import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import polars as pl

df = pl.read_csv("./retail-investigation/retail_sales_1M_dataset.csv")

def humanReadable(n, decimals=1):
    abs_n = abs(n)
    if abs_n >= 1e12:
        value, suffix = n / 1e12, " trillion"
    elif abs_n >= 1e9:
        value, suffix = n / 1e9, " billion"
    elif abs_n >= 1e6:
        value, suffix = n / 1e6, " million"
    elif abs_n >= 1e3:
        value, suffix = n / 1e3, " thousand"
    else:
        return str(int(n) if float(n).is_integer() else str(n))

    formatted = f"{value:.{decimals}f}"
    if "." in formatted:
        formatted = formatted.rstrip("0").rstrip(".")
    return f"{formatted}{suffix}"

def getInfo(df: pl.DataFrame):
    print(df.head())
    print(df.describe())

# getInfo(df)



def totalRevenue(df: pl.DataFrame):
    totalRevenue: float = df["price"].sum()
    print(humanReadable(totalRevenue))

def totalRevenueItems(df: pl.DataFrame):
    revenueByItem: pl.DataFrame = df.group_by("product").agg(pl.col("price").sum()).sort("price")

    fig, ax = plt.subplots()
    ax.bar(revenueByItem["product"], revenueByItem["price"])
    ax.set_xlabel("Items")
    ax.set_ylabel("Price Million")
    fig.set_figwidth(15)

    # force y ticks to not be integers
    ax.yaxis.set_major_locator(MaxNLocator(integer=False))

    plt.show()

def totalRevenueCategorys(df: pl.DataFrame):
    revenueByItem: pl.DataFrame = df.group_by("category").agg(pl.col("price").sum()).sort("price")

    fig, ax = plt.subplots()
    ax.bar(revenueByItem["category"], revenueByItem["price"])
    ax.set_xlabel("Category")
    ax.set_ylabel("Price 10 Million")
    fig.set_figwidth(15)

    # force y ticks to not be integers
    ax.yaxis.set_major_locator(MaxNLocator(integer=False))

    plt.show()

totalRevenue(df)
totalRevenueItems(df)
totalRevenueCategorys(df)