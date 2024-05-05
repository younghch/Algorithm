package leetcode;

import java.util.*;

public class BinaryTreeZigzagLevelOrderTraversal {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> answer = new ArrayList<>();
        if (root == null) return answer;

        boolean rightFirst = true;
        answer.add(List.of(root.val));

        Deque<TreeNode> toVisits = new ArrayDeque<>();
        Deque<TreeNode> toNextVisits = new ArrayDeque<>();
        toVisits.add(root);
        while (!toVisits.isEmpty()) {
            TreeNode toVisit = toVisits.pop();
            if (rightFirst) {
                if (toVisit.left != null) toNextVisits.addFirst(toVisit.left);
                if (toVisit.right != null) toNextVisits.addFirst(toVisit.right);
            } else {
                if (toVisit.right != null) toNextVisits.addFirst(toVisit.right);
                if (toVisit.left != null) toNextVisits.addFirst(toVisit.left);
            }
            if (toVisits.isEmpty()) {
                if (!toNextVisits.isEmpty()) {
                    List<Integer> values = new ArrayList<>(toNextVisits.stream().map(node -> node.val).toList());
                    answer.add(values);
                }
                toVisits.clear();
                Deque<TreeNode> emptyDeque = toVisits;
                toVisits = toNextVisits;
                toNextVisits = emptyDeque;
            }
            rightFirst = !rightFirst;
        }
        return answer;
    }

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
}


