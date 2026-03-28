import math

def multi_dc_output(secondary_voltage_multi_phases, phases):
    v_dc = secondary_voltage_multi_phases * (math.sin(math.pi/phases)/ math.pi * phases)
    return v_dc

def multi_load_output(secondary_voltage_multi_phases, phases):
    v_load = secondary_voltage_multi_phases * math.sqrt(0.5 * (1 + (math.sin(2 * math.pi/phases)/(2 * math.pi/phases) )))
    return v_load