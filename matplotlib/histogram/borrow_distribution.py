import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Libraries2022.csv")

# Columns for each month
months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE',
          'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']

# Ensure month columns are numeric
for month in months:
    df[month] = pd.to_numeric(df[month], errors='coerce')

# Calculate total circulation per branch
df["Total Circulation"] = df[months].sum(axis=1)

# Drop rows with missing or zero total circulation
df = df.dropna(subset=["Total Circulation"])
df = df[df["Total Circulation"] > 0]

# Plot histogram with log scale
plt.figure(figsize=(10, 6))
plt.hist(df["Total Circulation"], bins=20, edgecolor="black", color="skyblue", alpha=0.8)
plt.xscale('log')

# Add mean and median lines
mean = df["Total Circulation"].mean()
median = df["Total Circulation"].median()

plt.axvline(mean, color='red', linestyle='dashed', linewidth=1.5, label=f"Mean: {int(mean):,}")
plt.axvline(median, color='green', linestyle='dotted', linewidth=1.5, label=f"Median: {int(median):,}")

# Annotate outliers (top 5%)
outliers = df[df["Total Circulation"] > df["Total Circulation"].quantile(0.95)]
for _, row in outliers.iterrows():
    plt.annotate(row["BRANCH"], xy=(row["Total Circulation"], 1),
                 xytext=(5, 5), textcoords='offset points', fontsize=8, rotation=45)

# Titles and labels
plt.title("Distribution of Total Books Borrowed by Library Branches (2022)")
plt.xlabel("Total Circulation (log scale)")
plt.ylabel("Number of Branches")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show plot
plt.show()