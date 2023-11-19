class ElectricMountainRailway:
    def __init__(self):
        self.total_passengers = {f"Up {i+1}": 0 for i in range(4)}
        self.total_money = {f"Up {i+1}": 0 for i in range(4)}

        self.available_tickets = {f"Up {i+1}": 480 for i in range(4)}
        self.group_discount_threshold = 10

    def display_screen(self):
        print("\nTrain Schedule:")
        for i in range(4):
            print(f"{9 + i * 2:02}:00 - Up {i + 1} - Tickets available: {self.available_tickets[f'Up {i+1}']}")

    def purchase_tickets(self, journey, num_tickets):
        if self.available_tickets[journey] >= num_tickets:
            self.available_tickets[journey] -= num_tickets


            ticket_price = 25
            total_price = num_tickets * ticket_price
            free_tickets = (num_tickets // self.group_discount_threshold) * ticket_price
            total_price -= free_tickets


            self.total_passengers[journey] += num_tickets
            self.total_money[journey] += total_price

            print(f"\nTickets purchased for {journey}. Total price: ${total_price:.2f}")
        else:
            print(f"\nTickets for {journey} are sold out. Sorry!")

    def end_of_day_summary(self):
        print("\nEnd of Day Summary:")
        for journey in self.total_passengers:
            print(f"Train {journey}: {self.total_passengers[journey]} passengers, Total money: ${self.total_money[journey]:.2f}")

        total_passengers_day = sum(self.total_passengers.values())
        total_money_day = sum(self.total_money.values())
        print(f"\nTotal Passengers for the Day: {total_passengers_day}")
        print(f"Total Money for the Day: ${total_money_day:.2f}")

        most_popular_journey = max(self.total_passengers, key=self.total_passengers.get)
        print(f"Most Popular Journey: Train {most_popular_journey} with {self.total_passengers[most_popular_journey]} passengers.")


def main():
    railway = ElectricMountainRailway()

    # Task 1
    railway.display_screen()

    # Task 2
    railway.purchase_tickets("Up 1", 5)
    railway.purchase_tickets("Up 2", 15)
    railway.purchase_tickets("Up 3", 10)

    # Display screen after ticket purchases
    railway.display_screen()

    # Task 3 - End of the Day
    railway.end_of_day_summary()


if __name__ == "__main__":
    main()
