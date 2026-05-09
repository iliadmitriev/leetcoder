class MyQueue {
private:
    stack<int> input;
    stack<int> output;

    // fill output from input, O(n)
    // move all from input to output stack if output stack is empty
    void _move() {
        // 
        if (!output.empty()) {
            return;
        }

        while (!input.empty()) {
            int x = input.top(); input.pop();
            output.push(x);
        }
    }

public:
    MyQueue(): input(), output() {}
    
    // O(1)
    void push(int x) {
        input.push(x);
    }
    
    // O(1) if output is not empty
    // O(n) if output is empty (n operations to fill output from input)
    int pop() {
        _move();
        int x = output.top(); output.pop();
        return x;
    }
    
    // O(1) if output is not empty
    // O(n) if output is empty (n operations to fill output from input)
    int peek() {
        _move();
        return output.top();
    }
    
    bool empty() {
        return input.empty() && output.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */