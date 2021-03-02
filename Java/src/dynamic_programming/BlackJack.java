package dynamic_programming;

import java.io.IOException;
import java.util.Scanner;
public class BlackJack {
	public static void main(String[] args) throws IOException{
		//scan input
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		int m = scanner.nextInt();
		int[] cards = new int[n];
		
		for (int i = 0; i < n; i++)
			cards[i] = scanner.nextInt();
		
		//code starts
		int ans = 0;
		for (int i = 0; i < n; i++)
		{
			for (int j = i+1; j < n; j++)
			{
				for (int k = j + 1 ; k < n; k++)
				{
					int temp = cards[i] + cards[j] + cards[k];
					if (temp <= m && (m - temp) < (m - ans))
						ans = temp;
				}
			}
		}
		System.out.print(ans);
		
	}
}
