import math

def dc_voltage(secondary_voltage):
    dc_voltage_out = secondary_voltage / math.pi
    return dc_voltage_out

def voltage_across_load_hw(secondary_voltage):
    voltage_across_load = secondary_voltage / 2
    return voltage_across_load

def voltage_across_load_fw(secondary_voltage):
    voltage_across_load = secondary_voltage / math.sqrt(2)
    return voltage_across_load

def dc_current(secondary_voltage, load_resistance):
    dc_current = secondary_voltage / (load_resistance * math.pi)
    current_across_load = secondary_voltage / (load_resistance * 2)
    return dc_current, current_across_load
