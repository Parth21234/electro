import functions_Multi_Phase as fmp

secondary_voltage_multi_phases = float(input())
phases = int(input())

voltage_dc = fmp.multi_dc_output(secondary_voltage_multi_phases, phases)
print(voltage_dc)

voltage_load = fmp.multi_load_output(secondary_voltage_multi_phases, phases)
print(voltage_load)


foam_factor_multi_phases = voltage_load/voltage_dc
print(foam_factor_multi_phases)