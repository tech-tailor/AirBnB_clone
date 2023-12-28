#!/usr/bin/python3
"""cli package"""


import cmd


class HBNBCommand(cmd.Cmd):
    """class for cli"""

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """enter quit to stop the console"""
        return 1

    def do_EOF(self, arg):
        """You can enter $^D to stop the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
