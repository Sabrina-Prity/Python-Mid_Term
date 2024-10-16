class Star_Cinema:
    __hall_list = []

    def entry_hall(self, rows, cols, hall_no):
        for hall in self.__hall_list:
            if hall.get_hall_no() == hall_no:
                print(f'\n\tHall with Hall_No {hall_no} already exists.')
                return
        hall = Hall(rows, cols, hall_no)
        self.__hall_list.append(hall)
        print(f'\n\tHall {hall_no} added successfully with Rows: {rows} and Columns: {cols}.')

    def view_all_halls(self):
        if not self.__hall_list:
            print("\n\tNo halls available.")
            return
        else:
            print("\n\t<----- Available Halls: ----->\n")
            for hall in self.__hall_list:
                print(f"Hall No: {hall.get_hall_no()}, Rows: {hall.get_rows()}, Columns: {hall.get_cols()}")

    def get_hall_by_no(self, hall_no):
        for hall in self.__hall_list:
            if hall.get_hall_no() == hall_no:
                return hall
        return None

    def get_all_halls(self):
        return self.__hall_list


class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self._rows = rows
        self._cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []

    def get_hall_no(self):
        return self.__hall_no

    def get_rows(self):
        return self._rows

    def get_cols(self):
        return self._cols

    def entry_show(self, id, movie_name, time):
        for show in self.__show_list:
            if show[0] == id:
                print(f'\n\tShow with ID {id} already exists.')
                return
        self.__show_list.append((id, movie_name, time))

        self.__seats[id] = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        print(f'\nShow with ID: {id} added successfully for movie - "{movie_name}" in Hall -> {self.__hall_no}.')

    def view_all_shows(self):
        if not self.__show_list:
            print("\n\tNo shows available.")
            return
        else:
            self.view_show_list()

    def book_seats(self, id, r, c):
        if id not in self.__seats:
            print(f'\nInvalid Show ID. Please try again with a valid Show ID.')
            return

        if r < 0 or r >= self._rows or c < 0 or c >= self._cols:
            print(f'\nInvalid seat selection at Row {r}, Column {c}. Please choose seats within range.')
            return

        if self.__seats[id][r][c] == 1:
            print(f'\nSeat at Row {r}, Column {c} is already booked.')
        else:
            self.__seats[id][r][c] = 1
            print(f'\nSeat at Row {r}, Column {c} booked successfully for Show ID {id}.')

    def view_show_list(self):
        if not self.__show_list:
            print(f'\nNo shows available in Hall No: {self.__hall_no}.')
            return
        else:
            print(f'\n\t<----- Available Shows in Hall_no: {self.__hall_no} ----->\n')
            for show in self.__show_list:
                print(f'(Show_ID: {show[0]}, Movie: {show[1]}, Time: {show[2]})')

    def view_available_seats(self, id):
        if id not in self.__seats:
            print('Invalid Show ID. Please check and try again.')
            return
        else:
            print(f'\n<----- Available seats for Show ID: {id} ----->\n')
            available = False
            for r in range(self._rows):
                row_seats = []
                for c in range(self._cols):
                    if self.__seats[id][r][c] == 0:
                        row_seats.append('0')  
                    else:
                        row_seats.append('1')  
                print(row_seats)  
                available = True

            if not available:
                print('No available seats for this show.')


cinema = Star_Cinema()

# Initial Data
cinema.entry_hall(10, 12, 101)
cinema.entry_hall(8, 10, 102)
cinema.entry_hall(10, 10, 103)

hall_101 = cinema.get_hall_by_no(101)
hall_101.entry_show(1, "The Matrix", "6:00 PM")
hall_101.entry_show(2, "Inception", "9:00 PM")

hall_101.book_seats(1, 3, 3)

hall_102 = cinema.get_hall_by_no(102)
hall_102.entry_show(3, "Interstellar", "7:00 PM")
hall_102.entry_show(4, "Spider-Man", "10:00 PM")

hall_103 = cinema.get_hall_by_no(103)
hall_103.entry_show(5, "Jawan", "7:00 PM")

admin_password = "admin123"

run = True

while run:
    option = input("Are you an Admin or User? (A/U) or Q to Quit: ").upper()

    # Admin Menu with Check Password 
    if option == 'A':
        password = input("Enter Admin Password: ")
        if password == admin_password:
            while True:
                print("\n\t<----- Admin Options ----->")
                print("\t1 : Entry Hall")
                print("\t2 : Entry Shows")
                print("\t3 : View Halls")
                print("\t4 : View Shows")
                print("\t5 : Logout")

                choose = int(input("\nEnter Option: "))

                if choose == 1:
                    rows = int(input("\tEnter Rows: "))
                    cols = int(input("\tEnter Columns: "))
                    hall_no = int(input("\tEnter Hall_No: "))
                    cinema.entry_hall(rows, cols, hall_no)

                elif choose == 2:
                    id = int(input("\tEnter a Show_id: "))
                    movie_name = input("\tEnter movie name: ")
                    time = input("\tEnter Time (e.g., 10:00 PM): ")
                    hall_no = int(input("\n\tEnter Hall_No to add the show: "))
                    hall = cinema.get_hall_by_no(hall_no)
                    if hall:
                        hall.entry_show(id, movie_name, time)
                    else:
                        print(f'\n\tHall No {hall_no} does not exist.')

                elif choose == 3:
                    cinema.view_all_halls()

                elif choose == 4:
                    for hall in cinema.get_all_halls():
                        hall.view_all_shows()

                elif choose == 5:
                    print("\n\tLogged out successfully.")
                    break

                else:
                    print("\n\tInvalid option. Please try again.")
        else:
            print("\n\tIncorrect Password. Access Denied.")

    # User Menu
    elif option == 'U':
        while True:
            print("\n\t<----- User Options ----->")
            print("\t1 : View all shows")
            print("\t2 : View available seats")
            print("\t3 : Book seat")
            print("\t4 : Logout")

            choose = int(input("\nEnter Option: "))

            if choose == 1:
                for hall in cinema.get_all_halls():
                    hall.view_all_shows()

            elif choose == 2:
                id = int(input("\n\tEnter Show_id: "))
                found = False
                for hall in cinema.get_all_halls():
                    if id in hall._Hall__seats:
                        hall.view_available_seats(id)
                        found = True
                        break
                if not found:
                    print("\n\tShow ID not found.")

            elif choose == 3:
                id = int(input("\n\tEnter Show_id: "))
                r = int(input("\n\tEnter Row: "))
                c = int(input("\n\tEnter Column: "))
                found = False
                for hall in cinema.get_all_halls():
                    if id in hall._Hall__seats:
                        hall.book_seats(id, r, c)
                        found = True
                        break
                if not found:
                    print("\n\tShow ID not found.")

            elif choose == 4:
                print("\n\tLogged out successfully.")
                break

            else:
                print("\n\tInvalid option. Please try again.")

    # Exit Menu
    elif option == 'Q':
        run = False
        print("\n\tExiting the system. Goodbye!")
    else:
        print("\n\tInvalid option. Please enter 'A' for Admin, 'U' for User, or 'Q' to Quit.")
