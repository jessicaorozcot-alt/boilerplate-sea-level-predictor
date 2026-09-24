import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv') 

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Create first line of best fit
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_levels_extended = res_all.intercept + res_all.slope * years_extended
    plt.plot(years_extended, sea_levels_extended, 'r', label='Fit: 1880-2050')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    sea_levels_recent = res_recent.intercept + res_recent.slope * years_recent
    plt.plot(years_recent, sea_levels_recent, 'green', label='Fit: 2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')  

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()