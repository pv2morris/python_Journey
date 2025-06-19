import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

# Load and filter data
df = pd.read_csv("owid_co2_data.csv")
df_2021 = df[df['year'] == 2021]
df_2021 = df_2021.dropna(subset=['gdp', 'co2', 'population', 'country'])

# Filter countries with valid data
df_2021 = df_2021[df_2021['gdp'] > 0]

# Assign colors by country (default gray if not listed)
color_map = {
    'China': 'red',
    'United States': 'blue',
    'India': 'green',
    'Japan': 'purple',
    'Germany': 'orange',
    'United Kingdom': 'brown',
    'Brazil': 'gold',
    'Russia': 'pink'
}
df_2021['color'] = df_2021['country'].map(color_map).fillna('gray')

# Bubble sizes (scaled by population)
sizes = df_2021['population'] / 1e6 * 10

# Create plot
fig, ax = plt.subplots(figsize=(12, 7))
scatter = ax.scatter(
    df_2021['gdp'],
    df_2021['co2'],
    s=sizes,
    c=df_2021['color'],
    alpha=0.8,
    edgecolors='w',
    linewidths=0.5
)

# Label only countries with population > 200 million
for i, row in df_2021.iterrows():
    if row['population'] > 200_000_000:
        ax.text(row['gdp'], row['co2'], row['country'], fontsize=9, ha='center')

# Add interactive tooltips for all points
cursor = mplcursors.cursor(scatter, hover=True)
@cursor.connect("add")
def on_add(sel):
    row = df_2021.iloc[sel.index]
    sel.annotation.set_text(
        f"{row['country']}\nGDP: {row['gdp']:.0f}\nCO₂: {row['co2']:.0f} Mt"
    )

# Add labels and title
ax.set_xscale('log')
ax.set_xlabel("GDP (log scale)")
ax.set_ylabel("CO₂ Emissions (million tonnes)")
ax.set_title("CO₂ Emissions vs GDP in 2021")
ax.grid(True)
plt.tight_layout()

# Show plot
plt.show()