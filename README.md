# Time-Series-Analysis
Python code for time-series analysis in a project on battery immersion cooling for electric vehicles
Developed using Pandas and Matplotlib, it showcases handling and visualisation of experimental data. Data remains confidential; however, I've been granted permission to share the code for portfolio display only.

Charging Data Plots V2 (refined) changes:

print_versions Function: The original version used individual print statements for each library version. The refined code uses a loop over a dictionary, reducing repetition and making it easier to add or remove libraries in the future.

plot_time_series Function: The refined function is designed to accept a list of column names (data_cols) instead of a single column name, enabling it to plot multiple time series in one call. This reduces the number of times the function needs to be called and makes the code more compact.

descriptive_statistics Function: Similar to plot_time_series, the function is modified to handle multiple columns. It iterates over a list of column names, which streamlines the process of printing descriptive statistics for each column.

Exception Handling: The error messages in the exception handling block have been made more concise.
