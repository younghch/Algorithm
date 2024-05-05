package leetcode;

import java.util.LinkedList;
import java.util.Queue;

public class PopulatingNextRightPointerInEachNode {

    public NodeWithNext connect(NodeWithNext root) {
        NodeWithNext dummyNode = new NodeWithNext(0);
        NodeWithNext curLayerNode = root;
        NodeWithNext nextLayerNode = dummyNode;

        while (curLayerNode != null) {
            if (curLayerNode.left != null) {
                nextLayerNode.next = curLayerNode.left;
                nextLayerNode = nextLayerNode.next;
            }
            if (curLayerNode.right != null) {
                nextLayerNode.next = curLayerNode.right;
                nextLayerNode = nextLayerNode.next;
            }
            curLayerNode = curLayerNode.next;
            if (curLayerNode == null) {
                curLayerNode = dummyNode.next;
                nextLayerNode = dummyNode;
                dummyNode.next = null;
            }

        }
        return root;
    }

    public NodeWithNext connectRecursive(NodeWithNext root) {
        if (root == null) return null;
        NodeWithNext leftMost = root;
        while (leftMost != null) {
            leftMost = populateUpdateReturnLeftMost(leftMost);
        }
        return root;
    }

    NodeWithNext populateUpdateReturnLeftMost(NodeWithNext currentParentNode) {
        if (currentParentNode == null) return null;
        NodeWithNext nextParentNode = getNextNodeWithChild(currentParentNode.next);
        NodeWithNext leftChild = currentParentNode.left;
        NodeWithNext rightChild = currentParentNode.right;
        NodeWithNext leftMostChild = leftChild == null ? rightChild : leftChild;

        NodeWithNext childToUpdateNext = null;

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

    NodeWithNext getNextNodeWithChild(NodeWithNext node) {
        while (node != null) {
            if (node.left != null || node.right != null) return node;
            node = node.next;
        }
        return null;
    }

    public NodeWithNext connectWithLinkedList(NodeWithNext root) {
        if (root == null) return null;
        Queue<NodeWithNext> toVisits = new LinkedList<>();
        Queue<NodeWithNext> toUpdateNexts = new LinkedList<>();
        toVisits.add(root);
        while (!toVisits.isEmpty()) {
            for (NodeWithNext toVisit: toVisits) {
                if (toVisit.left != null) toUpdateNexts.add(toVisit.left);
                if (toVisit.right != null) toUpdateNexts.add(toVisit.right);
            }
            final NodeWithNext[] toUpdateNext = {toUpdateNexts.peek()};
            toUpdateNexts.stream().skip(1).forEach(rightNode -> {
                toUpdateNext[0].next = rightNode;
                toUpdateNext[0] = rightNode;
            });
            toVisits.clear();
            Queue<NodeWithNext> empty = toVisits;
            toVisits = toUpdateNexts;
            toUpdateNexts = empty;
        }
        return root;
    }
}
class NodeWithNext {
    public int val;
    public NodeWithNext left;
    public NodeWithNext right;
    public NodeWithNext next;

    public NodeWithNext() {}

    public NodeWithNext(int _val) {
        val = _val;
    }

    public NodeWithNext(int _val, NodeWithNext _left, NodeWithNext _right, NodeWithNext _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};