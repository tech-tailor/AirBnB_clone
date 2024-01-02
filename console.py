#!/usr/bin/python3
"""cli package"""


import cmd
from models.base_model import BaseModel
import shlex
import models


class HBNBCommand(cmd.Cmd):
    """class for a command line interpreter"""

    prompt = "(hbnb) "
    class_names = ['BaseModel', 'dddd']

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """overide the execution of last command"""
        pass

    def do_EOF(self, arg):
        """You can enter $^D to stop the program"""
        print()
        return True

    def do_create(self, line):
        """ create instance of the the BaseModel class"""
        if line and line in self.class_names:
            model_instance = BaseModel()
            model_instance.save()
            instance_id = model_instance.id
            print(instance_id)
        elif line:
            print("** class name doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """print string representation of a class"""
        args = shlex.split(line)
        if len(args) == 0:
            print('** class name missing **')
        elif len(args) == 1 and str(args[0]) not in self.class_names:
            print("** class doesn't exist **")
        elif len(args) == 1 and args[0] in self.class_names:
            print("** instance id is missing **")
        else:
            try:
                key = f"{args[0]}.{args[1]}"
                objects = models.storage.all()
                value = objects[key]
                print(value)
            except Exception:
                print("** no instance found  **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id"""
        args = shlex.split(line)
        if len(args) == 0:
            print('** class name missing **')
        elif len(args) == 1 and str(args[0]) not in self.class_names:
            print("** class doesn't exist **")
        elif len(args) == 1 and args[0] in self.class_names:
            print("** instance id is missing **")
        else:
            try:
                key = f"{args[0]}.{args[1]}"
                objects = models.storage.all()
                obj = objects[key]
                objects.pop(key)
                del obj
                models.storage.save()
            except Exception:
                print("** no instance found  **")

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name"""
        args = shlex.split(line)
        if len(args) == 1 and (args[0]) not in self.class_names:
            print("** class doesn't exist **")
            # if len(args) == 0 or str(args[0]) not in self.class_names
            # print('** class name missing **')
        else:
            all_obj = []
            objects = models.storage.all()
            for key in objects.keys():
                value = objects[key]
                all_obj.append(str(value))
            print(all_obj)

    def do_update(self, line):
        """Updates an instance based on
        the class name and id"""
        args = shlex.split(line)
        if len(args) == 0:
            print('** class name missing **')
        elif len(args) == 1 and str(args[0]) not in self.class_names:
            print("** class doesn't exist **")
        elif len(args) == 1 and args[0] in self.class_names:
            print("** instance id is missing **")
        else:
            try:
                key = f"{args[0]}.{args[1]}"
                objects = models.storage.all()
                obj = objects[key]
                if obj and len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
            except Exception:
                print("** no instance found  **")
            try:
                if len(args) >= 4:
                    attr_name = args[2]
                    attr_value = (args[3])
                    setattr(obj, attr_name, attr_value)
                    print(attr_name, attr_value)
                    # print(obj)
                    models.storage.save()
            except Exception as e:
                print("** no instance found  **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
