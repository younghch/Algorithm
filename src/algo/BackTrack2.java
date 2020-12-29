package algo;

import java.util.Scanner;

public class BackTrack2 {
	
	public static boolean[] check;
	public static int[] ans;
	public static StringBuilder sb = new StringBuilder();
	public static void dfs(int N, int M, int idx, int depth)
	{
		if (depth == M)
		{
			for (int j = 0; j < M - 1; j++)
				sb.append(ans[j]).append(' ');
			sb.append(ans[M - 1]).append('\n');
			return ;
		}
		for (int j = idx; j < N; j ++)
		{
			if (check[j])
				continue;
			check[j] = true;
			ans[depth] = j + 1;
			dfs(N, M, j + 1, depth + 1);
			check[j] = false;
		}
	}
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		int m = scanner.nextInt();
		scanner.close();
		check = new boolean[n];
		ans = new int[m];
		dfs(n, m, 0, 0);
		System.out.print(sb);

	}

}
