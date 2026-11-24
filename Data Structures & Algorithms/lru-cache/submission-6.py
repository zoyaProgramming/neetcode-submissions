class LRUCache:
    
    def __init__(self, capacity: int):  
        self.capacity = capacity
        self.dictionary = {}
        self.lru = OrderedDict()

    def get(self, key: int) -> int:
        if self.lru.get(key) == None:
            return -1
        else :
            k = self.lru[key]
            self.lru.move_to_end(key)
            return k
        

    def put(self, key: int, value: int) -> None:
        if self.lru.get(key) is None:
            if len(self.lru) == self.capacity:
                k, v = self.lru.popitem(last=False)
                print("popping k : %d to put %d" %(k, key))
                self.lru[key] = value

                self.lru.move_to_end(key, last=True)

                self.lru.update({key:value})
            else:
                self.lru[key] = value
                self.lru.move_to_end(key, last=True)
             #   self.dictionary.update({key: value})
            
        else:
            
            self.lru[key] = value
            self.lru.move_to_end(key, last=True)
        #    self.dictionary.update({key: value})

                

        
