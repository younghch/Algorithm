package algo;

import java.util.Arrays;
import java.util.HashSet;


public class Solution {
	public int[] solution(int[] numbers) {
        HashSet<Integer> set = new HashSet<Integer>();
        int	i;
        int j;
        int len;
        int [] ans;
        
        len = numbers.length;
        i = 0;
        while (i < len)
        {
        	j = i + 1;
        	while (j < len)
        	{
        		set.add(numbers[i] + numbers[j]);
        		j++;
        	}
        	i++;
        }
        ans = set.stream().mapToInt(Integer::intValue).toArray();
        Arrays.sort(ans);
        return ans;
    }
}
