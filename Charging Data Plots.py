import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def print_versions():
    """
    Function to print versions of libraries being used. Function used for 
    formatting only
    """
    print("\n")  # For better readability in output
    print(f"Pandas version: {pd.__version__}")
    print(f"NumPy version: {np.__version__}")
    print(f"Matplotlib version: {plt.matplotlib.__version__}")
    print(f"Seaborn version: {sns.__version__}")
    print("\n")  # For better readability in output

def plot_time_series(dataframe, time_col, data_col, ylabel, title):
    """
    Function to plot a time series graph.
    """
    plt.figure(figsize=(10,5))
    plt.plot(dataframe[time_col], dataframe[data_col], label=f'{ylabel} over Time')
    plt.xlabel('Time [s]')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()

def descriptive_statistics(dataframe, column):
    """
    Function to print descriptive statistics of a dataframe column.
    """
    print(f"Descriptive statistics for {column}:")
    print(dataframe[column].describe())
    print("\n")  # For better readability in output
    
# Print the versions of the libraries being used
print_versions()

# Load Raw Charging Data
charging_data_path = r'C:\Users\joshu\Desktop\Charging Data\Raw Data\2515_230314_5CsT_ch008_007NCR3B_no header.txt'

# Attempt to read the TXT file as CSV
try:
    # Adjust the separator if needed 
    df = pd.read_csv(charging_data_path, sep=',')  
    
    # Check the first few rows to confirm it's loaded correctly
    print(df.head())

    # Plotting time series data
    plot_time_series(df, '~Time[s]', 'U[V]', 'Voltage [V]', 'Voltage Plot')
    plot_time_series(df, '~Time[s]', 'I[A]', 'Current [A]', 'Current Plot')
    plot_time_series(df, '~Time[s]', 'Ah[Ah]', 'Ampere-hour [Ah]', 'Ampere-hour Plot')
    plot_time_series(df, '~Time[s]', 'Wh[Wh]', 'Watt-hour [Wh]', 'Watt-hour Plot')
    
    # Printing descriptive statistics for each measurement
    descriptive_statistics(df, 'U[V]')
    descriptive_statistics(df, 'I[A]')
    descriptive_statistics(df, 'Ah[Ah]')
    descriptive_statistics(df, 'Wh[Wh]')
