def format_name(f_name, l_name):
    """""
    A docstring is a note/documentation written inside a function, usually right below the def line.
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



