from core.plotter import plot_iv_curve


def franck_hertz_experiment():
    print("\nFranck–Hertz Experiment")
    print("Plot: Plate Current vs Grid Voltage (V2K)\n")


    while True:
        try:
            n = int(input("Enter number of readings (recommended 40–42): "))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("❌ Please enter a valid positive integer (e.g. 40).")

    grid_voltage = []
    plate_current = []

    for i in range(n):
        while True:
            try:
                v = float(input(f"Grid Voltage V2K (V) [{i+1}]: "))
                i_p = float(input(f"Plate Current (A) [{i+1}]: "))
                grid_voltage.append(v)
                plate_current.append(i_p)
                break
            except ValueError:
                print("❌ Invalid input! Enter numeric values only.")

    plot_iv_curve(
        grid_voltage,
        plate_current,
        "Grid Voltage V2K (Volts)",
        "Plate Current (Ampere)",
        "Franck–Hertz Experiment: Plate Current vs Grid Voltage",
        "franck_hertz_curve.png"
    )
