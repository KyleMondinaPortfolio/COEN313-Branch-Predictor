class Bit3Predictor:
	def __init__(self):
		self.state = "WN3"
	def taken(self):
		if (self.state == "SN"):
			self.state = "WN1"
		elif (self.state == "WN1"):
			self.state = "WN2"
		elif (self.state == "WN2"):
			self.state = "WN3"
		elif (self.state == "WN3"):
			self.state = "WT1"
		elif (self.state == "WT1"):
			self.state = "WT2"
		elif (self.state == "WT2"):
			self.state = "WT3"
		elif (self.state == "WT3"):
			self.state = "ST"
		elif (self.state == "ST"):
			self.state = "ST"

	def notTaken(self):
		if (self.state == "SN"):
			self.state = "SN"
		elif (self.state == "WN1"):
			self.state = "SN"
		elif (self.state == "WN2"):
			self.state = "WN1"
		elif (self.state == "WN3"):
			self.state = "WN2"
		elif (self.state == "WT1"):
			self.state = "WN3"
		elif (self.state == "WT2"):
			self.state = "WT1"
		elif (self.state == "WT3"):
			self.state = "WT2"
		elif (self.state == "ST"):
			self.state = "WT3"

	def predict(self):
		if (self.state == "SN"):
			return "N"
		elif (self.state == "WN1"):
			return "N"
		elif (self.state == "WN2"):
			return "N"
		elif (self.state == "WN3"):
			return "N"
		elif (self.state == "WT1"):
			return "T"
		elif (self.state == "WT2"):
			return "T"
		elif (self.state == "WT3"):
			return "T"
		elif (self.state == "ST"):
			return "T"

