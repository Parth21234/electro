def max_duty_cycle(input_max_voltage, output_voltage, n = 90):
    deno = input_max_voltage * n
    max_d = output_voltage/deno
    return max_d


def inductor_ripple_current(input_max_voltage, output_voltage, max_duty, switching_frequency, inductor_value):
    deno = switching_frequency * inductor_value #L
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

def input_Capacitor_Selection():
    """The best practice is to use low-equivalent series resistance (ESR) ceramic capacitors. The dielectric
    material must be X5R or better. Otherwise, the capacitor loses much of its capacitance due to dc bias or
    temperature."""

def output_Capacitor_Selection(del_inductor_ripple_current, switching_frequency, eSR, output_voltage):
    """The best practice is to use low-ESR capacitors to minimize the ripple on the output voltage. Ceramic
    capacitors are a good choice if the dielectric material is X5R or better.
    If the converter has external compensation, any capacitor value above the recommended minimum in the
    data sheet can be used, but the compensation has to be adjusted for the used output capacitance.
    With internally compensated converters, the recommended inductor and capacitor values must be used,
    or the recommendations in the data sheet for adjusting the output capacitors to the application in the data
    sheet must be followed for the ratio of L × C"""

    c_out = del_inductor_ripple_current /(8 * switching_frequency * output_voltage)
    del_v_out_esr = eSR * del_inductor_ripple_current
    return c_out, del_v_out_esr