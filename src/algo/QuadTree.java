package algo;

import java.util.Scanner;

public class QuadTree {
	static int[][] square;
	static int count_w;
	static int count_b;
	
	public static boolean check_square(int x, int y, int side)
	{
		int i = square[x][y];
		
		for (int j = 0; j < side; j++)
		{
			for (int k = 0; k < side; k++)
			{
				if (square[x + j][y + k] != i)
					return false;
			}
		}
		if (i == 0)
			count_w++;
		if (i == 1) 
			count_b++;
		return true;
	}
	
	public static void devide_four(int x, int y, int side)
	{
		if (check_square(x, y, side))
			return ;
		
		int side_s = side / 2;
		devide_four(x, y, side_s);
		devide_four(x + side_s, y, side_s);
		devide_four(x, y + side_s, side_s);
		devide_four(x + side_s, y + side_s, side_s);
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		square = new int[n][n];
		count_w = 0;
		count_b = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				square[i][j] = sc.nextInt();
		devide_four(0, 0, n);
		System.out.println(count_w);
		System.out.println(count_b);
		
	}

}
