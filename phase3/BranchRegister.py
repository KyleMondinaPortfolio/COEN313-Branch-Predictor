BranchPatterns = {
    "00000":0,
    "00001":0,
    "00010":0,
    "00011":0,
    "00100":0,
    "00101":0,
    "00110":0,
    "00111":0,
    "01000":0,
    "01001":0,
    "01010":0,
    "01011":0,
    "01100":0,
    "01101":0,
    "01110":0,
    "01111":0,
    "10000":0,
    "10001":0,
    "10010":0,
    "10011":0,
    "10100":0,
    "10101":0,
    "10110":0,
    "10111":0,
    "11000":0,
    "11001":0,
    "11010":0,
    "11011":0,
    "11100":0,
    "11101":0,
    "11110":0,
    "11111":0,
}

class BranchRegister:
    def __init__(self):
       self.queue = [0,0,0,0,0]
       self.patterns = BranchPatterns
    def update(self,actual_value):
       self.patterns[self.__get_pattern()] = actual_value
       self.queue.pop()
       self.queue.insert(0,actual_value)
    def __get_pattern(self):
       s = ''.join(str(bit) for bit in self.queue)
       return s
    def predict(self):
       return self.patterns[self.__get_pattern()]



