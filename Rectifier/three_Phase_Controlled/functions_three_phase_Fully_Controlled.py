import math

def voltage_3_phase_fully_controlled(secondary_voltage_fully_controlled, firing_angle):
    vol_dc_fully_controlled_o = secondary_voltage_fully_controlled * 3 * math.sqrt(3)/math.pi

    if 0<= firing_angle <= 60:
        vol_3_phase_f_controlled = vol_dc_fully_controlled_o * math.cos(firing_angle)


    elif 60 < firing_angle <= 120:
        vol_3_phase_f_controlled = vol_dc_fully_controlled_o * (1+ math.cos(firing_angle + math.pi/3))

    else:
        print("The firing angle must be between 0 and 120")
