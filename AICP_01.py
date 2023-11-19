
def display_menu(category, items):
    print(f"\n{category} Menu:")
    for item_code, description, price in items:
        print(f"{item_code}: {description} - ${price:.2f}")

def get_user_choice(category, items):
    while True:
        display_menu(category, items)
        user_choice = input(f"\nEnter the item code of your choice ({category}): ").upper()

        for item_code, description, price in items:
            if user_choice == item_code:
                return description, price

        print("Invalid choice. Please enter a valid item code.")

def main():
    # Define menu items for each category
    cases = [("A1", "Compact", 75.00), ("A2", "Tower", 150.00)]
    rams = [("B1", "8 GB", 79.99), ("B2", "16 GB", 149.99), ("B3", "32 GB", 299.99)]
    main_hdds = [("C1", "1 TB HDD", 49.99), ("C2", "2 TB HDD", 89.99), ("C3", "4 TB HDD", 129.99)]
    solid_state_drive =[("D1", "240 GB SSD", 59.99),("D2","480 GB SSD", 119.99)]
    second_harddisk_drive =[("E1", "1 TB HDD", 49.99), ("E2","2 TB HDD", 89.99), ("E3","4 TB HDD", 129.99)]
    optical_drive = [("F1","DVD/Blu-Ray Player", 50.00),("F2", "DVD/Blu-Ray Re-writer",100.00)]
    operating_system = [("G1","Standard Version",100.00),("G2", "professional Version", 175)]

    # Get user choices
    chosen_case, case_price = get_user_choice("Case", cases)
    chosen_ram, ram_price = get_user_choice("RAM", rams)
    chosen_main_hdd, main_hdd_price = get_user_choice("Main Hard Disk Drive", main_hdds)
    chosen_solid_state, solid_state_price = get_user_choice("Solid State Price Drive", solid_state_drive)
    chosen_second_hdd, second_hdd_price = get_user_choice("Second Hard Disk Drive", second_harddisk_drive)
    chosen_optical, optical_price = get_user_choice("Optical Drive", optical_drive)
    chosen_operating, operating_price = get_user_choice("Operating System", operating_system)

    # Calculate total price
    total_price = case_price + ram_price + main_hdd_price + solid_state_price + second_hdd_price + optical_price + operating_price

    # Display user choices and total price
    print("\nYour Choices:")
    print(f"Case: {chosen_case} - ${case_price:.2f}")
    print(f"RAM: {chosen_ram} - ${ram_price:.2f}")
    print(f"Main Hard Disk Drive: {chosen_main_hdd} - ${main_hdd_price:.2f}")
    print(f"Solid State Drive: {chosen_solid_state} - ${solid_state_price:.2f}")
    print(f"Second Hard Disk Drive: {chosen_second_hdd} - ${second_hdd_price:.2f}")
    print(f"Optical Drive: {chosen_optical} - ${optical_price:.2f}")
    print(f"Operating System: {chosen_operating} - ${operating_price:.2f}")
    print(f"\nTotal Price: ${total_price:.2f}")

if __name__ == "__main__":
    main()
