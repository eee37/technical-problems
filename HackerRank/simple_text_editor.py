# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
    Input: S: str, ops: List[str] 
'''

class TextEditor():
    
    def __init__(self, s=''):
        self.hist = []
        self.s = s
    
    def append(self, w:str) -> None:
        self.hist.append(self.s)
        self.s = self.s + w
        
    
    def delete(self, k:int) -> None:
        if k <= len(self.s):
            self.hist.append(self.s)
            self.s = self.s[: len(self.s) - k]
    
    def print_k(self, k:int):
        if k <= len(self.s):
            print(self.s[k-1])
    
    def undo(self) -> None:
        if self.hist:
            self.s = self.hist.pop()
        
    def process_input(self):
        # iterate over each line
        num_ops = int(input()) # NOTE: First input is just an stringified int
        
        for _ in range(num_ops):
            op = input() # NOTE: Method to grab input
            op = op.split(" ") # NOTE: Method to split string to array
            op_type = int(op[0]) # NOTE: Will be string
            if op_type == 1:
                self.append(op[1])
            elif op_type == 2:
                self.delete(int(op[1]))
            elif op_type == 3:
                self.print_k(int(op[1]))
            elif op_type == 4:
                self.undo()

te = TextEditor()
te.process_input()
        