# Define the source matrix
source_matrix = [
    [75, 125, 180, 230, 280, 330, 380, 430, 480, 530, 580, 630, 680, 730, 780, 830, 880, 930, 980, 1030, 1080],
    [110, 160, 210, 260, 310, 360, 410, 460, 510, 560, 610, 660, 710, 760, 810, 860, 910, 960, 1010, 1060, 1110],
    [150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150]
]

# Function to calculate and display cost for slab 1
def costSlab1():
    print("\nElectricity Bill - Slab 1")
    print("Unit Range: 0 to 100, Cost per unit: Rs.10")

    units_consumed = int(input("Enter the number of units consumed: "))
    if units_consumed <= 100:
        cost = units_consumed * 10
        print(f"Total Cost: Rs.{cost:.2f}")
    else:
        print("Invalid input. Units consumed should be in the range 0 to 100.")

# Function to calculate and display cost for slab 2
def costSlab2():
    print("\nElectricity Bill - Slab 2")
    print("Unit Range: 101 to 200, Cost per unit: Rs.15")

    units_consumed = int(input("Enter the number of units consumed: "))
    if 101 <= units_consumed <= 200:
        cost = (units_consumed - 100) * 15
        print(f"Total Cost: Rs.{cost:.2f}")
    else:
        print("Invalid input. Units consumed should be in the range 101 to 200.")

# Function to calculate and display cost for slab 3
def costSlab3():
    print("\nElectricity Bill - Slab 3")
    print("Unit Range: 201 to 300, Cost per unit: Rs.20")

    units_consumed = int(input("Enter the number of units consumed: "))
    if 201 <= units_consumed <= 300:
        cost = (units_consumed - 200) * 20
        print(f"Total Cost: Rs.{cost:.2f}")
    else:
        print("Invalid input. Units consumed should be in the range 201 to 300.")

# Main menu
def main():
    student_id = input("Enter student's ID: ")

    while True:
        print("\nMenu:")
        print("1. Display the bill of slab 1 and slab 2.")
        print("2. Display the bill of slab 3.")
        print("Press any other key to exit.")

        choice = input("Enter your choice: ")

        if choice == '1':
            costSlab1()
            costSlab2()
        elif choice == '2':
            costSlab3()
        else:
            break

    print("\nProgram terminated.")

if __name__ == "__main__":
    main()
