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