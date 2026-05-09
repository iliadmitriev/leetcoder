#include <vector>
using std::vector;

class CustomStack {
private:
  int top, capacity;
  int *data, *inc;

public:
  CustomStack(int maxSize)
      : top(0), capacity(maxSize), data(new int[maxSize]), inc(new int[maxSize]) {}

  void push(int x) {
    if (top == capacity)
      return;

    data[top] = x;
    inc[top] = 0;
    top++;
  }

  int pop() {
    if (!top) {
      return -1;
    }

    top--;
    data[top] += inc[top];

    if (top > 0) {
      inc[top - 1] += inc[top];
    }

    return data[top];
  }

  void increment(int k, int val) {
    k = std::min(k, top) - 1;
    if (k >= 0) {
      inc[k] += val;
    }
  }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
