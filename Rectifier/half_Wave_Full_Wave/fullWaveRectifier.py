import functions_rectifier

import math


secondary_voltage_fw = float(input())
load_resistance_fw = float(input())

dc_voltage_output_fw = functions_rectifier.dc_voltage(secondary_voltage_fw)
print(2 * dc_voltage_output_fw)

voltage_across_load_fw = functions_rectifier.voltage_across_load_fw(secondary_voltage_fw)
print(voltage_across_load_fw)

dc_current_hw, current_across_load_hw  = functions_rectifier.dc_current(secondary_voltage_fw, load_resistance_fw)
dc_current_hw = 2 * dc_current_hw
current_across_load_hw = math.sqrt(2) * current_across_load_hw

print(dc_current_hw)
print(current_across_load_hw)

foam_factor_fw = math.pi/(math.sqrt(2) * 2)
print(foam_factor_fw)

efficiency_rectifier_hw = (1 / foam_factor_fw) ** 2
print(efficiency_rectifier_hw)

ripple_factor_hw = math.sqrt(foam_factor_fw ** 2 - 1)
print(ripple_factor_hw)

transformer_utilization_factor_hw = 0.671
print(transformer_utilization_factor_hw)

transformer_utilization_factor_hw_bridge = 0.813
print(f"Full - wave Rectifier -- bridge - Transfomer Utilization Factor = {transformer_utilization_factor_hw}")
