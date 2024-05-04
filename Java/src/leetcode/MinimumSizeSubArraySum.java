package leetcode;

// https://leetcode.com/problems/minimum-size-subarray-sum
public class MinimumSizeSubArraySum {
    public int minSubArrayLen(int target, int[] nums) {
        int len = nums.length;
        int left = 0;
        int right = 0;
        int sum = nums[0];

        int answer = Integer.MAX_VALUE;
        while (right < len) {
            if (sum >= target) {
                answer = Math.min(answer, right - left);
                sum -= nums[left++];
            } else if (right == len - 1) {
                break;
            } else {
                sum += nums[++right];
            }
        }
        return answer == Integer.MAX_VALUE ? 0 : answer + 1;
    }
}
