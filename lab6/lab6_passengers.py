# Create the FlightService enumeration that defines the following items (services):
# snack, free e-journal, priority boarding, selection of food and drinks,
# free onboard wifi, and an item for cases when services are not specified.
#
# Create the Passenger class with the following attributes:
# - name - passenger name and surname
# - passport - passenger's passport number (as string); private attribute
# - air_miles - the number of miles the passenger has made with the given air company;
#   zero if not specified
# - checked_in - a boolean indicator variable, true if the passenger has checked in;
#   False if not specified
# - services - a class attribute defining the list of services available to all
#   passengers of a particular class (category); available services for various categories
#   of passengers should be defined as elements of the FlightService enumeration.
#   For this class, services are undefined (FlightService.UNDEFINED), as they depend on
#   the passenger's class and will be defined in the subclasses.
#
# In addition, the Passenger class should implement the following methods:
# - constructor (__init__()) - only name and passport have to be specified
# - get and set methods for the passport attribute (using appropriate decorators);
#   designate it as a private attribute and assure that it is a string of length 6,
#   consisting of digits only.
# - a method that returns a string representation of a Passenger object (__str__())
# - a method (available_services()) that returns a list of strings describing services
#   available to the passengers (a class method); this list is created based on the
#   services attribute.
#
# Create class EconomyPassenger that extends the Passenger class and has:
# - method candidate_for_upgrade that check if the passenger is a candidate for an upgrade
#   and returns an appropriate boolean value; a passenger is a candidate for upgrade if their
#   their current air miles exceed the given threshold (input parameter) and the passenger
#   has checked in
# - changed value for the services class attribute, which includes the following elements of
#   the FlightServices enum: snack, free e-journal
# - overridden __str__ method so that it first prints "Economy class passenger" and then
#   the available information about the passenger
#
# Create class BusinessPassenger that extends the Passenger class and has:
# - changed value for the services class attribute, so that it includes the following elements of
#   the FlightServices enum: priority boarding, selection of food and drinks, free onboard wifi
# - overridden __str__ method so that it first prints "Business class passenger" and then
#   the available information about the passengers


from enum import Enum


class FlightServices(Enum):
    """
    Enum defining the kinds of services available to
    different categories of passengers on a flight
    """

    UNDEFINED = "Undefined"
    SNACK = "Snack"
    FREE_E_JOURNAL = "Free e-journal"
    PRIORITY_BOARDING = "Priority boarding"
    SELECTION_OF_FOOD_AND_DRINKS = "Selection of food and drinks"
    FREE_ONBOARD_WIFI = "Free on-board WiFi"


class Passenger:

    services = [FlightServices.UNDEFINED]

    def __init__(self, name, passport, air_miles = 0, checked_in = False):
        self.name = name
        self.passport = passport
        self.air_miles = air_miles
        self.checked_in = checked_in


    def __str__(self):
        passenger_str = self.name + \
                        ", passport number: " + self.passport + \
                        ", air miles: " + str(self.air_miles) + "; "
        passenger_str += "completed check-in" if self.checked_in else "not yet checked-in"
        passenger_str += "\navailable services: " + ", ".join(self.available_services())
        return passenger_str


    @property
    def passport(self):
        return self.__passport


    @passport.setter
    def passport(self, passport):
        """Passport number has to be a string of length 6, consisting of digits only"""

        if (len(passport) == 6) and self.all_digits(passport):
            self.__passport = passport
        else:
            print("Error! Passport number has to be a string of length 6, consisting of digits only")


    @staticmethod
    def all_digits(str_val):
        digit_indicators = [ch.isdigit() for ch in str_val]
        return all(digit_indicators)


    @classmethod
    def available_services(cls):
        return [service.value for service in cls.services]


class EconomyPassenger(Passenger):

    services = [FlightServices.SNACK, FlightServices.FREE_E_JOURNAL]

    def candidate_for_upgrade(self, threshold):
        return self.checked_in and (self.air_miles > threshold)

    def __str__(self):
        return "Economy class passenger:\n" + super().__str__()


class BusinessPassenger(Passenger):

    services = [FlightServices.PRIORITY_BOARDING,
                FlightServices.FREE_ONBOARD_WIFI,
                FlightServices.SELECTION_OF_FOOD_AND_DRINKS]

    def __str__(self):
        return "Business class passenger:\n" + super().__str__()



if __name__ == '__main__':

    pass

    bob = BusinessPassenger("Bob Smith", "123456", air_miles=1000, checked_in=True)
    print(bob)
    print()
    john = EconomyPassenger("John Smith", "987654", checked_in=False)
    print(john)
    print()
    bill = EconomyPassenger("Billy Stone", "917253", air_miles=5000, checked_in=True)
    print(bill)
    print()
    dona = EconomyPassenger("Dona Stone", "917253", air_miles=2500, checked_in=True)
    print(dona)
