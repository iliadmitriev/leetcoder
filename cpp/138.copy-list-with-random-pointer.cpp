/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == NULL) {
            return NULL;
        }
        // duplicate nodes in pairs:
        // original node 1 -> carbon copy 1 -> original node 2 -> carbon copy 2 -> ..
        Node* ptr = head;
        for (Node* ptr = head; ptr != NULL; ptr = ptr->next->next ) {
            Node* cc = new Node(ptr->val); cc->next = ptr->next;
            ptr->next = cc;
        }

        // save pointer to head of carbon copy
        Node* head_cc = head->next;

        // set pointers to `random` nodes
        for (Node* ptr = head; ptr != NULL; ptr = ptr->next->next) {
            if (ptr->random != NULL) {
                ptr->next->random = ptr->random->next;
            }
        }

        // recover original and cc lists by spliting
        for (Node* ptr = head; ptr != NULL; ptr = ptr->next) {
            // get carbon copy
            Node* cc = ptr->next;
            // split nodes (recover original nodes)
            if (ptr->next != NULL) ptr->next = ptr->next->next;
            if (cc->next != NULL) cc->next = cc->next->next;
        }

        // return saved pointer to head of carbon copy
        return head_cc;
    }
};