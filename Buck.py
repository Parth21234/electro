"""
///OUTLOOK///

    ~ Basic Calculation of a Buck Converter's Power Stage.

        -> Necessary Parameters of the Power Stage.
             -? Input voltage range: VIN(min) and VIN(max) >> viM and voM
             -? Nominal output voltage: VOUT >> v0
             -? Maximum output current: IOUT(max) >> i_0_Max
             -? Integrated circuit used to build the buck converter. This is necessary because some parameters for the
                calculations must be derived from the data sheet.

        -> Calculate the Maximum Swtich Current
             The first step to calculate the switch current is to determine the duty cycle, D, for the maximum input
             voltage. The maximum input voltage is used because this leads to the maximum switch current.

                    Maximum Duty Cycle : D = v0/(viM * N)
                    N = efficiency of the converter (Estimated 90%)


            The next step in calculating the Maximum Swtich Current is to find the Inductor Ripple Current

                    Inductor Ripple Current : del_i_L = (viM - v0) * D/(fs * L)

                    viM = maximum input voltage
                    v0 = desired output voltage
                    fs = minimum switching frequency of the converter
                    L = selected inductor Value
            It now has to be determined if the selected IC can deliver the maximum output current.

                    Max Output Current of the selected IC : i_0_Max = i_Lim_min - del_i_L/2

                    i_Lim_min = minimum value of the current limit of the integrated switch (given in the data sheet)
                    del_i_L = inductor ripple current calculated

            If the calculated value for the maximum output current of the selected IC, IMAXOUT, is below the system's
            required maximum output current, the switching frequency has to be increased to reduce the ripple current
            or another IC with a higher switch current limit has to be used.

            Only if the calculated value for IMAXOUT is just a little smaller than the needed one, it is possible to use the
            selected IC with an inductor with higher inductance if it is still in the recommended range. A higher
            inductance reduces the ripple current and therefore increases the maximum output current with the
            selected IC.
            If the calculated value is above the maximum output current of the application, the maximum switch
            current in the system is calculated:

                    Application specific maximum switch current : i_sw_max = i_0_Max + del_i_L/2
"""

import functions_Buck as functions
from functions_Buck import inductor_ripple_current, inductor_selection

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

