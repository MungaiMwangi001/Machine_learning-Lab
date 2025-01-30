import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the data from the CSV
def load_data():
    df = pd.read_csv('epa-sea-level.csv')
    return df

def draw_plot():
    df = load_data()

    # Create a scatter plot of the data
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='red')

    # Create a line of best fit
    # Linear regression for all data
    fit = np.polyfit(df['Year'], df['CSIRO Adjusted Sea Level'], 1)
    fit_fn = np.poly1d(fit)
    plt.plot(df['Year'], fit_fn(df['Year']), color='blue')

    # Create a second line of best fit starting from 2000
    df_recent = df[df['Year'] >= 2000]
    fit_recent = np.polyfit(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'], 1)
    fit_fn_recent = np.poly1d(fit_recent)
    plt.plot(df_recent['Year'], fit_fn_recent(df_recent['Year']), color='green')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Show the plot
    plt.show()
