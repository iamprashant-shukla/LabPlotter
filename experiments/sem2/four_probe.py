from core.plotter import plot_xy


def four_probe_experiment():
    print("\nFour Probe Method – Band Gap")

    while True:
        try:
            n = int(input("Enter number of readings: "))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("❌ Invalid input")

    inv_t, ln_rho = [], []

    for i in range(n):
        while True:
            try:
                inv_t.append(float(input(f"1/T × 10³ [{i+1}]: ")))
                ln_rho.append(float(input(f"ln(ρ) [{i+1}]: ")))
                break
            except ValueError:
                print("❌ Enter numeric values only")

    plot_xy(
        inv_t, ln_rho,
        "1/T × 10³ (K⁻¹)",
        "ln(ρ)",
        "Band Gap by Four Probe Method",
        "four_probe.png"
    )
