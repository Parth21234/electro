from Rectifier.half_Wave_Full_Wave import functions_rectifier
import math

secondary_voltage_hw = float(input())
load_resistance_hw = float(input())
effective_transformative_VA_rating_hw = float(input())
dc_vol_output_hw = functions_rectifier.dc_voltage(secondary_voltage_hw)
print(dc_vol_output_hw)

vol_across_load_hw = functions_rectifier.voltage_across_load_hw(secondary_voltage_hw)
print(vol_across_load_hw)

dc_curr_hw, curr_across_load_hw = functions_rectifier.dc_current(secondary_voltage_hw, load_resistance_hw)
print(dc_curr_hw)
print(curr_across_load_hw)

foam_factor_hw = math.pi/2
print(foam_factor_hw)

efficiency_rectifier_hw = (1 / foam_factor_hw) ** 2
print(efficiency_rectifier_hw)

ripple_factor_hw = math.sqrt(foam_factor_hw ** 2 - 1)
print(ripple_factor_hw)

transformer_utilization_factor_hw = 0.323
print(transformer_utilization_factor_hw)
