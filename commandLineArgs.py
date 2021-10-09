"""
10/4/2021
Todo: understand this program to understand how command line arguments work
Important: In the command line arguments, the first argument is ALWAYS the program name. You can verify it from the output of the line 16
Excercise: Shwetha, add a method called display_only_args() which displays all arguments except the program name
"""

import sys


class CommandLineArgs:
    def __init__(self, args):  # constructor that takes one parameter, needs to be passed at the time of object creation
        self.args = args

    def display_all_args(self):
        print("Args count = ", len(self.args))
        print("Args value = ", self.args)

    def display_only_args(self):
        arguments = len(self.args) -1 

        position = 1
        while (arguments >= position):
            print("arguments %i: %s" % (position, self.args[position]))
            position = position +1

def main():
    # create CommandLineArgs object
    command_line_args = CommandLineArgs(sys.argv)
    command_line_args.display_all_args()
    command_line_args.display_only_args()


# call the main method
if __name__ == "__main__":
    sys.exit(main())  # calling the main method inside the sys.exit() method so that it can exit safely
