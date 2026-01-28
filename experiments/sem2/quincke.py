from core.plotter import plot_xy


def quincke_experiment():
    print("\nQuincke’s Method – Susceptibility")

    while True:
        try:
            n = int(input("Enter number of readings: "))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("❌ Invalid input")

    H, h = [], []

    for i in range(n):
        while True:
            try:
                H.append(float(input(f"Magnetic Field H [{i+1}]: ")))
                h.append(float(input(f"Rise in liquid level h [{i+1}]: ")))
                break
            except ValueError:
                print("❌ Enter numeric values only")

    plot_xy(
        H, h,
        "Magnetic Field H",
        "Rise in Liquid Level h",
        "Quincke’s Method",
        "quincke.png"
    )
