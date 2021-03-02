package bfs_dfs;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Bfs1 {

	static boolean[] visited;
	static int		 count = 0;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int v = sc.nextInt();
		int e = sc.nextInt();
		visited = new boolean[v + 1];
		
		ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>(v + 1);
		graph.add(null);
		for(int i = 1; i <= v; i++)
			graph.add(i, new ArrayList<Integer>());
		for (int i = 0 ; i < e; i ++)
		{
			int com1 = sc.nextInt();
			int com2 = sc.nextInt();
			graph.get(com1).add(com2);
			graph.get(com2).add(com1);
		}
		
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.add(1);
		while (!queue.isEmpty())
		{
			int cur = queue.poll();
			System.out.println(cur);
			for (int next : graph.get(cur))
			{
				
				if (visited[next] == true)
					continue ;
				visited[next] = true;
				count++;
				queue.add(next);
			}
		}
		System.out.print(count);
	}
}
