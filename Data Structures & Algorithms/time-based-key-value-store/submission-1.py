
        
class TimeMap:

    def __init__(self):
        self.time_dict: dict[str, OrderedDict] = {}
    

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_dict:
            self.time_dict.update({key: OrderedDict()})
            self.time_dict[key][timestamp]=value
        else:
            od = self.time_dict.get(key)
            od[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        print("searching for %d"%(timestamp))
        if key in self.time_dict:
            od = self.time_dict.get(key)
            items = list( od.items())
            l = 0
            
            r = len(items) - 1
            m = -1
            mid = 0

            count = 0 
            print("length : %d"%(len(items)))
            while l <= r and count < 10:
                mid = (l + r)//2
                k, v = items[mid]
                print("mid : %d, l%d, r%d"%(mid,l,r))
                if k == timestamp:
                    print("case 1 k %d timestamp %d"%(k,timestamp))
                    return v
                elif k < timestamp: # timestamp is larger: look right
                    print("case 2 k %d timestamp %d"%(k,timestamp))
                    m = mid 
                    l = mid + 1
                else :
                    r = mid - 1
                count += 1
            if m == -1: return ""
            else: return items[m][1]
        return ""