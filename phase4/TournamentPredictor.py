class TournamentPredictor:
    def __init__(self):
        self.state = "WBP"

    def SR(self):
        if (self.state == "SBP"):
            self.state = "WBP"
        elif (self.state == "WBP"):
            self.state = "WSR"
        elif (self.state == "WSR"):
            self.state = "SSR"
        elif (self.state == "SSR"):
            self.state = "SSR"

    def BP(self):
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