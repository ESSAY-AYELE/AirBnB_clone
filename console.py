#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
import re
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def tokenize(args):
    curly_brace = re.search(r"\{(.*?)\}", args)
    bracket = re.search(r"\[(.*?)\]", args)

    if curly_brace is None:
        if bracket is None:
            return [i.strip(",") for i in split(args)]
        else:
            tmp = split(args[:bracket.span()[0]])
            tmp1 = [i.strip(',') for i in tmp]
            tmp1.append(bracket.group())
            return tmp1
    else:
        tmp = split(args[:curly_brace.span()[0]])
        tmp1 = [i.strip(',') for i in tmp]
        tmp1.append(curly_brace.group())
        return tmp1


class HBNBCommand(cmd.Cmd):
    """You must use the module cmd
        Your class definition must be: class HBNBCommand(cmd.Cmd):
        Your command interpreter should implement:
        quit and EOF to exit the program
        help (this action is provided by default by cmd but
        you should keep it updated and documented as you work through tasks)
        a custom prompt: (hbnb)
        an empty line + ENTER shouldn’t execute anything
        Your code should not be executed when imported"""

    prompt = "(hbnb) "
    __class = [
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"]

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if (len(arg) == 0):
            print("** class name missing **")
            return
        args = tokenize(arg)

        if args[0] not in HBNBCommand.__class:
            print("** class doesn't exist **")
            return
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_quit(self, arg):
        """ quit the program"""
        return True

    def do_EOF(self, arg):
        """ eof signal the program to exit"""
        print("")
        return (True)

    def emptyline(self):
        """ do nothing"""
        pass

    def do_show(self, arg):
        """Prints the string representation of
        an instance based on the class name
        usage: show <class> <id>"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = tokenize(arg)
        objects = storage.all()
        if args[0] not in self.__class:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if "{}.{}".format(args[0], args[1]) not in objects:
            print("** no instance found **")
            return
        else:
            print(objects["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = tokenize(arg)
        objects = storage.all()
        if args[0] not in self.__class:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if "{}.{}".format(args[0], args[1]) not in objects:
            print("** no instance found **")
            return
        else:
            del objects["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_update(self, arg):
        """Updates an instance based on the class name and
        id by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"""
        if len(arg) == 0:
            print("** class name missing **")
            return False
        args = tokenize(arg)
        objects = storage.all()
        args = tokenize(arg)
        objects = storage.all()
        if args[0] not in self.__class:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in objects:
            print("** no instance found **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args) > 3:
            instance = objects["{}.{}".format(args[0], args[1])]
            if args[2] in instance.__class__.__dict__.keys():
                typeof = type(instance.__dict__[args[2]])
                instance.__dict__[args[2]] = typeof(args[3])
            else:
                instance.__dict__[args[2]] = args[3]
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
