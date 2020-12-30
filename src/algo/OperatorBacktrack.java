package algo;

import java.util.Scanner;

public class OperatorBacktrack {
	static int[] numbers;
	static int max = -1000000001;
	static int min = 1000000001;
	
	public static int cal(int i, int depth, int val)
	{
		if (i == 0)
			return (val + numbers[depth + 1]);
		if (i == 1)
			return (val - numbers[depth + 1]);
		if (i == 2)
			return (val * numbers[depth + 1]);
		else
			return (val / numbers[depth + 1]);
	}
	public static void dfs(int n, int depth, int val, int[] operators)
	{
		if (depth + 1 == n)
		{
			if (val > max)
				max = val;
			if (val < min)
				min = val;
			return ;
		}
		for (int i = 0; i < 4; i++)
		{
			if (operators[i] != 0)
			{
				operators[i] -= 1;
				dfs(n, depth + 1, cal(i, depth, val), operators);
				operators[i] += 1;
			}
		}
	}
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		numbers = new int[n];
		for (int i = 0; i < n; i++)
			numbers[i] = sc.nextInt();
		int[] operators = new int[4];
		for (int i = 0; i < 4; i++)
			operators[i] = sc.nextInt();
		// + - * %
		dfs(n, 0, numbers[0], operators);
		System.out.println(max);
		System.out.println(min);
	}
}
