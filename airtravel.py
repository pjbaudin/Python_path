"""
Model for aircraft flights
"""


class Flight:
    """
    A flight with a particular passenger aircraft
    """

    # Initialization method
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self, seat):
        """
        Parse a seat designator into a valid row and letter
        :param seat: A seat designator such as '12F'
        :return: a tuple containing an integer and a string for row and seat
        """
        row_numbers, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row))

        if row not in row_numbers:
            raise ValueError("Invalid row number {}".format(row))

        return row, letter

    def allocate_seat(self, seat, passenger):
        """
        Allocate a seat to a passenger
        :param: seat: A seat designatir such as '12C' or '21F'
        :param passenger: the passenger name
        :raises: ValueError if the seat is unavailable
        """
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        """
        Relocate a pssenger to a different seat
        :param from_seat: the existing seat designator for the passenger to be moved
        :param to_seat: the new seat designator
        :return:
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate in seat {}".format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} already occupied".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_cards(self,  card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """
        An iterable series of passenger seating allocations
        """
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, letter))


class Aircraft:

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        # For simplicity's sake, we ignore complex
        # seating arrangement for first class
        return range(1, 56), "ABCDEFGHJK"


def make_flight():
    f = Flight("PA456", AirbusA319("Q-EDFT"))
    f.allocate_seat('12A', 'Pierre Baudin')
    f.allocate_seat('15F', 'Dumbell Dog')
    f.allocate_seat('15E', "Dummay Dam")
    f.allocate_seat('1C', 'Rubbish John')
    f.allocate_seat('1D', "Cokakoo")

    g = Flight("PA456", Boeing777("Q-FRTT"))
    g.allocate_seat('12A', 'Pierre Baudin')
    g.allocate_seat('15F', 'Dumbell Dog')
    g.allocate_seat('15E', "Dummay Dam")
    g.allocate_seat('1C', 'Rubbish John')
    g.allocate_seat('1D', "Cokakoo")

    return f, g


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}"      \
             "  Flight: {1}"    \
             "  Seat: {2}"      \
             "  Aircraft: {3}"  \
             " |".format(passenger, flight_number, seat, aircraft)
    banner = "+" + "-" * (len(output) - 2) + '+'
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()