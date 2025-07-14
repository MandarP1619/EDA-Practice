import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the historical data
historical_data = pd.read_csv('C:/Users/momas/Documents/EDAPractice/IEA-EV-dataEV salesHistoricalCars.csv')

# Load the projection data
projected_data = pd.read_csv('C:/Users/momas/Documents/EDAPractice/IEA-EV-dataEV salesProjection-STEPSCars.csv')

historical_regions = historical_data['region']
print(historical_regions)

#EDA (two cleaning steps)
import pandas as pd

# Load the datasets
historical_data = pd.read_csv('C:/Users/momas/Documents/EDAPractice/IEA-EV-dataEV salesHistoricalCars.csv')
projection_data = pd.read_csv('C:/Users/momas/Documents/EDAPractice/IEA-EV-dataEV salesProjection-STEPSCars.csv')

# Check for duplicates
print(f"Historical Data: {historical_data.duplicated().sum()} duplicate rows")
print(f"Projection Data: {projection_data.duplicated().sum()} duplicate rows")

# Drop duplicates
historical_data = historical_data.drop_duplicates()
projection_data = projection_data.drop_duplicates()

# Confirm cleaning
print(f"Historical Data Shape: {historical_data.shape}")
print(f"Projection Data Shape: {projection_data.shape}")

# Check for missing values
print("Historical Data Missing Values:")
print(historical_data.isnull().sum())

print("\nProjected Data Missing Values:")
print(projected_data.isnull().sum())

# Graph 1: Divided Line Graphs Share of new cars sold that are electric 2010-2023
# Function to plot EV sales share over the years for a given region
# Filter data for EV sales share
historical_ev_sales_share = historical_data[historical_data['parameter'] == 'EV sales share']
projection_ev_sales_share = projected_data[projected_data['parameter'] == 'EV sales share']

# Combine historical and projection data
combined_ev_sales_share = pd.concat([historical_ev_sales_share, projection_ev_sales_share])

# List of specific regions to show
specific_regions = ['World', 'Norway', 'United Kingdom', 'EU27', 'China', 'USA']

# Filter data for the specific regions
filtered_data = combined_ev_sales_share[combined_ev_sales_share['region'].isin(specific_regions)]

# Create subplots
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(20, 12), sharey=True)

# Plot each region separately in a subplot
for i, region in enumerate(specific_regions):
    row = i // 3
    col = i % 3
    region_data = filtered_data[filtered_data['region'] == region]
    axes[row, col].plot(region_data['year'], region_data['value'], marker='o', label=region)
    axes[row, col].set_xlabel('Year')
    axes[row, col].set_title(f'{region}')
    axes[row, col].grid(True)
    if col == 0:
        axes[row, col].set_ylabel('EV Sales Share (%)')
    axes[row, col].legend()

plt.suptitle('Share of New Cars that are EV Over Time (2010-2023)')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('ev_sales_share_combined.png')
plt.show()

# Graph 2: Linechart of Share of new cars sold that are electric 2023
import pandas as pd
import matplotlib.pyplot as plt

# Define regions of interest
regions_of_interest = ['World', 'Norway', 'United Kingdom', 'EU27', 'China', 'USA',
                       'Germany', 'South Africa', 'India', 'Sweden']

# Filter data for BEVs and PHEVs in the specified regions and years
historical_filtered = historical_data[
    (historical_data['region'].isin(regions_of_interest)) &
    (historical_data['powertrain'].isin(['BEV', 'PHEV'])) &
    (historical_data['year'].between(2010, 2023))
]

projected_filtered = projected_data[
    (projected_data['region'].isin(regions_of_interest)) &
    (projected_data['powertrain'].isin(['BEV', 'PHEV'])) &
    (projected_data['year'].between(2010, 2023))
]

# Combine datasets
combined_data = pd.concat([historical_filtered, projected_filtered])

# Aggregate sales by year and region
aggregated_data = combined_data.groupby(['year', 'region'])['value'].sum().reset_index()

# Create subplots
fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(15, 20), sharex=True, sharey=True)
axes = axes.flatten()  # Flatten axes array for iteration

# Plot data for each region
for idx, region in enumerate(regions_of_interest):
    ax = axes[idx]
    region_data = aggregated_data[aggregated_data['region'] == region]
    ax.plot(region_data['year'], region_data['value'], marker='o', label=region, color='tab:blue')
    ax.set_title(region, fontsize=12)
    ax.grid(True)
    ax.set_xlabel('Year')
    ax.set_ylabel('Sales (Units)')

# Adjust layout
#plt.tight_layout()
plt.suptitle('Share of new cars sold that are electric from 2010 to 2023', fontsize=16, y=1.02)
plt.show()

# Graph 3: Line graph  Share of new electric cars that are fully battery-electric, 2012 to 2023
import seaborn as sns
import pandas as pd

historical_data = pd.read_csv('C:/Users/momas/Documents/EDAPractice/IEA-EV-dataEV salesHistoricalCars.csv')

countries = ['Norway', 'United Kingdom', 'World', 'China', 'Sweden']

filtered_historical_data = historical_data[
    (historical_data['region'].isin(countries))]

sns.lineplot(data=filtered_historical_data, x='year', y='value', hue = 'region', marker='o')
plt.show()

# Graph 5: geo graph Number of new electric cars sold, 2023 (Mandar)
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


# Now read the shapefile, it should be in the directory
world = gpd.read_file('C:/Users/nomas/Documents/EDAPractice/ne_10m_admin_0_countries.shp')

# Filter the data for the year 2023 and for new electric car sales
ev_sales_2023 = historical_data[(historical_data['year'] == 2023) & (historical_data['parameter'] == 'EV sales')]

# Group by region and sum the sales
ev_sales_2023_grouped = ev_sales_2023.groupby('region')['value'].sum().reset_index()

# Manually create a mapping for regions that do not match
region_mapping = {
    'United States': 'United States of America',
    'South Korea': 'Korea, Republic of',
    'Russia': 'Russian Federation',
    'Iran': 'Iran, Islamic Republic of',
    'Syria': 'Syrian Arab Republic',
    'Venezuela': 'Venezuela, Bolivarian Republic of',
    'Bolivia': 'Bolivia, Plurinational State of',
    'Tanzania': 'Tanzania, United Republic of',
    'Vietnam': 'Viet Nam',
    'Laos': "Lao People's Democratic Republic",
    'Brunei': 'Brunei Darussalam'
}

# Apply the mapping to the EV sales data
ev_sales_2023_grouped['region'] = ev_sales_2023_grouped['region'].replace(region_mapping)

# Merge the world map with the EV sales data
world_ev_sales = world.merge(ev_sales_2023_grouped, how='left', left_on='name', right_on='region')

# Plot the world map with EV sales data
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world_ev_sales.plot(column='value', ax=ax, legend=True,
                    legend_kwds={'label': "Number of New Electric Cars Sold in 2023",
                                 'orientation': "horizontal"})
plt.title('Distribution of New Electric Car Sales in 2023')
plt.show()