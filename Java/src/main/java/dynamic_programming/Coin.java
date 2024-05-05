package dynamic_programming;

import java.util.Arrays;
import java.util.Scanner;

public class Coin {
	
	
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int sum = sc.nextInt();
		int[] coins = new int[n + 1];
		int[] ways = new int[sum + 1];
		for (int i = 1; i <= n; i++)
			coins[i] = sc.nextInt();
		ways[0] = 1;
		for (int c = 1; c <= n; c++)
		{
			for (int k = coins[c]; k <= sum; k++)
				ways[k] += ways[k - coins[c]];
		}
		System.out.print(ways[sum]);
	}
}
