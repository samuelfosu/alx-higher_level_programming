#!/usr/bin/python3
"""
Describes base
"""


import json


class Base:
    """Implements `Base`"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes instance attributes"""
        if (id is not None):
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json rep. of list_dictionaries"""
        if (list_dictionaries is None):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes json str rep. of list_objs tofile"""
        filename = cls.__name__ + ".json"
        content = []
        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                json_dict = json.loads(cls.to_json_string(item))
                content.append(json_dict)

        with open(filename, mode="w") as fd:
            json.dump(content, fd)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of json string representation"""
        if (json_string is None):
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with attributes set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            r2 = Rectangle(3, 8)
        elif cls.__name__ == "Square":
            r2 = Square(5)
        r2.update(**dictionary)
        return (r2)

    @classmethod
    def load_from_file(cls):
        """parameters for and instance and from that creating instances"""
        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, encoding="UTF8") as fd:
                content = cls.from_json_string(fd.read())
        except:
            return []

        instances = []

        for instance in content:
            tmp = cls.create(**instance)
            instances.append(tmp)

        return instances
