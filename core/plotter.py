import matplotlib.pyplot as plt


def plot_xy(x, y, x_label, y_label, title, filename):
    if len(x) != len(y):
        print("❌ Error: X and Y data length mismatch")
        return

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', linewidth=1.5)

    plt.xlabel(x_label)
    plt.ylabel(y_label) 
    plt.title(title)
    plt.grid(True)

    plt.savefig(f"outputs/graphs/{filename}", dpi=300)
    plt.show()
