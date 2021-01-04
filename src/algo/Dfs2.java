package algo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Dfs2 {
	
	
	public static void main(String[] args) throws IOException
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int[][] map = new int[n][m];
		for (int i = 0; i < n; i++)
		{
			String input = br.readLine();
			for (int j = 0; j < m; j++)
			{
				map[i][j] = input.charAt(j) - '0';
			}
		}
		int[][] visited = new int[n][m];
		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[]{0,0,0,0});
		int[] dx = {0, 0, -1, 1};
	    int[] dy = {-1, 1, 0, 0};
	    
		int depth = -1;
		while (!queue.isEmpty())
		{
			
			int[] cur = queue.poll();
			//System.out.printf("depth : %d, cur : (%d, %d, %d)\n", cur[3], cur[0], cur[1], cur[2]);
			if (cur[0] == n - 1 && cur[1] == m - 1)
			{
				depth = cur[3] + 1;
				break;
			}
			if (visited[cur[0]][cur[1]] == 0 || visited[cur[0]][cur[1]] == 2)
			{
				if (cur[2] == 1)
					visited[cur[0]][cur[1]] = 2;
				else
					visited[cur[0]][cur[1]] = 1;
				
				for (int i = 0; i < 4; i++)
				{
					int nx = cur[0] + dx[i];
		            int ny = cur[1] + dy[i];
		            if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
					if (map[nx][ny] == 1)	
					{
						if (cur[2] == 0)
						{
							visited[nx][ny] = 2;
							queue.add(new int[]{nx, ny, 1, cur[3] + 1});
						}
					}
					else
						queue.add(new int[] {nx, ny, cur[2], cur[3] + 1});
				}
			}
		}
		System.out.print(depth);
	}

		
		
}

