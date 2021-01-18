package binary_search;

import java.util.Scanner;

public class BInarySearch2 {
	
	public static void binary_search(int left, int right, int mid, int k, int n)
	{
		long count = 0;
		
		for (int i = 1; i <= mid; i++)
			count += Math.min(n, mid / i);
		if (count < k)
			left = mid + 1;
		else
			right = mid - 1;
		if (left > right)
		{
			System.out.print(mid);
			return ; 
		}
		binary_search(left, right, (left + right) / 2, k, n);
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		
		binary_search(1, k, k/2, k, n);
	}

}
