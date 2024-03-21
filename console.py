#!/usr/bin/python3
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
    }

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name
        and id
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return
        
        try:
            cls_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            objs = storage.all()
            key = "{}.{}".format(cls_name, args[1])
            obj = objs.get(key)
            if not obj:
                print("** no instance found **")
                return
            print(obj)
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the classname and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        
        try:
            cls_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            objs = storage.all()
            key = "{}.{}".format(cls_name, args[1])
            obj = objs.get(key)
            if not obj:
                print("** no instance found **")
                return
            del objs[key]
            storage.save()
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances.
        """
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attributes
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        
        try:
            cls_name = arg[0]
            objs = storage.all()
            if cls_name not in [cls.__name__ for cls in BaseModel.__subclasses__()]:
                print("** class doesn't exist **")
                return
            
            if len(args) < 2:
                print("** instance id missing **")
                return
            
            key = "{}.{}".format(cls_name, args[1])
            obj = objs.get(key)
            if not obj:
                print("** no instance found **")
                return
            
            if len(args) < 3:
                print("** attribute name missing **")
                return
            
            if len(args) < 4:
                print("** value missing **")
                return
            
            attr_name = args[2]
            attr_value = ' '.join(args[3:])

            if hasattr(obj, attr_name) and attr_name not in  ['id', 'created_at', 'updated_at']:
                attr_type = type(getattr(obj, attr_name))
                try:
                    setattr(obj, attr_name, attr_type(attr_value.strip('"')))
                    storage.save()
                except ValueError:
                    print("** invalid value **")
            else:
                print("** attribute doesn't exist **")
        except NameError:
            print("** class doesn't exist **")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """Exit the program by using EOF (Ctrl + D)"""
        print()
        return True
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()