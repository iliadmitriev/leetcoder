#include <iostream>

using namespace std;

class Node {
public:
  int val;
  Node *next;
  Node *prev;

  Node(int x) : val(x), next(nullptr), prev(nullptr) {}
  Node(int x, Node *n, Node *p) : val(x), next(n), prev(p) {}

  void pprint() {
    cout << val << ", ";
    if (next) {
      next->pprint();
    } else {
      cout << endl;
    }
  }
};

class MyLinkedList {
private:
  Node *head;
  Node *tail;
  int size;

  Node *getNode(int index) {
    if (index < 0 || index >= size) {
      return nullptr;
    }

    bool fromHead = index < size / 2;

    Node *cur;
    if (fromHead) {
      cur = head;
    } else {
      cur = tail;
      index = size - index - 1;
    }

    while (index-- > 0 && cur) {
      cur = fromHead ? cur->next : cur->prev;
    }

    return cur;
  }

  void addNodeBetween(Node *node, Node *prev, Node *next) {
    node->next = next;
    node->prev = prev;

    if (prev) {
      prev->next = node;
    } else {
      head = node;
    }

    if (next) {
      next->prev = node;
    } else {
      tail = node;
    }

    size++;
  }

  void deleteNode(Node *node) {
    Node *prev = node->prev;
    Node *next = node->next;

    if (prev) {
      prev->next = next;
    } else {
      head = next;
    }

    if (next) {
      next->prev = prev;
    } else {
      tail = prev;
    }

    size--;
  }

public:
  MyLinkedList() : head(nullptr), tail(nullptr), size(0) {}

  int get(int index) {
    if (index < 0 || index >= size) {
      return -1;
    }

    auto node = getNode(index);
    return node ? node->val : -1;
  }

  void addAtHead(int val) { addNodeBetween(new Node(val), nullptr, head); }

  void addAtTail(int val) { addNodeBetween(new Node(val), tail, nullptr); }

  void addAtIndex(int index, int val) {
    if (index < 0 || index > size) {
      return;
    }

    if (index == 0) {
      addAtHead(val);
      return;
    }

    if (index == size) {
      addAtTail(val);
      return;
    }

    auto pos = getNode(index);
    if (!pos) {
      return;
    }

    addNodeBetween(new Node(val), pos->prev, pos);
  }

  void deleteAtIndex(int index) {

    auto pos = getNode(index);

    if (!pos) {
      return;
    }

    deleteNode(pos);
    delete pos;
  }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */