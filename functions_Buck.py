def max_duty_cycle(input_max_voltage, output_voltage, n = 90):
    deno = input_max_voltage * n
    max_d = output_voltage/deno
    return max_d


def inductor_ripple_current(input_max_voltage, output_voltage, n = 90):