class NumPattern:
    maxValue = 0      # tracks initial value in pattern
    pattern = []   # tracks pattern
    results = []      # stores results 

    # logic for creating pattern
    def create_pattern(self, num1, num2):
        # maxValue initially 0
        if num1 == self.maxValue:
            self.add_value(int(num1))
        # maxValue reassigned to first paramater on first call
        elif num1 > self.maxValue:
            self.maxValue = num1
            self.add_value(int(num1))
            self.create_pattern(int(num1 - num2), int(num2))
        # result list contains no value equal or less than zero
        elif num1 > 0 and (self.contains_zero(self.pattern) != True):
            self.add_value(int(num1))
            self.create_pattern(int(num1 - num2), int(num2))
        # result contains result less than zero, count up
        elif num1 > 0 and (self.contains_zero(self.pattern) == True):
            self.add_value(int(num1))
            self.create_pattern(int(num1 + num2), int(num2))
        # reached minimum limit
        elif num1 <= 0 and (self.contains_zero(self.pattern) != True):
            self.add_value(int(0))
            self.create_pattern(int(num1 + num2), int(num2))  
        return self
    
    # builds and stores patterns
    def build_pattern(self, num1, num2):
        self.create_pattern(num1, num2)
        self.store_results()
        self.clear_pattern()
        return self
        
    # append to pattern
    def add_value(self, num):
        self.pattern.append(num)
        return self
        
    # print each value in pattern    
    def get_pattern(self):
        for value in self.results:
            print(value)
        return self
            
    # clear pattern
    def clear_pattern(self):
        self.pattern = []
        self.maxValue = 0
        return self
        
    # store pattern to results
    def store_results(self):
        self.results.append(self.pattern)
        return self
        
    # check for value <= 0 in pattern
    def contains_zero(self, nums):
        result = False
        for x in self.pattern:
            if x <= 0:
                result = True
                continue
        return result


def main():
    numPattern = NumPattern()   
    numPattern.build_pattern(20, 4)
    numPattern.create_pattern(5, 1).store_results().clear_pattern().get_pattern()

if __name__ == "__main__":
    main()
            
