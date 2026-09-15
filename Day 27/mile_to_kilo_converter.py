from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.60934, 2)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

# Miles Label
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

# Equals Label
is_equal_label = Label(text="Equals")
is_equal_label.grid(row=1, column=0)

# Result Label
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(row=1, column=1)

# Kilometer Label
kilometer_label = Label(text="Km")
kilometer_label.grid(row=1, column=2)

# Calculate Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()