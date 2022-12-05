class Bit2Predictor:
    def __init__(self):
        self.state = "WNT"

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
            return "N"
        elif (self.state == "WNT"):
            return "N"
        elif (self.state == "WT"):
            return "T"
        elif (self.state == "ST"):
            return "T"
