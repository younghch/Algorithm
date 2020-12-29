package algo;

import java.util.Scanner;

public class BackTrack1 {
	static boolean[] check;//N
	static int[] ans;//M
	
	public static void dfs(int N, int M, int depth)
	{
		if (depth == M)
		{
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < M - 1; i++)
				sb.append(ans[i]).append(" ");
			sb.append(ans[M-1]);
			System.out.println(sb);
			return ;
		}
		for (int i = 0; i < N; i++)
		{
			if (check[i])
				continue;
			check[i] = true;
			ans[depth] = i + 1;
			dfs(N, M, depth + 1);
			check[i] = false;
		}
	}
	public static void main(String[] args)
	{
		Scanner scanner = new Scanner(System.in);
		
		int N = scanner.nextInt();
		int	M = scanner.nextInt();
		
		check = new boolean[N];
		ans = new int[M];
		dfs(N, M, 0);
		
	}
}
