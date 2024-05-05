package algo;

import java.util.Scanner;
import java.util.Collections;
import java.util.ArrayList;
public class Sort1 {
	
	public static void main(String[] args)
	{
		Scanner scanner = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		int len = scanner.nextInt();
		ArrayList<Integer> ans = new ArrayList<>();
		for (int i = 0; i < len ; i++)
		{
			ans.add(scanner.nextInt());
		}
		scanner.close();
		Collections.sort(ans);
		
		for (int i : ans)
			sb.append(i).append('\n');
		System.out.println(sb);
	}
}
