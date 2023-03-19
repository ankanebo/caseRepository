from typing import Union
from constants import MAX_SPEED, PI
from math import sin


def calculate_varp_speed(power_to_engine: Union[int, float], ship_weight: Union[int, float]):
    v = MAX_SPEED * (power_to_engine / 80) * (200 / ship_weight)
    return v


def calculate_change_population(g0: Union[int, float], growth_factor: Union[int, float]):
    g = g0 + g0 * growth_factor
    return g


def calculate_growth_factor(temperature: Union[int, float], oxigen: Union[int, float]):
    k = sin(
        (-PI / 2) + (PI * (temperature + 0.5 * oxigen) / 40)
    )
    return k


def calculate_count_energy():
    pass
