import pandas as pd
import numpy as np

# Generate synthetic time series data for two years (24 data points)
start_date = pd.to_datetime('2022-01-01')
end_date = pd.to_datetime('2023-12-01')
date_range = pd.date_range(start=start_date, end=end_date, freq='H')  # Monthly frequency

# Generate random sales data with some fluctuations
np.random.seed(42)
sales = np.random.normal(loc=150, scale=20, size=len(date_range))

# Create a DataFrame for the time series data
data = pd.DataFrame({'Date': date_range, 'Sales': sales})

# Save the data to a CSV file
data.to_csv('time_series_data.csv', index=False)
