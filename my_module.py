

import json

class BaseModel:
    def __init__(self):
        self.id = None
        self.created_at = None
        self.updated_at = None

    def save(self):
        self.updated_at = datetime.now()
        # Save the object to a database or file

    def __str__(self):
        return "{}".format(self.__dict__)

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w") as f:
            json.dump({k: v.__dict__ for k, v in self.__objects.items()}, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                self.__objects = {k: BaseModel(**v) for k, v in data.items()}
        except FileNotFoundError:
            pass

