# importing necessary modules
from constants import *
import math
import random
import time

#main heating/cooling function
def heating_cooling(t):
    global Q_ambient, Q_occupants, T, Q_hvac

    T_ambient, Q_ambient = ambient_temp(t)
    N, Q_occupants = probabilities_Nocc(t)

    if t == 300:
        x = T
    else:
        x = temp_change_equation(t - dt, Q_hvac, Q_ambient, Q_occupants)

    if x > T_high:
        Q_hvac = -Q_max
    elif x < T_low:
        Q_hvac = Q_max
    else:
        Q_hvac = 0

    T = temp_change_equation(t, Q_hvac, Q_ambient, Q_occupants)
    temp_change_list.append(T)

    return T, Q_hvac, N

#calculate ambient temperature according to set of rules
def ambient_temp(t):
    global T

    if 0 <= t < 21600:
        T_ambient = 15
    elif 21600 <= t < 43200:
        start, end = 21600, 43200
        T_start, T_end = 15, 32

        progress = (t - start)/(end - start)

        T_ambient = T_start + progress*(T_end - T_start)
    elif 43200 <= t < 57600:
        T_ambient = 32
    else:
        start, end = 57600, 86400
        T_start, T_end = 32, 15

        progress = (t - start)/(end - start)

        T_ambient = T_start + progress*(T_end - T_start)

    Q_ambient = (T_ambient - T)/R
    return T_ambient, Q_ambient

#randomly define probabilities based on few rules
def probabilities_Nocc(t):
    if 0 <= t < 28800:
        N = random.randint(0,2)
    elif 28800 <= t < 36000:
        N = random.randint(1,5)
    elif 36000 <= t < 57600:
        N = random.randint(5,10)
    elif 57600 <= t < 68400:
        N = random.randint(1,4)
    elif 68400 <= t < 86400:
        N = random.randint(0,2)

    Q_occupants = N*Q_occ
    return N, Q_occupants

#calculate power consumed in a single time frame dt
def power_consumed(mode):
    if mode != "Idle":
        return abs(Q_hvac)/COP
    return 0

#decide mode of hvac system used
def mode_hvac(Q_hvac):
    if Q_hvac < 0:
        return "Cooling"
    elif Q_hvac > 0:
        return "Heating"
    else:
        return "Idle"

#convert seconds to 24hrs clock format for report
def time_24hr(t):
    hours=t//3600
    minute=(t%3600)//60

    if hours<1:
        hours=0
    if minute<1:
        minute=0

    return f"{hours:02}{minute:02}hrs"

# defining core equation
def temp_change_equation(t, Q_hvac, Q_ambient, Q_occupants):
    return (temp_change_list[-1] + dt*(Q_hvac + Q_ambient + Q_occupants)/C)
