# def f(): 
#     print(s)
   
# # Global scope
# s = "I love Geeksforgeeks"
# f()
import sys

# WORKS
def g():
    s = "I love Geeksforgeeks"
    def f(): 
        print(s)
    f()

g()


def g():
    s = "I love Geeksforgeeks"
    def f(): 
        print(s) # NOTE: "s" is not defined
        s = 'No  I dont'
    f()

g()



# Note: You can unpack arrays
x = [[1,2]]
for a,b in x:
    print(f'{a} {b}')

# def find_in_order_successor(self, inputNode):
#     if self.root is None:
#         return None

#     result = 1

#     def dfs(n): # NOTE: If not passed in result and inputNode are out of scope
#         if n is None:
#             return
#         print(result) # NOTE: Compile. Can only ref global var if it is not re-assigned inside fxn o.w local reference takea precedence. If you try to useit prior to reassignment in nested fxn you could get an error due to var not being assigned yet
#         if n == 1:
#             return n
#         return

#     dfs(self.root)

#     return result if result.key != sys.maxsize else None # should return 11. Getting AttributeError