"""Pressure altitude calculator."""

import math


class FlightPlanningCalculator():
    """
    Docstring for FlightPlanningCalculator
    """

    def calc_densty_alt(self, pressure, field_elevation, out_air_temp):
        """
        Docstring for calc_press_alt
        
        :param self: Description
        """
        pressure_altitude = 1000 * (29.92 - pressure) + field_elevation
        
        international_standard_temperature = 15 - 1.98 *(pressure_altitude / 1000)
        density_altitude = pressure_altitude + 120 * (out_air_temp
                                               - international_standard_temperature)
        return pressure_altitude, density_altitude
    def compute_wind_angle(self, wind_speed, wind_direction, true_air_speed, course):
        """
        Docstring for compute_wind_angle
        
        :param self: Description
        """
     
        # Degrees to radians conversion
        wind_angle_degrees = course - wind_direction
        wind_angle_radians = math.radians(wind_angle_degrees)

        # Correction angle calculation
        correction_angle = math.atan2(
            wind_speed * math.sin(wind_angle_radians), true_air_speed)
        correction_angle_degrees = math.degrees(correction_angle)

        # Conversion from radians to degrees
        correction_angle_degrees = math.degrees(correction_angle)
        
        # Bring into 0–360 range
        correction_angle_degrees = correction_angle_degrees % 360

        # Convert to -180–+180 range
        if correction_angle_degrees > 180:
            correction_angle_degrees -= 360
        return round(correction_angle_degrees)
            