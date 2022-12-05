from FiveBitBranchRegister import FiveBitBranchRegister
from bit2Predictor import Bit2Predictor

class TournamentPredictor:
    def __init__(self):
        self.state = "WBP"
	self.shift_register = FiveBitBranchRegister(); 
	self.bit_predictor = Bit2Predictor();

    def predict(self):
	if (self.state == "SBP" or self.state == "WBP"):
	    return self.bit_predictor.predict()
	else:
	    return self.shift_register.predict()

    def update(self,actual_value):
	bool sr_correct = acutal_value == self.shift_register.predict()
	bool bp_correct = acutal_value == self.bit_predictor.predict()
	
	#update the two predictors
	self.shift_register.update(actual_value);
	self.branch_predictor.update(actual_value);

	if (sr_correct == bp_correct):
	    #do notthing
            return
	if (sr_correct and !bp_correct):
	    self.skew_to_SR()
	    return
	if (!sr_correct and bp_correct):
	    self.skew_to_BP()
            return
		

    def skew_to_SR(self):
        if (self.state == "SBP"):
            self.state = "WBP"
        elif (self.state == "WBP"):
            self.state = "WSR"
        elif (self.state == "WSR"):
            self.state = "SSR"
        elif (self.state == "SSR"):
            self.state = "SSR"

    def skew_to_BP(self):
        if (self.state == "SBP"):
            self.state = "SBP"	
        elif (self.state == "WBP"):
            self.state = "SBP"
        elif (self.state == "WSR"):
            self.state = "WBP"
        elif (self.state == "SSR"):
            self.state = "WSR"

    def display(self):
        if (self.state == "SBP"):
            return "BP"
        elif (self.state == "WBP"):
            return "BP"
        elif (self.state == "WSR"):
            return "SR"
        elif (self.state == "SSR"):
            return "SR"
