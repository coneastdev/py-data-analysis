import polars as pl
import matplotlib.pyplot as plt

dfSummer = pl.read_csv("./Olympics/SummerSD.csv")
dfWinter = pl.read_csv("./Olympics/WinterSD.csv")
dfCountries = pl.read_csv("./Olympics/CountriesSD.csv")

def medalsByPopAndGDP(dfWins: pl.DataFrame, dfCountries: pl.DataFrame):
    # get data
    wins: pl.Series = dfWins.group_by("Country").agg(pl.col("Medal").count()).sort(by="Medal", descending=True)
    #pop: pl.DataFrame

    print(wins.head())

    # plot
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    ax.scatter(wins, ys, zs)

    ax.set(xticklabels=[],
        yticklabels=[],
        zticklabels=[])

    plt.show()

def mainMenu(dfSummer: pl.DataFrame, dfWinter: pl.DataFrame, dfCountries: pl.DataFrame):
    print("Select Grapth\n1. Medals per population and GDP")

    inp = input("Enter option number $ ")

    if inp == "1":
        dfSummer = dfSummer.drop("Country")
        dfSummer = dfSummer.rename({"Code": "Country"})
        medalsByPopAndGDP(pl.concat([dfSummer, dfWinter]), dfCountries)
    
mainMenu(dfSummer, dfWinter, dfCountries)