import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./pixelvault/pixelvault_game_sales.csv")

def getInfo(df: pd.DataFrame):
    print(df.head(), df.head(-5), df.info(), df.describe(), df["sale_date"].max(), df["sale_date"].min())

# getInfo(df)

def checkDataQuality(df: pd.DataFrame):
    dropedNa = df.dropna()

    combinedDf = df.groupby(["sale_id"])

    print(f"their are {len(df) - len(dropedNa)} null values and {len(df) - len(combinedDf)} duplicate values.")

# checkDataQuality(df)

def insights(df: pd.DataFrame):
    gamePopularity: pd.Series = df["game_title"].value_counts().sort_values(axis=0, ascending=False).head(5)
    print(gamePopularity)

    plt.pie(gamePopularity, labels=gamePopularity.index)
    plt.show()

    salesByCategory = df.groupby("category")["total_sale"].sum().sort_values(axis=0, ascending=False)
    print(salesByCategory.head())

    highstSingleSales = df.sort_values(by=["total_sale"], ascending=False)
    print(highstSingleSales.head())

    averagePrice = round(df["price"].mean(), 2)
    print(f"the average price is £{averagePrice}")

insights(df)