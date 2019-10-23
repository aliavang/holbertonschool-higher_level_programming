#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


class Base:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize ID

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string to file

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        filename = "{}.json".format(cls)
        my_obj = Base.to_json_string([list_objs])
        with open(filename, 'w') as f:
            json.dump(my_obj, f)

    @classmethod
    def from_json_string(json_string):
        """Return list of JSON string representation

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        import json
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
