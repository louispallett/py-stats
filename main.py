import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

# style.use("dark_background")

df = pd.read_csv("smoking.csv")
smokers = df.loc[(df["smoke"] == "Yes")]
non_smokers = df.loc[(df["smoke"] == "No")]

smokers.to_csv("smokers.csv", index=False)
non_smokers.to_csv("non-smokers.csv", index=False)

def chartByGender():
    smokersF = smokers.loc[(df["gender"] == "Female")]
    smokersM = smokers.loc[(df["gender"] == "Male")]

    non_smokersF = non_smokers.loc[(df["gender"] == "Female")]
    non_smokersM = non_smokers.loc[(df["gender"] == "Male")]

    fig, axs = plt.subplots(1, 3)

    axs[0].pie([len(smokers), len(non_smokers)], labels=["Smokers", "Non-Smokers"], 
               explode=[0, 0.2], autopct="%.1f%%", pctdistance=0.5, textprops={"fontsize": 7.5})
    axs[0].set_title("Smoking Habits")

    axs[1].pie([len(smokersF), len(smokersM)], labels=["Female", "Male"],
               autopct="%.1f%%", pctdistance=0.5, textprops={"fontsize": 7.5})
    axs[1].set_title("Smokers")

    axs[2].pie([len(non_smokersF), len(non_smokersM)], labels=["Female", "Male"],
               autopct="%.1f%%", pctdistance=0.5, textprops={"fontsize": 7.5})
    axs[2].set_title("Non-Smokers")

    fig.suptitle("Population by Gender", fontsize=30, fontname="Carlito")
    plt.tight_layout()
    plt.savefig("gender.png", dpi=300, bbox_inches="tight")

def chartQualifications():
    # Remove any missing data
    df = pd.read_csv("smokers.csv")
    qual = df.dropna(subset=["highest_qualification"])


    qualifications = ["No Qualification", "Degree", "GCSE", "Higher/Sub Degree", "ONC/BTEC", "A Levels", "Other"]
    none = qual.loc[(df["highest_qualification"] == "No Qualification")]
    degree = qual.loc[(df["highest_qualification"] == "Degree")]
    gcse = qual.loc[(df["highest_qualification"] == "GCSE/0") | (df["highest_qualification"] == "GCSE/CSE") | (df["highest_qualification"] == "GCSE/O Level")]
    higher = qual.loc[(df["highest_qualification"] == "Higher/Sub Degree")]
    btec = qual.loc[(df["highest_qualification"] == "ONC/BTEC")]
    aLevel = qual.loc[(df["highest_qualification"] == "A Levels")]
    other = len(qual) - (len(none) + len(degree) + len(gcse) + len(higher) + len(btec) + len(aLevel))
    explodes = [0, 0.3, 0, 0, 0, 0, 0]
    
    fig, axs = plt.subplots(1, 2)

    axs[0].pie([len(none), len(degree), len(gcse), len(higher), len(btec), len(aLevel), other], labels=qualifications,
            autopct="%.1f%%", pctdistance=0.7, textprops={"fontsize": 7.5}, explode=explodes)
    axs[0].set_title("Smokers")

    df = pd.read_csv("non-smokers.csv")
    qual = df.dropna(subset=["highest_qualification"])

    qualifications = ["No Qualification", "Degree", "GCSE", "Higher/Sub Degree", "ONC/BTEC", "A Levels", "Other"]
    none = qual.loc[(df["highest_qualification"] == "No Qualification")]
    degree = qual.loc[(df["highest_qualification"] == "Degree")]
    gcse = qual.loc[(df["highest_qualification"] == "GCSE/0") | (df["highest_qualification"] == "GCSE/CSE") | (df["highest_qualification"] == "GCSE/O Level")]
    higher = qual.loc[(df["highest_qualification"] == "Higher/Sub Degree")]
    btec = qual.loc[(df["highest_qualification"] == "ONC/BTEC")]
    aLevel = qual.loc[(df["highest_qualification"] == "A Levels")]
    other = len(qual) - (len(none) + len(degree) + len(gcse) + len(higher) + len(btec) + len(aLevel))

    axs[1].pie([len(none), len(degree), len(gcse), len(higher), len(btec), len(aLevel), other], labels=qualifications,
            autopct="%.1f%%", pctdistance=0.7, textprops={"fontsize": 7.5}, explode=explodes)
    axs[1].set_title("Non-Smokers")

    fig.suptitle("Population by Qualification", fontsize=30, fontname="Carlito")
    plt.tight_layout()
    plt.savefig("qualifications.png", dpi=300, bbox_inches="tight")

def displayHabits():
    style.use("dark_background")
    smokers = pd.read_csv("smokers.csv")

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))    

    axs[0].scatter(smokers["age"], smokers["amt_weekdays"], marker="x", s=20, color="r")
    axs[0].set_title("Weekdays")
    axs[0].set_ylabel("Number of Times Smoking a Day")
    axs[0].set_xlabel("Age")
    axs[0].grid(True)
    
    axs[1].scatter(smokers["age"], smokers["amt_weekends"], marker="x", s=20, color="r")
    axs[1].set_title("Weekends")
    axs[1].set_ylabel("Number of Times Smoking a Day")
    axs[1].set_xlabel("Age")
    axs[1].grid(True)

    fig.suptitle("Smoking Habits: Weekdays vs. Weekends", fontsize=30, fontname="Carlito")
    plt.tight_layout()
    plt.savefig("habits.png", dpi=500, bbox_inches="tight")

displayHabits()