var MinStackNode = /** @class */ (function () {
    function MinStackNode(val, min) {
        this.val = val;
        this.min = min;
    }
    return MinStackNode;
}());
var MinStack = /** @class */ (function () {
    function MinStack() {
        this.stack = [];
    }
    MinStack.prototype.push = function (val) {
        this.stack.push(new MinStackNode(val, this.min));
        if (typeof (this.min) !== 'undefined') {
            if (val < this.min) {
                this.min = val;
            }
        }
        else {
            this.min = val;
        }
    };
    MinStack.prototype.pop = function () {
        if (this.stack.length) {
            var toBeDeleted = this.stack[this.stack.length - 1];
            if (this.min === toBeDeleted.val) {
                this.min = toBeDeleted.min;
            }
            this.stack.pop();
        }
    };
    MinStack.prototype.top = function () {
        return this.stack.length ? this.stack[this.stack.length - 1].val : null;
    };
    MinStack.prototype.getMin = function () {
        return this.min ? this.min : null;
    };
    return MinStack;
}());
/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
 const minStack = new MinStack()
 minStack.push(-2)
 minStack.push(0)
 minStack.push(-3)
 console.log(minStack.getMin())  // return -3
 minStack.pop()
 console.log(minStack.top()) // return 0# getting (<class 'TypeError'>, TypeError("'Node' object is not callable"), <traceback object at 0x1029b6988>) here
 console.log(minStack.getMin())  // return -2
