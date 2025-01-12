import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('sea_level_data.csv')  # Assuming your data is in this CSV file with 'Year' and 'CSIRO Adjusted Sea Level'

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Create first line of best fit (for all data)
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = range(df['Year'].min(), 2051)  # Extending to year 2050
    plt.plot(years_extended, [slope1 * year + intercept1 for year in years_extended], label='Best fit line (all data)', color='red')

    # Create second line of best fit (from 2000 onward)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    plt.plot(years_extended, [slope2 * year + intercept2 for year in years_extended], label='Best fit line (2000 onwards)', color='green')

    # Add labels and title
    plt.title('Sea Level Rise')
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level (mm)')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
