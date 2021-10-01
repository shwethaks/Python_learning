calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days *calculation_to_units} {name_of_unit}"

my_var =days_to_units(10)
print(my_var)