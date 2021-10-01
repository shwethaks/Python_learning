calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    condition_check =num_of_days >0
    print(type(condition_check))
    """check positive or negetive days"""
    print(num_of_days > 0) # used to check the boolean condition, we do have a function called "type" which will check the type of value
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days *calculation_to_units} {name_of_unit}"
    elif num_of_days == 0:
        return "please enter number above 0"
    else:
        return "you entered a negetive value"

def validate_and_execute():
    if user_input.isdigit():
        #user_input = input("hey user , please enter number of days\n")
        user_input_number = int(user_input)
        calculated_value = days_to_units(user_input_number)
        print(calculated_value)
        
    else:
        print("your input is not a valid one")

user_input = input("hey user , please enter number of days\n")
validate_and_execute()