/*
    Could have instead used vanilla object  {val: number, min: number} w/o creating class
    cant run using ts-node bc of MODULE_NOT_FOUND error

*/

class MinStackNode{
    val: number
    min: number
    constructor(val: number, min: number) {
        this.val = val;
        this.min = min;
    }
}

class MinStack {
    stack: Array<MinStackNode> // NOTE: Stack is array of tuples
    min: number

    constructor() {
        this.stack = []
    }

    

    push(val: number): void {
        this.stack.push(new MinStackNode(val, this.min))
        if (typeof(this.min) !== 'undefined') {
            if (val < this.min) 
            {
                this.min = val
            }
        } else {
            this.min = val
        }
    }

    pop(): void {
        if (this.stack.length) {
            const toBeDeleted = this.stack[this.stack.length - 1]
            if (this.min === toBeDeleted.val) 
            {
                this.min = toBeDeleted.min
            }
            this.stack.pop()
        }

    }

    top(): number {
        return this.stack.length ? this.stack[this.stack.length - 1].val : null
    }

    getMin(): number {
        return this.min ? this.min : null
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
//  const minStack = new MinStack()
//  minStack.push(-2)
//  minStack.push(0)
//  minStack.push(-3)
//  console.log(minStack.getMin())  // return -3
//  minStack.pop()
//  console.log(minStack.top()) // return 0# getting (<class 'TypeError'>, TypeError("'Node' object is not callable"), <traceback object at 0x1029b6988>) here
//  console.log(minStack.getMin())  // return -2