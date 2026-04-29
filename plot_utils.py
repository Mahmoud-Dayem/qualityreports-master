import math
import matplotlib.pyplot as plt
import seaborn as sns

def plot_oxide_distribution(df, oxides, cols=3, plot_type="violin+swarm"):
    """
    plot_type options:
    - 'violin'
    - 'box'
    - 'swarm'
    - 'violin+swarm'
    - 'box+swarm'
    """

    oxides = list(dict.fromkeys(oxides))  # remove duplicates
    palette = sns.color_palette("tab10", len(oxides))

    rows = math.ceil(len(oxides) / cols)
    plt.figure(figsize=(15, 5 * rows))

    for i, (oxide, color) in enumerate(zip(oxides, palette), 1):
        plt.subplot(rows, cols, i)

        if oxide not in df.columns:
            print(f"Warning: {oxide} not found")
            continue

        data = df[oxide].dropna()

        if plot_type == "violin":
            sns.violinplot(y=data, color="lightgray")

        elif plot_type == "box":
            sns.boxplot(y=data, color="lightgray")

        elif plot_type == "swarm":
            sns.swarmplot(y=data, color=color, size=3)

        elif plot_type == "violin+swarm":
            sns.violinplot(y=data, color="lightgray", inner=None)
            sns.swarmplot(y=data, color=color, size=2)

        elif plot_type == "box+swarm":
            sns.boxplot(y=data, color="lightgray")
            sns.swarmplot(y=data, color=color, size=2)

        else:
            raise ValueError("Invalid plot_type")

        plt.title(oxide)

    plt.tight_layout()
    plt.show()