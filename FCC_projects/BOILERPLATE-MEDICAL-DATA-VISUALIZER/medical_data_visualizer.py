import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import the data
df = pd.read_csv('medical_examination.csv')

# 2. Add an overweight column based on BMI
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)) > 25
df['overweight'] = df['overweight'].astype(int)  # Convert boolean to 0 or 1

# 3. Normalize cholesterol and glucose values
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4. Draw the categorical plot
def draw_cat_plot():
    # 5. Create a DataFrame for the catplot
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])

    # 6. Group and reformat the data
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")

    # 7. Create the catplot
    fig = sns.catplot(x="variable", hue="value", col="cardio", data=df_cat, kind="count")

    # 8. Get the figure
    fig = fig.fig

    # 9. Save the catplot
    fig.savefig('catplot.png')
    return fig


# 10. Draw the heat map
def draw_heat_map():
    # 11. Clean the data by filtering incorrect data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Calculate the correlation matrix
    corr = df_heat.corr()

    # 13. Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))

    # 15. Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap='coolwarm', ax=ax)

    # 16. Save the heatmap
    fig.savefig('heatmap.png')
    return fig
