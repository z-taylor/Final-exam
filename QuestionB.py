class ticketSystem():
    def __init__(self, title, seats, adultPrice, kidPrice):
        self.title = str(title)
        self.seats = int(seats)
        self.adultPrice = float(adultPrice)
        self.kidPrice = float(kidPrice)
    def bookTickets(self, adultTickets, kidTickets):
        totalTickets = adultTickets+kidTickets
        if totalTickets > self.seats:
            print("Not enough seats available for your order")
        else:
            self.seats -= totalTickets
            totalPrice = (adultTickets * self.adultPrice) + (kidTickets * self.kidPrice)
            print(f"Your order has been placed successfully!\nMovie: {self.title}\nSeats booked: {totalTickets} ({adultTickets} Adult tickets and {kidTickets} Kids tickets)\nTotal price: ${totalPrice}\nSeats left for this movie: {self.seats}")

matrix = ticketSystem("The Matrix", 100, 12, 8)

print(f"Welcome to our movie theater! Please fill in your details below.\nMovie available: {matrix.title}\nAdult ticket price: ${matrix.adultPrice}\nKids ticket price: ${matrix.kidPrice}")
adultTickets = int(input("Enter the number of adult tickets you want to book: "))
kidTickets = int(input("Enter the number of kids tickets you want to book: "))
matrix.bookTickets(adultTickets, kidTickets)