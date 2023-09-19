import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def describe(filepath):
    df = pd.read_csv(filepath)
    print(df.describe())

    # Create the scatter plot
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.scatter(df['mpg'], df['hp'], c='b', marker='o', edgecolors='k', alpha=0.6)
    plt.title('Scatter Plot of MPG vs. HP')
    plt.xlabel('MPG')
    plt.ylabel('HP')

    # Save the visualization as an image file
    plt.savefig('output/scatter_plot.png', dpi=300, bbox_inches='tight')

    # Display the plot (optional)
    plt.show()

def main():
    describe("data/cars.csv")

if __name__ == "__main__":
    main()