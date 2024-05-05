package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

// https://leetcode.com/problems/merge-intervals
public class MergeIntervals {
    public int[][] merge(int[][] intervals) {
        List<int[]> answer = new ArrayList<>();
        Arrays.sort(intervals, Comparator.comparingInt(interval -> interval[0]));
        int[] before = intervals[0];
        for (int[] cur : intervals) {
            if (before[1] >= cur[0]) {
                if (before[1] < cur[1]) {
                    before[1] = cur[1];
                }
            } else {
                answer.add(before);
                before = cur;
            }
        }
        if (answer.size() == 0 || answer.get(answer.size() - 1) != before) answer.add(before);
        return answer.toArray(int[][]::new);
    }
}
