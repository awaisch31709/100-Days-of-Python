# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# print(format_name("AnGEla", "YU"))
def format_name(f_name, l_name):

    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"Result: {formatted_f_name} {formatted_l_name}"


first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

result = format_name(first_name, last_name)

print(result)