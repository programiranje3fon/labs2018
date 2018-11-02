# Create the Flight class with the following attributes:
# - flight_num - flight number
# - departure - the date and time of the departure
# - origin - the location the flight departs from
# - destination - the destination of the flight
# - operated_by - the company that operates the flight
# - passengers - list of passengers, that is, instances of the Passenger class
#
# Use appropriate decorators to create get and set methods for the following attributes:
# - departure - make it a private attribute and assure that it is a datetime object of the format:
#   "%Y-%m-%d %H:%M"; consider defining this format as a class attribute (departure_format)
# - flight_num - make it a private attribute and assure that the flight number consist of
#   two letters followed by 3-4 digits
# - passengers - make it a private attribute and assure that only objects of the type Passenger
#   can be added to the passengers list; if None is passed to the setter, create an empty
#   passengers list
#
# The Flight class should implement the following methods:
# - constructor (__init__())
# - method that returns a string representation of the given Flight object (__str__())
# - class method from_Frankfurt_by_Lufthansa() that creates flights that fly from Frankfurt and
#   are operated by Lufthansa (alternative constructor)
# - a generator method that generates a sequence of passengers who have not yet checked in
# - a generator method that generates a sequence of candidate passengers for an upgrade to
#   the business class; those are the passengers of the economy class whose air miles
#   exceed the given threshold (input parameter) and who have checked in for the flight;
#   the generated sequence should consider the passengers air miles, so that those with more
#   air miles are first offered the upgrade option



from datetime import datetime

from lab6.lab6_passengers import Passenger, BusinessPassenger, EconomyPassenger


class Flight:

    departure_format = "%Y-%m-%d %H:%M"

    def __init__(self, flight_num, departure, origin = "unknown",
                 destination = "unknown", operated_by = "unknown", passengers = None):
        self.flight_num = flight_num
        self.departure = departure
        self.origin = origin
        self.destination = destination
        self.operated_by = operated_by
        self.passengers = passengers


    @property
    def departure(self):
        return self.__departure

    @departure.setter
    def departure(self, departure):
        """Expecting departure date and time in the form: %Y-%m-%d %H:%M"""
        try:
            self.__departure = datetime.strptime(departure, self.departure_format)
        except ValueError as error:
            print(error)
            print("Error! Departure expected in the format: " + self.departure_format)


    @property
    def flight_num(self):
        return self.__flight_num

    @flight_num.setter
    def flight_num(self, flight_number):
        """Flight number should consist of two letters followed by 3-4 digits"""

        if self.flight_number_ok(flight_number):
            self.__flight_num = flight_number
        else:
            self.__flight_num = "unknown"
            print("Incorrect flight number; expected 2 letters followed by 3-4 digits")

    @staticmethod
    def flight_number_ok(flight_to_check):
        if not isinstance(flight_to_check, str):
            flight_to_check = str(flight_to_check)
        first_two_letters = flight_to_check[0].isalpha() and flight_to_check[1].isalpha()
        if not first_two_letters:
            return False
        only_digits_left = [False]*(len(flight_to_check) - 2)
        for i, ch in enumerate(flight_to_check[2:]):
            only_digits_left[i] = ch.isdigit()
        return all(only_digits_left)


    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, passengers):
        if passengers is None:
            self.__passengers = list()
            return
        for i, p in enumerate(passengers):
            if isinstance(p, Passenger):
                self.__passengers.append(p)
            else:
                print("{0} element of the input list is not a Passenger object!".format(i+1))


    def __str__(self):
        flight_str = "Flight number: " + self.flight_num + " operated by: " + self.operated_by + \
                     "\nDeparture date/time: " + datetime.strftime(self.departure, self.departure_format) + \
                     "\nOrigin: " + self.origin + "\nDestination: " + self.destination

        if len(self.passengers) == 0:
            flight_str += "\nNo passengers registered yet"
        else:
            flight_str += "\nPassengers:\n"
            flight_str += "\n".join([str(p) for p in self.passengers])

        return flight_str


    @classmethod
    def from_Frankfurt_by_Lufthansa(cls, flight_num, departure):
        return cls(flight_num, departure, origin='Frankfurt', operated_by="Lufthansa")


    def generate_non_checked_list(self):
        for passenger in self.passengers:
            if not passenger.checked_in:
                yield passenger


    def generate_upgrade_candidates(self, miles_min):
        candidates = [p for p in self.passengers if isinstance(p, EconomyPassenger) and p.candidate_for_upgrade(miles_min)]
        candidates = sorted(candidates, key=lambda passenger: passenger.air_miles, reverse=True)
        for passenger in candidates:
            yield passenger



if __name__ == '__main__':

    lh1411 = Flight('LH1411', '2018-11-03 6:50', origin='Belgrade', destination='Frankfurt')
    print(lh1411)
    print()

    lh992 = Flight.from_Frankfurt_by_Lufthansa('LH992', '2018-11-03 12:20')
    lh992.destination = "Amsterdam"
    print(lh992)
    print()

    bob = BusinessPassenger("Bob Smith", "123456", air_miles=1000, checked_in=True)
    john = EconomyPassenger("John Smith", "987654", checked_in=False)
    bill = EconomyPassenger("Billy Stone", "917253", air_miles=5000, checked_in=True)
    dona = EconomyPassenger("Dona Stone", "917253", air_miles=2500, checked_in=True)
    kate = EconomyPassenger("Kate Fox", "114252", air_miles=3500, checked_in=True)

    lh1411.passengers.extend([bob, john, bill, dona, kate])

    # print(f"After adding passengers to flight {lh1411.flight_num}:\n")
    # print(lh1411)

    # print("Last call to passengers who have not yet checked in!")
    # for passenger in lh1411.generate_non_checked_list():
    #     print(passenger)

    print("Passengers offered an upgrade opportunity:")
    for ind, passenger in enumerate(lh1411.generate_upgrade_candidates(2000)):
        print(str(ind+1) + ".\n" + str(passenger))

