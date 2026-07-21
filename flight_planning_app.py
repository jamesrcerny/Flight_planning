"""Flight planning app."""
import customtkinter as ctk

from flight_calculator_methods import FlightPlanningCalculator

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

alt_calc = FlightPlanningCalculator()

root = ctk.CTk()
root.title("The Flight Planning App")
root.geometry("420x520")

LABEL_FONT = ("Arial", 14)
ENTRY_FONT = ("Arial", 14)
BUTTON_FONT = ("Arial", 16)
TITLE_FONT = ("Arial", 24, "bold")

title = ctk.CTkLabel(root, text="Flight Planning App", font=TITLE_FONT)
title.pack(pady=(20, 10))

content_frame = ctk.CTkFrame(root)
content_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))


def clear_content():
    """Clears the content frame."""
    for widget in content_frame.winfo_children():
        widget.destroy()


def add_field(parent, row, label_text, placeholder, unit_text):
    """Adds a labeled entry row with a unit suffix and returns the entry widget."""
    ctk.CTkLabel(parent, text=label_text, font=LABEL_FONT).grid(
        row=row, column=0, columnspan=2, padx=20, pady=(10, 2), sticky="w")
    entry = ctk.CTkEntry(parent, placeholder_text=placeholder, font=ENTRY_FONT, width=180)
    entry.grid(row=row + 1, column=0, padx=(20, 5), pady=(0, 5), sticky="w")
    ctk.CTkLabel(parent, text=unit_text, font=LABEL_FONT).grid(
        row=row + 1, column=1, padx=(0, 20), pady=(0, 5), sticky="w")
    return entry


def show_error(parent, row, message):
    """Displays an error message, replacing any previous error."""
    for widget in parent.grid_slaves():
        if getattr(widget, "_is_error", False):
            widget.destroy()
    error_label = ctk.CTkLabel(parent, text=message, font=LABEL_FONT, text_color="red")
    error_label._is_error = True
    error_label.grid(row=row, column=0, columnspan=2, padx=20, pady=10, sticky="w")


def show_result(parent, row, message):
    """Displays a result message, replacing any previous result."""
    for widget in parent.grid_slaves():
        if getattr(widget, "_is_result", False):
            widget.destroy()
    result_label = ctk.CTkLabel(parent, text=message, font=("Arial", 16, "bold"))
    result_label._is_result = True
    result_label.grid(row=row, column=0, columnspan=2, padx=20, pady=10, sticky="w")


def calc_alt():
    """Displays the pressure/density altitude calculator."""
    clear_content()

    input_pressure = add_field(content_frame, 0, "Pressure (Hg)", "Enter pressure in Hg", "Hg")
    input_field_elevation = add_field(content_frame, 2, "Field Elevation (ftMSL)",
                                      "Enter field elevation", "ftMSL")
    input_outside_airtemp = add_field(content_frame, 4, "Outside Air Temperature (C)",
                                      "Enter air temperature", "C")

    def store_pressure_vars():
        try:
            pressure = float(input_pressure.get())
            field_elevation = float(input_field_elevation.get())
            out_air_temp = float(input_outside_airtemp.get())
        except ValueError:
            show_error(content_frame, 8, "Please enter valid numbers in all fields.")
            return

        pressure_alt, den_alt = alt_calc.calc_densty_alt(
            pressure, field_elevation, out_air_temp)
        show_result(content_frame, 8,
                    f"Pressure alt: {round(pressure_alt)} ft\nDensity alt: {round(den_alt)} ft")

    button_row = ctk.CTkFrame(content_frame, fg_color="transparent")
    button_row.grid(row=6, column=0, columnspan=2, pady=15)
    ctk.CTkButton(button_row, text="Main Menu", font=BUTTON_FONT,
                  command=main_menu).pack(side="left", padx=5)
    ctk.CTkButton(button_row, text="Calculate", font=BUTTON_FONT,
                  command=store_pressure_vars).pack(side="left", padx=5)


def calc_wind():
    """Displays the wind correction angle calculator."""
    clear_content()

    input_wind_speed = add_field(content_frame, 0, "Wind Speed (kts)",
                                 "Enter the wind speed", "kts")
    input_wind_direction = add_field(content_frame, 2, "Wind Direction (degrees)",
                                     "Enter the wind direction", "deg")
    input_true_air_speed = add_field(content_frame, 4, "True Air Speed (kts)",
                                     "Enter the true air speed", "kts")
    input_course = add_field(content_frame, 6, "Course (degrees)",
                             "Enter the course", "deg")

    def store_wind_vars():
        try:
            wind_speed = float(input_wind_speed.get())
            wind_direction = float(input_wind_direction.get())
            true_air_speed = float(input_true_air_speed.get())
            course = float(input_course.get())
        except ValueError:
            show_error(content_frame, 10, "Please enter valid numbers in all fields.")
            return

        result = alt_calc.compute_wind_angle(wind_speed, wind_direction, true_air_speed, course)
        show_result(content_frame, 10, f"Correction angle: {result} degrees")

    button_row = ctk.CTkFrame(content_frame, fg_color="transparent")
    button_row.grid(row=8, column=0, columnspan=2, pady=15)
    ctk.CTkButton(button_row, text="Main Menu", font=BUTTON_FONT,
                  command=main_menu).pack(side="left", padx=5)
    ctk.CTkButton(button_row, text="Calculate", font=BUTTON_FONT,
                  command=store_wind_vars).pack(side="left", padx=5)


def main_menu():
    """Displays the main menu options."""
    clear_content()

    ctk.CTkLabel(content_frame, text="Select an option:", font=LABEL_FONT).pack(
        anchor="w", padx=20, pady=(20, 10))

    ctk.CTkButton(content_frame, text="Pressure and Density Altitude Calculator",
                  font=BUTTON_FONT, command=calc_alt).pack(
                      fill="x", padx=20, pady=10)

    ctk.CTkButton(content_frame, text="Wind Angle Calculator",
                  font=BUTTON_FONT, command=calc_wind).pack(
                      fill="x", padx=20, pady=10)


main_menu()
root.mainloop()
