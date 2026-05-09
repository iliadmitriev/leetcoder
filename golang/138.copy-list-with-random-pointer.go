/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
    if head == nil {
        return nil
    }

    // duplicate nodes in pairs:
    // 'node 1' -> 'carbon copy 1' -> 'original node 2' -> 'carbon copy 2' -> ..
    for ptr := head; ptr != nil; ptr = ptr.Next.Next {
        // make a carbon copy
        cc := &Node{Val: ptr.Val, Next: ptr.Next}
        // set original pointer to copy
        ptr.Next = cc
    }

    // save pointer to head of carbon copy
    head_cc := head.Next

    // set pointers to `random` nodes
    for ptr := head; ptr != nil; ptr = ptr.Next.Next {
        if ptr.Random != nil {
            ptr.Next.Random = ptr.Random.Next
        }
    }

    // recover original and carbon copy lists
    for ptr := head; ptr != nil; ptr = ptr.Next {
        // get carbon copy
        cc := ptr.Next
        // split nodes (recover original pointer)
        if ptr.Next != nil { ptr.Next = ptr.Next.Next }
        if cc.Next != nil { cc.Next = cc.Next.Next }
    }

    // return saved pointer to head of carbon copy
    return head_cc  
}