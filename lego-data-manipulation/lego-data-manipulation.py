import polars as pl
import matplotlib.pyplot as plt
import numpy as np

df = pl.read_csv("./lego-data-manipulation/lego_sets.csv")

def getInfo(df: pl.DataFrame):
    print(df.head())
    print(df.describe())
    print(f"length: {len(df)}")

# getInfo(df)

def histPrice(df: pl.DataFrame):
    prices = df["list_price"]

    plt.hist(prices)

    plt.xlabel("listing price")
    plt.ylabel("lego sets")

    plt.title("Histogram of Lego Set Prices")

    plt.show()


# histPrice(df)

def scaterPrice(df: pl.DataFrame):
    prices = df["list_price"]
    pieceCount = df["piece_count"]

    z = np.polyfit(pieceCount, prices, 1)
    p = np.poly1d(z)

    plt.scatter(pieceCount, prices)

    plt.xlabel("piece count")
    plt.ylabel("listing price")

    plt.plot(pieceCount, p(pieceCount), "r--")

    plt.title("Scatter Graph of Lego Set Prices To Piece Count")

    plt.show()

# scaterPrice(df)

def topTenSetThemes(df: pl.DataFrame):
    combinedByThemes = df.group_by("theme_name").agg(pl.col("play_star_rating").mean() + pl.col("star_rating").mean() + pl.col("val_star_rating").mean())

    combinedByThemes = combinedByThemes.sort("play_star_rating", nulls_last=True, descending=True)

    combinedByThemes = combinedByThemes.with_columns(
        pl.col("play_star_rating").round(1)
    )

    combinedByThemes = combinedByThemes.drop_nulls()

    combinedByThemes = combinedByThemes.with_columns(
        pl.when(pl.col("theme_name").str.len_chars() > 12)
        .then(pl.col("theme_name").str.slice(0, 12) + "...")
        .otherwise(pl.col("theme_name"))
        .alias("theme_name")
    )

    print(combinedByThemes.head(10))

    plt.xlabel("Theme Names")
    plt.ylabel("Average Ratings Out Of 15")

    plt.bar(combinedByThemes["theme_name"].head(10), combinedByThemes["play_star_rating"].head(10), width=0.5)

    plt.show()

# topTenSetThemes(df)