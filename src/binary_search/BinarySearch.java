package binary_search;

import java.util.Arrays;
import java.util.Scanner;
public class BinarySearch {
	
	public static void is_exist(int target, int[] num, int n, StringBuilder sb)
	{
		int left;
		int right;
		int mid;
		
		left = 0;
		right = n - 1;
		mid = (left + right) / 2;
		while(true)
		{
			if (num[mid] == target)
			{
				sb.append(1).append('\n');
				return ;
			}
			else if (num[mid] > target)
				right = mid - 1;

			else if (num[mid] < target)
				left = mid + 1;
			if (right < left || left > right)
			{
				sb.append(0).append('\n');
				return ;
			}
			mid = (right + left) / 2;
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[] num = new int[n];
		for (int i = 0; i < n; i++)
			num[i] = sc.nextInt();
		
		int m = sc.nextInt();
		int[] target = new int[m];
		for (int i = 0; i < m; i++)
			target[i] = sc.nextInt();
		Arrays.sort(num);
		StringBuilder sb = new StringBuilder();
		for (int t : target)
			is_exist(t, num, n, sb);
		System.out.print(sb);
		
	}

}
