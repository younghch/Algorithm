package leetcode;

import java.util.LinkedList;
import java.util.Queue;

public class PopulatingNextRightPointerInEachNode {

    public Node connectRecursive(Node root) {
        if (root == null) return null;
        Node leftMost = root;
        while (leftMost != null) {
            leftMost = populateUpdateReturnLeftMost(leftMost);
        }
        return root;
    }

    Node populateUpdateReturnLeftMost(Node currentParentNode) {
        if (currentParentNode == null) return null;
        Node nextParentNode = getNextNodeWithChild(currentParentNode.next);
        Node leftChild = currentParentNode.left;
        Node rightChild = currentParentNode.right;
        Node leftMostChild = leftChild == null ? rightChild : leftChild;

        Node childToUpdateNext = null;

        if (rightChild != null) {
            if (leftChild != null) leftChild.next = rightChild;
            childToUpdateNext = rightChild;
        } else if (leftChild != null) {
            childToUpdateNext = leftChild;
        }

        if (nextParentNode == null) {
            return leftMostChild;
        } else if (childToUpdateNext != null) {
            childToUpdateNext.next = nextParentNode.left == null ? nextParentNode.right : nextParentNode.left;
            populateUpdateReturnLeftMost(nextParentNode);
            return leftMostChild;
        } else {
            return populateUpdateReturnLeftMost(nextParentNode);
        }
    }

    Node getNextNodeWithChild(Node node) {
        while (node != null) {
            if (node.left != null || node.right != null) return node;
            node = node.next;
        }
        return null;
    }

    public Node connectWithLinkedList(Node root) {
        if (root == null) return null;
        Queue<Node> toVisits = new LinkedList<>();
        Queue<Node> toUpdateNexts = new LinkedList<>();
        toVisits.add(root);
        while (!toVisits.isEmpty()) {
            for (Node toVisit: toVisits) {
                if (toVisit.left != null) toUpdateNexts.add(toVisit.left);
                if (toVisit.right != null) toUpdateNexts.add(toVisit.right);
            }
            final Node[] toUpdateNext = {toUpdateNexts.peek()};
            toUpdateNexts.stream().skip(1).forEach(rightNode -> {
                toUpdateNext[0].next = rightNode;
                toUpdateNext[0] = rightNode;
            });
            toVisits.clear();
            Queue<Node> empty = toVisits;
            toVisits = toUpdateNexts;
            toUpdateNexts = empty;
        }
        return root;
    }
}
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};