
        
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
            res = ""
            mid = 0
            count = 0 

            while l <= r and count < 10:
                mid = (l + r)//2
                k, v = items[mid]
                if k == timestamp:
                    return v
                elif k < timestamp: # timestamp is larger: look right
                    res = v
                    l = mid + 1
                else :
                    r = mid - 1
                count += 1
            return res
        return ""