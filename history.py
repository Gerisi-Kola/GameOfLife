import numpy as np

class History:
    def __init__(self,json_data):
        self.grid_size = json_data["grid_size"]
        self.max_history_len = json_data["history_len"]
        self.history = np.zeros((   self.max_history_len,
                                    self.grid_size,
                                    self.grid_size),
                                    int)
        self.index = -1
        self.undo_len, self.redo_len = 0,0
        self.previous_status = None
    
    def history_append(self, status):
        if not np.array_equal(self.previous_status,status):
            #on evite les IndexError
            if self.index == self.max_history_len-1:
                self.index = -1
            self.index += 1
            #on evite de bouclé dans l'historique
            if self.undo_len <= self.max_history_len:
                self.undo_len += 1
            self.redo_len = 0
            
            self.history[self.index] = status
            #print(self.index)
            
            #on vérifie à ne pas remplir l'historique avec le meme état
            self.previous_status = status.copy()
    
    
    def time_travel(self):
        if self.undo_len > 0 :
            self.undo_len -= 1
            self.redo_len += 1
            
            if self.index == -self.max_history_len-1:
                self.index = 0
            
            self.index -= 1
            print(self.index)
            
            return self.history[self.index]
        else:
            print("end of index")
            return self.history[self.index]
    
    def redo_time_travel(self):
        if self.redo_len > 1:
            self.undo_len += 1
            self.redo_len -= 1
            
            if self.index == self.max_history_len:
                self.index = 0
            
            self.index += 1
            print(self.index)
            
            return self.history[self.index]
        else:
            print("end of redo index")
            return self.history[self.index]

if __name__ == "__main__":
    from json_controler import get_constant_and_limit
    json_data = get_constant_and_limit()
    h = History(json_data)
    
    print(h.history)