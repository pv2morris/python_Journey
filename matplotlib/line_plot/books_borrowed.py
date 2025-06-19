# books_borrowed.property

import os
import pandas as pd
import matplotlib.pyplot as plt

# Folder containing the CSV files
data_folder = "."

# Files you downloaded
csv_files = [
    "Libraries2012.csv",
    "Libraries2013.csv",
    "Libraries2015.csv",
    "Libraries2016.csv",
    "Libraries2021.csv",
    "Libraries2022.csv"
]

# Extracting year from each filename
def extract_year(filename):
    return ''.join(filter(str.isdigit, filename[:15]))

# Dictionary to store total circulation per year
year_totals = {}

# Process each CSV
for file in csv_files:
    year = extract_year(file)
    path = os.path.join(data_folder, file)
    df = pd.read_csv(path)

    # Try multiple common column names to avoid breakage
    for col in df.columns:
        if col in df.columns:
            total = df[col].sum()
            year_totals[int(year)] = total
            break

# Sort by year
sorted_years = sorted(year_totals.keys())
totals = [year_totals[year] for year in sorted_years]

# Plotting
plt.plot(sorted_years, totals, marker='o')
plt.title("Total Books Borrowed (Chicago Public Libraries)")
plt.xlabel("Year")
plt.ylabel("Total Circulation")
plt.grid(True)
plt.tight_layout()
plt.show()  