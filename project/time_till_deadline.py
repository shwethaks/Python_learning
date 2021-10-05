# below code gives the time remaining to reach your goal with in the given specific date



from datetime import datetime

user_input = input("enter your goal with deadline seperated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
#calculate how many days from now to deadline

time_till= deadline_date - today_date

hours_till = int(time_till.total_seconds() /60 /60)
print(f"hi user!! time remaining for your goal : {goal} is {hours_till} hours ")

#print(datetime.datetime.strptime(deadline, "%d.%m.%Y"))
#print(input_list)