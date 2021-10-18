import sys


class ExceptionHandlingDemo:
    def __init__(self):  # this is empty constructor
        pass

    def display_list(self, mylist, index):
        print("Element at index %i is %i" % (index, mylist[index]))

    def display_list_handled_exception(self, mylist, index):
        try:
            print("Element at index %i is %i" % (index, mylist[index]))
        except IndexError:
            print("Exception occurred:")
            print(sys.exc_info())
        else:
            print("Executed successfully")
        finally:
            print("Execution completed")


def main():
    # create object
    exceptionHandleDemo = ExceptionHandlingDemo()

    # declare and initialize a list
    myList = [1, 2, 3, 4, 5, 6]

    # call display_list() method
    exceptionHandleDemo.display_list(myList, 3)  # no exception is thrown as the index is within range

    # now pass index out of range
    exceptionHandleDemo.display_list(myList, 8)
    # comment the line 48 and uncomment the line 52 to see how the exception is handled

    # call method with exception handled
    # exceptionHandleDemo.display_list_handled_exception(myList, 8)


# call the main method
if __name__ == "__main__":
    sys.exit(main())  # calling the main method inside the sys.exit() method so that it can exit safely