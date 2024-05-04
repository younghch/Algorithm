package leetcode;

// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
public class TwoSumII {
    public int[] twoSum(int[] numbers, int target) {
        int[] answer = new int[2];
        int frontPointer = 0;
        int rearPointer = numbers.length - 1;
        int sum = numbers[frontPointer] + numbers[rearPointer];

        while (target != sum) {
            if (sum < target) frontPointer++;
            else rearPointer--;
            sum = numbers[frontPointer] + numbers[rearPointer];
        }

        answer[0] = frontPointer + 1;
        answer[1] = rearPointer + 1;
        return answer;
    }
}
