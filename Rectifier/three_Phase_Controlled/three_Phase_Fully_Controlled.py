import functions_three_phase_Fully_Controlled as f3p

secondary_voltage_fully_controlled = float(input())
firing_angle = float(input())

voltage_dc_three_phase_fully_controlled = (
    f3p.voltage_3_phase_fully_controlled(secondary_voltage_fully_controlled, firing_angle))
print(voltage_dc_three_phase_fully_controlled)

