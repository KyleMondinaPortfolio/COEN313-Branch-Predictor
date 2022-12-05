class Bit2Predictor:
    def __init__(self):
        self.state = "WNT"

    def update(self,actual_value):
	if (actual_value == 1):
            self.taken();
	else:
	    self.notTaken();

    def taken(self):
        if (self.state == "SNT"):
            self.state = "WNT"
        elif (self.state == "WNT"):
            self.state = "WT"
        elif (self.state == "WT"):
            self.state = "ST"
        elif (self.state == "ST"):
            self.state = "ST"

    def notTaken(self):
        if (self.state == "SNT"):
            self.state = "SNT"	
        elif (self.state == "WNT"):
            self.state = "SNT"
        elif (self.state == "WT"):
            self.state = "WNT"
        elif (self.state == "ST"):
            self.state = "WT"

    def predict(self):
        if (self.state == "SNT"):
            return 0
        elif (self.state == "WNT"):
            return 0
        elif (self.state == "WT"):
            return 1
        elif (self.state == "ST"):
            return 1
