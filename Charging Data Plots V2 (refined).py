import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def print_versions():
    """
    Function to print versions of libraries being used. Function used for 
    formatting only
    """
    libraries = {'Pandas': pd, 'NumPy': np, 'Matplotlib': plt.matplotlib, 'Seaborn': sns}
    for lib, module in libraries.items():
        print(f"{lib} version: {module.__version__}")
        
    libraries= 1

def plot_time_series(dataframe, time_col, data_cols, title_prefix):
    """
    Function to plot time series graphs for multiple data columns.
    """
    for data_col in data_cols:
        plt.figure(figsize=(10, 5))
        plt.plot(dataframe[time_col], dataframe[data_col], label=f'{data_col} over Time')
        plt.xlabel('Time [s]')
        plt.ylabel(data_col)
        plt.title(f'{title_prefix} {data_col}')
        plt.legend()
        plt.show()

def descriptive_statistics(dataframe, columns):
    """
    Function to print descriptive statistics of multiple dataframe columns.
    """
    for column in columns:
        print(f"Descriptive statistics for {column}:")
        print(dataframe[column].describe(), "\n")

# Print the versions of the libraries being used
print_versions()

# Load Raw Charging Data
charging_data_path = 'C:\\Users\\joshu\\Desktop\\Charging Data\\Raw Data\\2515_230314_5CsT_ch008_007NCR3B_no header.txt'

# Attempt to read the TXT file as CSV
try:
    df = pd.read_csv(charging_data_path, sep=',')
    print(df.head())

    # Plotting time series data for multiple columns
    columns_to_plot = ['U[V]', 'I[A]', 'Ah[Ah]', 'Wh[Wh]']
    plot_time_series(df, '~Time[s]', columns_to_plot, 'Plot for')

    # Printing descriptive statistics for each measurement
    descriptive_statistics(df, columns_to_plot)
