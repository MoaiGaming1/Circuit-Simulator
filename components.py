import time


class Component:
	def __init__(self):
		self.voltage = 0
		self.current = 0
		self.resistance = 0
		self.power = 0
		self.potentialBegin = 0
		self.potentialEnd = 0
		self.connections = []
		self.isVoltageConstant = False

	def evaluate(self):
		if not self.isVoltageConstant:
			self.voltage = self.current * self.resistance
		self.potentialEnd = self.potentialBegin - self.voltage
		self.power = self.voltage * self.current



class Connection:
	def __init__(self, c1:Component, c2:Component):
		self.c1 = None
		self.c2 = None
		self.evalId = 0

		if c1:
			self.c1 = c1
			c1.connections.append(self)
		if c2:
			self.c2 = c2
			c2.connections.append(self)

	def evaluate(self, eId:int):
		if self.evalId == eId: return
		self.evalId = eId
		if not self.c1 or not self.c2: return
		if not self.c2.isVoltageConstant:
			self.c2.potentialBegin = self.c1.potentialEnd
		self.c2.evaluate()



class Circuit:
	def __init__(self):
		self.components = []
		self.connections = []
		self.resistance = 0
		self.current = 0
		self.voltage = 0

	def evaluate(self, evalId:int = time.time_ns(), secondPass = False):
		self.resistance = 0
		self.voltage = 0
		for c in self.connections:
			c.c1.evaluate()
			c.evaluate(evalId)
		for c in self.components:
			self.resistance += c.resistance
			if c.isVoltageConstant: self.voltage += c.voltage
		if self.resistance > 0:
			self.current = self.voltage / self.resistance
		else:
			self.current = 0
		for c in self.components:
			c.current = self.current
		if not secondPass: self.evaluate(evalId, True)


	def setCircuit(self, components, connections):
		self.components = components
		self.connections = connections


class Wire(Component):
	def __init__(self):
		super().__init__()
		self.length = 0
		self.resistancePerMeter = 52.7/1000

	def evaluate(self):
		self.resistance = self.length * self.resistancePerMeter



class Resistor(Component):
	def __init__(self):
		super().__init__()



class Source(Component):
	def __init__(self):
		super().__init__()
		self.isVoltageConstant = True
