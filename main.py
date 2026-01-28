from experiments.sem2.franck_hertz import franck_hertz_experiment


def main():
    print("\n========== LabPlotter ==========")
    print("A Laboratory Graph Plotting & Calculation Tool")
    print("================================\n")

    print("Select Semester:")
    print("1. Semester 1")
    print("2. Semester 2")
    choice = input("Enter choice: ")

    if choice == "2":
        print("\nSelect Experiment:")
        print("1. Franck–Hertz Experiment")
        exp_choice = input("Enter choice: ")

        if exp_choice == "1":
            franck_hertz_experiment()
        else:
            print("❌ Invalid experiment selection")

    else:
        print("❌ Invalid semester selection")


if __name__ == "__main__":
    main()
