# The starting point for this task is the module lab6_flight, that is,
# the Flight class. Note that one attribute of this class is a list of flight
# passengers the elements of which are objects of the class Passenger and/or its
# subclasses BusinessPassenger and EconomyPassenger defined in the module
# lab6_passengers.
# Your task is to create functions for
# - serialising (writing) objects of the class Flight into a .json file
# - deserializing (reconstructing) objects of the class Flight from a
#   .json file (created using the previous function)
#
# Note: function __str__ in the flight class needs to be modified
# in particular, the formatting of the departure attribute so that
# we can expect to receive departure as either string or datetime
# object and be able to format it. To that end, add, to the Flight
# class a new static method (format_departure(departure_obj))

import json
from datetime import datetime
from lab6.lab6_flight import Flight
from lab6.lab6_passengers import BusinessPassenger, EconomyPassenger

known_classses = {
    'Flight': Flight,
    'BusinessPassenger': BusinessPassenger,
    'EconomyPassenger': EconomyPassenger
}

def serialise_to_json(obj):

    obj_type = type(obj).__name__

    if not isinstance(obj, tuple(known_classses.values())):
        raise TypeError("Error! Cannot serialise objects of type " + obj_type)

    obj_dict = {'__classname__': obj_type}
    obj_dict.update(vars(obj))

    if isinstance(obj, Flight):
        departure_var = '_Flight__departure'
        obj_dict[departure_var] = datetime.strftime(obj_dict[departure_var], Flight.departure_format)

    return obj_dict


def deserialise_from_json(json_obj):

    class_name = json_obj['__classname__']

    if class_name not in known_classses.keys():
        return json_obj

    cls = known_classses[class_name]
    obj = cls.__new__(cls)

    for key, val in json_obj.items():
        setattr(obj, key, val)

    return obj


# To add to the Flight class:
#     @staticmethod
#     def format_departure(departure):
#         if isinstance(departure, str):
#             return departure
#         try:
#             return datetime.strftime(departure, Flight.departure_format)
#         except ValueError as val_err:
#             print(val_err)
#             return "unknown"



if __name__ == '__main__':

    lh992 = Flight.from_Frankfurt_by_Lufthansa('LH992', '2018-11-03 12:20')
    lh992.destination = "Amsterdam"
    # print(lh992)
    # print()

    lh1411 = Flight('LH1411', '2018-11-03 6:50', origin='Belgrade', destination='Frankfurt')
    # print(lh1411)
    # print()

    bob = BusinessPassenger("Bob Smith", "123456", air_miles=1000, checked_in=True)
    john = EconomyPassenger("John Smith", "987654", checked_in=False)
    bill = EconomyPassenger("Billy Stone", "917253", air_miles=5000, checked_in=True)
    dona = EconomyPassenger("Dona Stone", "917253", air_miles=2500, checked_in=True)
    kate = EconomyPassenger("Kate Fox", "114252", air_miles=3500, checked_in=True)

    lh1411.passengers.extend([bob, john, bill, dona, kate])


    with open("Flight_LH992.json", "w") as jsonf:
        json.dump(lh992, jsonf, default=serialise_to_json, indent=4)

    with open("Flight_LH1411.json", "w") as jsonf:
        json.dump(lh1411, jsonf, default=serialise_to_json, indent=4)


    print("\nDeserialised objects:\n")

    with open("Flight_LH992.json", "r") as jsonf:
        lh992_copy = json.load(jsonf, object_hook=deserialise_from_json)
        print(lh992_copy)

    print()

    with open("Flight_LH1411.json", "r") as jsonf:
        lh1411_copy = json.load(jsonf, object_hook=deserialise_from_json)
        print(lh1411_copy)
