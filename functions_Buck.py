def max_duty_cycle(input_max_voltage, output_voltage, n = 90):
    deno = input_max_voltage * n
    max_d = output_voltage/deno
    return max_d


def inductor_ripple_current(input_max_voltage, output_voltage, max_duty, switching_frequency, inductor_value):
    deno = switching_frequency * inductor_value#L
    del_inductor_ripple_current = ((input_max_voltage - output_voltage) * max_duty)/deno
    return del_inductor_ripple_current

def inductor_selection(input_max_voltage, output_voltage, switching_frequency, i_out_max):
    deno = i_out_max * 0.3 * switching_frequency * input_max_voltage
    inductor_value = output_voltage * (input_max_voltage - output_voltage)/deno
    return inductor_value

def rectifier_diode_selection(output_voltage, switching_frequency, i_out_max, max_duty):
    forward_current = i_out_max * (1 - max_duty)

    power_of_dissipation = forward_current * 0.7  # Assuming, it is silicon diode.
    return power_of_dissipation, forward_current

def out_voltage_setting(i_forward):
    i_r1_r2 = 100 * i_forward
    """The current through the resistive divider needs to be at least 100 times as big as the feedback bias current"""

