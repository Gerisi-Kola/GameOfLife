import numpy as np

class History:
    def __init__(self,json_data):
        self.grid_size = json_data["grid_size"]
        self.history_len = json_data["history_len"]
        self.history = np.zeros((   self.history_len,
                                    self.grid_size,
                                    self.grid_size),
                                    int)
        #self.history = [0,0,0,0,0,0,0,0,0,0]
        #self.history = np.zeros((self.history_len,self.history_len), int)
        self.index = 0
    
    def history_append(self, status):
        if self.index == self.history_len:
            self.index = 0
        
        self.history[self.index] = status
        
        self.index += 1
        
        #print(self.history)
    
    def time_travel(self):
        if self.index == self.history_len:
            self.index = 0
        
        self.index -= 1
        #print(f"-self.history_len = {self.history_len}")
        #self.history[self.index-1] = 9999
        print(self.index)
        #print(self.history)
        
        return self.history[self.index]

if __name__ == "__main__":
    from json_controler import get_constant_and_limit
    json_data = get_constant_and_limit()
    h = History(json_data)
    """for i in range(20):
        h.history_append()
    print(h.history)
    print()
    h.time_travel()
    print()
    h.c = 0
    for i in range(4):
        h.history_append()
    print(h.history)
    """
    #print(h.history)
    #h.history[0] = np.zeros((10,10), int) + 1
    print(h.history)
    
    """for i in range(20):
        h.time_travel()
        h.index += 1"""
        #h.c += 1