# The starting point for this task is the module lab6_passengers, that is,
# the Passenger class and its subclasses BusinessPassenger and EconomyPassenger.
# Your task is to create functions for
# - serialising (writing) objects of the class Passenger and its subclasses
#   into a .json file
# - deserializing (reconstructing) objects of the class Passenger and its subclasses
#   from a .json file (created using the previous function)


import json
from sys import stderr
from lab6.lab6_passengers import Passenger, BusinessPassenger, EconomyPassenger

known_classes = {
    'Passenger': Passenger,
    'BusinessPassenger': BusinessPassenger,
    'EconomyPassenger': EconomyPassenger
}

def serialise_to_json(obj):

    obj_type = type(obj).__name__

    if isinstance(obj, tuple(known_classes.values())):
        d = {"__classname__": obj_type}
        d.update(vars(obj))
        return d
    else:
        raise TypeError("Error! Received object of type " + obj_type +
                        "; can only serialise objects of the following types:\n" +
                        ", ".join(known_classes.keys()))


def deserialize_from_json(json_obj):

    try:
        class_name = json_obj['__classname__']
    except KeyError as key_err:
        stderr.write("Error: __classname__ key is not available - cannot determine the type of object")
        stderr.write(str(key_err))
        return json_obj

    if class_name not in known_classes.keys():
        stderr.write("Object of unknown class '{}'; cannot be processed".format(class_name))
        return json_obj

    cls = known_classes[class_name]
    obj = cls.__new__(cls)
    for key, val in json_obj.items():
        setattr(obj, key, val)
    return obj


class PassengerEncoder(json.JSONEncoder):

    def default(self, o):

        o_type = type(o).__name__

        if not isinstance(o, tuple(known_classes.values())):
            known_types = ", ".join(known_classes.keys())
            stderr.write('Cannot serialise objects of type {0}, '
                         'only objects of the following types: {1}'.format(o_type, known_types))
            return super().default(self, o)

        d = {"__classname__": o_type}
        d.update(vars(o))
        return d


if __name__ == '__main__':

    bob = BusinessPassenger("Bob Smith", "123456", air_miles=1000, checked_in=True)
    # print(bob)
    # print()

    john = EconomyPassenger("John Smith", "987654", checked_in=False)
    # print(john)
    # print()

    bill = EconomyPassenger("Billy Stone", "917253", air_miles=5000, checked_in=True)
    # print(bill)
    # print()

    dona = EconomyPassenger("Dona Stone", "917253", air_miles=2500, checked_in=True)
    # print(dona)
    # print()

    passengers = [bob, john, bill, dona]

    with open("passengers.json", 'w') as jsonf:
        json.dump(passengers, jsonf, default=serialise_to_json, indent=4)
        # json.dump(passengers, jsonf, cls=PassengerEncoder, indent=4)

    with open("passengers.json", "r") as jsonf:
        passengers_copy = json.load(jsonf, object_hook=deserialize_from_json)
        print("\n\n".join([str(p) for p in passengers_copy]))
