'''
#635
    LC Solution 
        Approach #1
            * Converts times to seconds. Subtracts from year 1999 to prevent overflow
            * Note to get times within a range. For end times you increment the granularity level by one to capture the actual upperbound
            * Need to specially handle month and day of month since those are 1-based rather than 0 based
        Approach # 2
            * Treemap implementation in python
                http://www.grantjenks.com/docs/sortedcontainers/
#hashmap #array #treemap
'''
from datetime import datetime

class LogSystem:

    def __init__(self):
        self.hist = []
        self.granularity_index_map = dict({ # NOTE: Py Syntax String keys need to be wrapped in quotes
            "Year": 3,
            "Month": 6,
            "Day": 9,
            "Hour": 12,
            "Minute": 15,
            "Second": 18
        })
        
        self.regex_map = dict({
            "Year": '%Y',
            "Month": '%Y:%m',
            "Day": '%Y:%m:%d',
            "Hour": '%Y:%m:%d:%H',
            "Minute": '%Y:%m:%d:%H:%M',
            "Second": '%Y:%m:%d:%H:%M:%S'
        })
        

    def put(self, id: int, timestamp: str) -> None:
        # https://stackoverflow.com/questions/5292303/how-does-tuple-comparison-work-in-python
        # heapq.heappush(self.heap, (timestamp, id) )  # NOTE: Look into how tuples are compared
        # NOTE: Can consider removing sorting here. Can improve to O(1) at no cost to retrieve
        self.hist.append((timestamp, id))
        
    def convert_string_date(self, string_date: str, regex_date: str):
        return datetime.strptime(string_date, regex_date)
    
    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        last_index_match = self.granularity_index_map[granularity]
        
        regex_date = self.regex_map[granularity]
        start = self.convert_string_date(start[:last_index_match + 1], regex_date) # NOTE: Py Syntax You can slice string just not reassing value at index cause strings are immutable. slicing just creates a new string
        end = self.convert_string_date(end[:last_index_match + 1], regex_date)
        ids_response = []
        for index, log in enumerate(self.hist):
            datetime, id  = log
            
            datetime = self.convert_string_date(datetime[: last_index_match + 1], regex_date)
            if start <= datetime and end >= datetime:
                ids_response.append(id)
        return ids_response
                
                
        
        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)