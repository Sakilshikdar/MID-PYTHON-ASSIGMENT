class Star_Cinema:
    def __init__(self):
        self.hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__show_list = []
        self.seats = {}

    def add_show(self, show):
        self.__show_list.append(show)

    def add_seats(self, id, row, col):

        if id == 10 and row <= self.__rows and col <= self.__cols:
            self.seats[(row, col)] = 0
        elif id == 11 and row <= self.__rows and col <= self.__cols:
            self.seats[(row, col)] = 0
        else:
            self.seats[(row, col)] = 0

    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))

    def view_show_list(self):
        print('-----------------')
        print('Show list:')
        for show in self.__show_list:
            print(show)
        print('-----------------')

    def view_available_seats(self, id):
        print('Available seats:')
        print('-----------------')
        if id == 10:
            for i in range(0, 10):
                print('[' + ' '.join(['0'] * self.__cols) + ']')
        elif id == 11:
            for i in range(self.__rows):
                print('[' + ' '.join(['0'] * self.__cols) + ']')
        else:
            print('Invalid id')
        print('-----------------')

    def book_seats(self, id, row, col):
        if id == 10:
            for i in range(0, 10):
                for j in range(1, 6):
                    self.add_seats(id, i, j)
            self.seats[(row, col)] = 1
            print(f'Seat booked ({row},{col}) for Show {id}')
        elif id == 11:
            for i in range(1, 6):
                for j in range(2, 5):
                    self.add_seats(id, i, j)
            self.seats[(row, col)] = 1
            print(f'Seat booked ({row},{col}) for Show {id}')
        else:
            print(f'Invalid show ID {id}')


cinema = Star_Cinema()
hall = Hall(5, 5, 1)
hall2 = Hall(10, 15, 1)
cinema.entry_hall(hall)
cinema.entry_hall(hall2)
hall.add_show(
    f'MOVIE NAME:Sujon Sokhi SHOW ID: {10} TIME:25-10-2023 10:00 AM')
hall.add_show(
    f'MOVIE NAME:King Kong SHOW ID: {11} TIME:25-10-2023 01:00 PM')
for i in range(0, 10):
    for j in range(1, 6):
        hall.add_seats(id, i, j)
while True:
    print("1: VIEW ALL SHOW TODAY")
    print("2: VIEW AVIABLE SITE TODAY")
    print("3: BOOK TICKET")
    print("4: EXIT")
    ch = int(input("Enter Option:"))

    if ch == 1:
        hall.view_show_list()
    elif ch == 2:
        id = int(input("Enter show id:"))
        if id == 10:
            for i in range(0, 10):
                for j in range(1, 6):
                    hall.add_seats(id, i, j)
        elif id == 11:
            for i in range(1, 6):
                for j in range(2, 5):
                    hall.add_seats(id, i, j)
        hall.view_available_seats(id)
    elif ch == 3:
        id = int(input("Enter show id:"))
        row = int(input("Enter row:"))
        col = int(input("Enter col:"))
        hall.book_seats(id, row, col)
    elif ch == 4:
        break
    else:
        print('-----------------')
        print("Invalid Option")
        print('-----------------')
