import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('data.csv', parse_dates=['date'], index_col='date')

# Clean data (example cleaning steps)
df = df.dropna()  # Drop rows with missing values

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df.index, df['value'], color='blue', linewidth=1)
    ax.set_title('Line Plot of Values Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.resample('M').sum()  # Resample by month and sum values
    
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    df_bar['value'].plot(kind='bar', ax=ax, color='orange')
    ax.set_title('Monthly Bar Plot of Values')
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Value')
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='month', y='value', data=df_box, ax=ax, palette='Set3')
    ax.set_title('Box Plot of Values by Month')
    ax.set_xlabel('Month')
    ax.set_ylabel('Value')
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
