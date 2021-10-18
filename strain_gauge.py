'''
    name: Shruti Jain

    roll no.: 2020BTechCSE071

    description: python script for taking readings of Strain Gauge experiment,
    it can used for all types of configrations.
'''

# take input voltage and resistance as input from user
input_voltage = float(input("Input voltage: "))
resistance = float(input("Enter resistance: "))

# print an ordered list of bridge types
print("Bridge Types:\n1. Quarter Bridge\n2. Half Bridge\n3. Full Quarter")
# take a number as input which corresponds to a bridge type
bridge_input = input("Enter bridge type (1/ 2/ 3): ")

# a dictionary to map numbers to bridge types
bridges = { "1": "quarter", "2": "half", "3": "full" }
bridge_type = bridges[bridge_input]

# while it stays true, the program will
# keep prompting user for input
wants_readings = True

# it returns the factor based on bridge type
# the type parameter means the bridge type
def get_factor(bridge_type):
    factor = -1
    if bridge_type == "quarter":
        factor = 0.25
    elif bridge_type == "half":
        factor = 0.5
    else:
        factor = 1
    return factor

# it takes the input voltage in volts(V)
# converts it to millivolts(mV) and rounds
# it off to two decimal places
def format_output_voltage(volage):
    return round(volage * 1000, 2)

# calculate the factor like 1/4 for quarter bridge
# 1/2 for half bridge, 1 for full bridge
factor = get_factor(bridge_type)

# keep prompting the user for input of weight
# to be measured and value of Rg (ohm) and prints
# output voltage to console
while wants_readings:
    # take weight to be measured as input
    weight_to_be_measured = input("Enter weight to be measured (Kg): ")

    # if the user enters the string 'quit' as weight
    # it will stop taking readings
    if weight_to_be_measured == "quit":
        break

    # in case the user enters a numeric value, convert it
    # to float.
    weight_to_be_measured = float(weight_to_be_measured)
    # take resistance value as input
    Rg = float(input("Enter value of Rg (ohm): "))

    # calculate the value of dR as dR = Rg - R
    dR = Rg - resistance

    # find output voltage using the formula as mentioned below
    output_voltage = factor * (dR / resistance) * input_voltage
    # format the output voltage using the helper function
    output_voltage = format_output_voltage(output_voltage)
    # and finally print the output voltage which is in mV
    print("Output Voltage (mV): ", output_voltage)
