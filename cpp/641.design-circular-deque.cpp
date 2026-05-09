class QueueListNode {
public:
  int value;
  QueueListNode *next, *prev;

  QueueListNode(int _value, QueueListNode *_next = nullptr,
                QueueListNode *_prev = nullptr)
      : value(_value), next(_next), prev(_prev) {}
};

class MyCircularDeque {
private:
  int maxLen;
  int count;
  QueueListNode *front, *tail;

public:
  MyCircularDeque(int k) : maxLen(k), count(0), front(nullptr), tail(nullptr) {}

  bool insertFront(int value) {
    if (isFull()) {
      return false;
    }

    QueueListNode *newNode = new QueueListNode(value, front, tail);
    if (this->isEmpty()) {
      front = tail = newNode;
    } else {
      front->prev = newNode;
      tail->next = newNode;
      front = newNode;
    }
    count++;

    return true;
  }

  bool insertLast(int value) {
    if (isFull()) {
      return false;
    }

    QueueListNode *newNode = new QueueListNode(value, front, tail);

    if (isEmpty()) {
      front = tail = newNode;
    } else {
      front->prev = newNode;
      tail->next = newNode;
      tail = newNode;
    }
    count++;

    return true;
  }

  bool deleteFront() {
    if (isEmpty()) {
      return false;
    }

    if (front == tail) {
      delete front;
      tail = front = nullptr;
    } else {
      QueueListNode *temp = front;
      front = front->next;
      front->prev = tail;
      tail->next = front;
      delete temp;
    }

    count--;

    return true;
  }

  bool deleteLast() {
    if (isEmpty()) {
      return false;
    }

    if (front == tail) {
      delete front;
      tail = front = nullptr;
    } else {
      QueueListNode *temp = tail;
      tail = tail->prev;
      tail->next = front;
      front->prev = tail;
      delete temp;
    }

    count--;

    return true;
  }

  inline int getFront() { return count ? front->value : -1; }

  inline int getRear() { return count ? tail->value : -1; }

  inline bool isEmpty() { return count == 0; }

  inline bool isFull() { return count == maxLen; }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */