import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1: Load dataset (Example dataset, you can replace it with your own)
df = sns.load_dataset("tips")  # This is an example dataset in Seaborn

# 2: Create an overweight column (Example condition)
df['overweight'] = df['total_bill'] > 20  # Example condition: overweight if total bill > 20

# 3: (Optional step can be added here based on your dataset needs)

# 4: Function to draw categorical plot
def draw_cat_plot():
    # 5: Create a categorical plot (Example: a boxplot based on 'overweight' column)
    df_cat = df[['overweight', 'day', 'total_bill']]  # Selecting relevant columns

    # 6: Create a seaborn categorical plot (you can use barplot, boxplot, etc.)
    sns.set(style="whitegrid")
    cat_plot = sns.catplot(x="day", hue="overweight", kind="count", data=df_cat)

    # 7: Customize the plot if needed (e.g., add title, change labels, etc.)
    cat_plot.fig.suptitle("Categorical Plot of Overweight by Day", fontsize=15)
    cat_plot.set_axis_labels("Day of the Week", "Count of Overweight People")

    # 8: Save the plot as a PNG file
    fig = cat_plot.fig

    # 9: Save the figure to a file
    fig.savefig('catplot.png')
    return fig


# 10: Function to draw heatmap plot
def draw_heat_map():
    # 11: Create a heatmap (Example: correlation matrix of the dataset)
    df_heat = df.corr()  # Use correlation matrix of the numeric columns in the dataset

    # 12: Compute correlation matrix for heatmap
    corr = df_heat

    # 13: Mask the upper triangle for better visualization
    mask = np.triu(np.ones_like(corr, dtype=bool))  # Masking the upper triangle of the heatmap

    # 14: Create the heatmap figure
    fig, ax = plt.subplots(figsize=(8, 6))  # You can adjust the size as needed
    sns.heatmap(corr, mask=mask, annot=True, cmap="coolwarm", fmt='.2f', ax=ax)

    # 15: Customize the heatmap (e.g., add title, color bar, etc.)
    ax.set_title("Heatmap of Correlations Between Features", fontsize=15)

    # 16: Save the figure to a file
    fig.savefig('heatmap.png')
    return fig


# Example of how to run both functions
draw_cat_plot()  # This will generate the cat plot
draw_heat_map()  # This will generate the heatmap
