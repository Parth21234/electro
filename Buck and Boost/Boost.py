import functions_Boost as functions
import functions_Boost

v_out = float(input())
i_out_max = float(input())
v_in_max = float(input())
switching_frequency = float(input())
efficiency = float(input())

maximum_Duty_Cycle = functions.max_duty_cycle(v_in_max, v_out, efficiency)
print(maximum_Duty_Cycle)


inductor_val = inductor_selection(v_in_max, v_out, switching_frequency, i_out_max)
print(inductor_val)

inductor_ripple_current = inductor_ripple_current(v_in_max, v_out, maximum_Duty_Cycle,
                                                 switching_frequency, inductor_val)
print(inductor_ripple_current)

app_specificMax_switch_current = inductor_ripple_current/2 + i_out_max
print(app_specificMax_switch_current)

eSR = float(input()) # Equivalent series resistance of the used output capacitor

output_Capacitor_value, output_Capacitor_voltage = output_Capacitor_Selection(inductor_ripple_current, switching_frequency, eSR, v_out)
print(output_Capacitor_value, output_Capacitor_voltage)