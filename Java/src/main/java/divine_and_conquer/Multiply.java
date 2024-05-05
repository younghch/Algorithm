package divine_and_conquer;

import java.util.Scanner;
public class Multiply {
	
	public static int power(int x, int pow, int div)
	{
		long temp;
		
		if (pow == 0)
			return (1);
		else if (pow == 1)
			return (x % div);
		else if (pow % 2 == 0)
		{
			temp = power(x, pow / 2, div);
			return (int) (temp * temp % div);
		}
		else
		{
			temp = power(x, pow / 2, div);
			return (int) ((temp * temp % div) * x % div);
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		
		long temp;
		temp = power(a, b, c);
		System.out.print(temp);

	}

}
