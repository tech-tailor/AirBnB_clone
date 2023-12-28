#!/usr/bin/python3
"""cli package"""


import cmd


class HBNBCommand(cmd.Cmd):
    """class for cli"""

    prompt = "(hbnb) "

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
