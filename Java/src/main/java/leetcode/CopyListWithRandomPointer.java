package leetcode;

import java.util.HashMap;

public class CopyListWithRandomPointer {
    public Node copyRandomList(Node head) {
        if (head == null) return null;
        HashMap<Node, Node> nodeReference = new HashMap<>();


        Node current = head;
        while (current != null) {
            Node copied = new Node(current.val);
            nodeReference.put(current, copied);
            current = current.next;
        }

        current = head;
        while (current != null) {
            Node copied = nodeReference.get(current);
            copied.next = nodeReference.get(current.next);
            copied.random = nodeReference.get(current.random);
            current = current.next;
        }

        return nodeReference.get(head);


    }

    class Node {
        int val;
        Node next;
        Node random;

        public Node(int val) {
            this.val = val;
            this.next = null;
            this.random = null;
        }
    }
}

