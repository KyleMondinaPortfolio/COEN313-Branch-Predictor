class Bit1Predictor:
	def __init__(self):
		self.state = "N"
	def taken(self):
		if (self.state == "T"):
			self.state = "T"
		elif (self.state == "N"):
			self.state = "T"

	def notTaken(self):
		if (self.state == "T"):
			self.state = "N"
		elif (self.state == "N"):
			self.state = "N"

	def predict(self):
		if (self.state == "T"):
			return "T"
		elif (self.state == "N"):
			return "N"
		
