class LRUCache:
    
    def __init__(self, capacity: int):  
        self.capacity = capacity
        self.dictionary = {}
        self.lru = OrderedDict()

    def get(self, key: int) -> int:
        if self.dictionary.get(key) == None:
            return -1
        else :
            k = self.dictionary[key]
            self.lru.move_to_end(key)
            return k
        

    def put(self, key: int, value: int) -> None:
        if self.dictionary.get(key) is None:
            if len(self.dictionary) == self.capacity:
                k, v = self.lru.popitem(last=False)
                print("popping k : %d to put %d" %(k, key))
                self.lru[key] = 1

                self.lru.move_to_end(key, last=True)
                print("popped" , self.dictionary.pop(k))

                self.dictionary.update({key:value})
            else:
                self.lru[key] = 1
                self.lru.move_to_end(key, last=True)
                self.dictionary.update({key: value})
            
        else:
            
            self.lru[key] = 1
            self.lru.move_to_end(key, last=True)
            self.dictionary.update({key: value})

                

        
