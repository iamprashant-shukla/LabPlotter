from core.plotter import plot_xy


def planck_experiment():
    print("\nPlanck’s Constant – Photoelectric Effect")

    for color in ["Red", "Green", "Blue"]:
        print(f"\n{color} Filter")

        while True:
            try:
                n = int(input("Enter number of readings: "))
                if n <= 0:
                    raise ValueError
                break
            except ValueError:
                print("❌ Invalid input")

        voltage, current = [], []

        for i in range(n):
            while True:
                try:
                    voltage.append(float(input(f"Negative Anode Voltage (V) [{i+1}]: ")))
                    current.append(float(input(f"Photocurrent (nA) [{i+1}]: ")))
                    break
                except ValueError:
                    print("❌ Enter numeric values only")

        plot_xy(
            voltage, current,
            "Negative Anode Voltage (V)",
            "Photocurrent (nA)",
            f"Photoelectric Effect – {color}",
            f"planck_{color.lower()}.png"
        )
