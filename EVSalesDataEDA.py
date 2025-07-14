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