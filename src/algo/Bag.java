package algo;
import java.util.Scanner;

public class Bag {
	public static int max(int a, int b)
	{
		if (a > b)
			return (a);
		return (b);
	}
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		
		int[] w = new int[n+1];
		int[] v = new int[n+1];
		
		for (int i = 1; i <= n; i++)
		{
			w[i] = sc.nextInt();
			v[i] = sc.nextInt();
		}
		int[][] dp = new int[n + 1][k+1];
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= k; j++)
			{
				if (j - w[i] >= 0)
					dp[i][j] = max(dp[i-1][j], dp[i - 1][j - w[i]] + v[i]);
				else
					dp[i][j] = dp[i-1][j];
			}
		}
		System.out.println(dp[n][k]);
	}
}
