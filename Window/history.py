class History:
    def __init__(self):
        self.history = [0,0,0,0,0,0,0,0,0,0]
        self.history_len = 10
        self.index = 0
        self.c = 0
    
    def history_append(self):
        if self.index == self.history_len:
            self.index = 0
        
        self.history[self.index] = self.c
        
        self.index += 1
        self.c += 1
        
        #print(self.history)
    
    def time_travel(self):
        if self.index == self.history_len:
            self.index = 0
        #print(f"-self.history_len = {self.history_len}")
        #self.history[self.index-1] = 9999
        print(self.index-1)
        #print(self.history)
        
        return self.history[self.index-1]

if __name__ == "__main__":
    h = History()
    for i in range(20):
        h.history_append()
    print(h.history)
    print()
    h.time_travel()
    print()
    h.c = 0
    for i in range(4):
        h.history_append()
    print(h.history)
    
    """for i in range(20):
        h.time_travel()
        h.index += 1"""
        #h.c += 1