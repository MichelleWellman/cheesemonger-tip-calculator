#=============================================================================================================================#
# Instructions:
#   1. Have Matt or a manager log in to when I work so you can see everyone's hours.
#   2. Add together everyone's hours worked from when the tips were last counted.
#   2. Make sure you DO NOT count hours worked in Mill/Longmeadow/Bottle-O or Oxbow hours. This can be annoying with buyers.
#   3. Enter the number of hours worked by each staff member in "cheesemongers_dict"
#   4. Count the total amount of money in the tip jar and enter it in "tip_jar"
#   5. Everything below the "tip_jar" line need not be touched.
#   6. Run the program - it will tell you exactly how much money to give each monger. There may be pennies left over.
#   7. Divvy up the money!
#=============================================================================================================================#

#=================================================================================================#
# Edit the following two variables!!!
# Enter the number of hours each monger worked in "cheesemongers_dict":
#   # Make sure the names are in single quotes.
#   # Make sure the numbers have commas right after them.

cheesemongers_dict = {
    'alena': 122.23,
    'graydon': 0,
    'kristen': 0,
    'michelle': 151.24,
    'ollie': 0,
    'randy': 0,
    'rua' : 136.5,
    'zoe': 111.99
}

tip_jar = 174.60

#=================================================================================================#

#=================================================================================================#
# Do not edit below this line!

def calculate_tips(cheesemongers, total_tips):
    total_hours = sum(cheesemongers.values())

    # Find the percentages of hours worked by each cheesemonger:
    for key, value in cheesemongers.items():
        cheesemongers[key] = value/total_hours

    # Calculate how much money each cheesemonger gets:
    for key, value in cheesemongers.items():
        cheesemongers[key] = value*total_tips

    return cheesemongers

# cheesemonger_tips = calculate_tips(cheesemongers_dict, tip_jar)
print(calculate_tips(cheesemongers_dict, tip_jar))