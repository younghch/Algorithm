package algo;

import java.util.Scanner;

public class Nqueen {
	
	static boolean[][] check;
	static int count = 0;
	
	public static boolean is_valid(int n, int depth, int i)
	{
		for (int j = 0; j < n; j++)
		{
			if (check[depth][j] || check[j][i])
				return false;
			
			try {
				if (check[depth - j][i - j])
					return false;
			} catch (ArrayIndexOutOfBoundsException e){}
			try {
				if (check[depth - j][i + j])
					return false;
			} catch (ArrayIndexOutOfBoundsException e){}
			try {
				if (check[depth + j][i - j])
					return false;
			} catch (ArrayIndexOutOfBoundsException e){}
			try {
				if (check[depth + j][i + j])
					return false;
			}catch (ArrayIndexOutOfBoundsException e){}
		}
		
		return true;
	}
	
	public static void dfs(int n, int depth)
	{
		if (depth == n)
		{
			count++;
			return ;
		}
		for (int i = 0; i < n; i++)
		{
			if (is_valid(n, depth, i))
			{
				check[depth][i] = true;
				dfs(n, depth+1);
				check[depth][i] = false;
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		check = new boolean[n][n];
		dfs(n,0);
		System.out.print(count);
		
	}

}
