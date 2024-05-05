package leetcode;

import java.util.Stack;

// https://leetcode.com/problems/simplify-path
public class SimplifyPath {
    public String simplifyPath(String path) {
        String[] directories = path.split("/");
        Stack<String> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();
        for (String dir : directories) {
            switch (dir) {
                case ".", "" -> {
                }
                case ".." -> {
                    if (!stack.isEmpty())
                        stack.pop();
                }
                default -> {
                    stack.push(dir);
                }
            }
        }
        for (String dir : stack) {
            sb.append("/");
            sb.append(dir);
        }
        return sb.isEmpty() ? "/" : sb.toString();
    }
}
