package algo;

import java.util.Scanner;

public class Wine {	

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] wine = new int[n];
		int[] best = new int[n];
		for (int i = 0; i < n; i++)
			wine[i] = sc.nextInt();
		if (n > 0)
			best[0] = wine[0];
		if (n > 1)
			best[1] = wine[0] + wine[1];
		if (n > 2)
			best[2] = Math.max(wine[1], wine[0] + wine[2]);
		if (n >3)
		{
			for (int i = 3; i < n; i++)
				best[i] = Math.max(Math.max(best[i-1], best[i-2] + wine[i]), best[i-3] + wine[i-1] + wine[i]);
		}
		System.out.print(best[n-1]);
	}

}
