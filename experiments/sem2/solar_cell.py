from core.plotter import plot_xy


def solar_cell_experiment():
    print("\nSolar Cell I–V Characteristics")

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
                voltage.append(float(input(f"Voltage (V) [{i+1}]: ")))
                current.append(float(input(f"Current (mA) [{i+1}]: ")))
                break
            except ValueError:
                print("❌ Enter numeric values only")

    plot_xy(
        voltage, current,
        "Voltage (V)",
        "Current (mA)",
        "Solar Cell I–V Curve",
        "solar_cell_iv.png"
    )
