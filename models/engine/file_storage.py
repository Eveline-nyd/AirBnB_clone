#!/usr/bin/python3
import json
import importlib
from models.user import User

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    if class_name == "User":
                        User = getattr(importlib.import_module('models.user'), 'User')
                        obj_instance = User(**value)
                    else:
                        module = importlib.import_module('models.base_model')
                        class_ = getattr(module, class_name)
                        obj_instance = class_(**value)
                    FileStorage.__objects[key] = obj_instance
        except FileNotFoundError:
            pass