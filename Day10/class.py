# Functions with Inputs
# def format_name(f_name, l_name):
#      return f"{f_name.title()} {l_name.title()}"

# formated_string = format_name("anGela", "yu")
# print(formated_string)

# Functions with Multiple Return Values
# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     return f"{f_name.title()} {l_name.title()}"

# formated_string = format_name(input("What is your first name? "), input("What is your last name? "))
# print(f"Hello, {formated_string}!")

def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if year % 4 != 0:
        return False
    else:
        if year % 100 != 0:
            return True
        else:
            if year % 400 == 0:
                return True
            else:
                return False
                
print(is_leap_year(2400))
