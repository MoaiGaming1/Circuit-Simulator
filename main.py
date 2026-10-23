import components

volt = components.Source()
volt.potentialBegin = 5
volt.voltage = 5
volt.resistance = 2

r = components.Resistor()
r.resistance = 8

c1 = components.Connection(volt, r)
c2 = components.Connection(r, volt)

circ = components.Circuit()
circ.setCircuit([volt, r], [c1, c2])
circ.evaluate()

print(volt.voltage, volt.current, volt.resistance, volt.power, volt.potentialBegin, volt.potentialEnd)
print(r.voltage, r.current, r.resistance, r.power, r.potentialBegin, r.potentialEnd)
