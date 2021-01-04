package algo;

import java.util.ArrayList;
import java.util.Scanner;

public class Dfs1 {
	
	static boolean[] visited;
	static int count = 0;
	
	public static void dfs(int v, ArrayList<ArrayList<Integer>> graph)
	{
		if (visited[v] == true)
			return ;
		visited[v] = true;
		count++;
		for (int next : graph.get(v))
			dfs(next, graph);
	}
	
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
		dfs(1, graph);
		System.out.print(count - 1);
	}

}
