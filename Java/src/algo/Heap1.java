package algo;

import java.util.Scanner;
import java.util.PriorityQueue;
import java.util.Collections;
public class Heap1 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		PriorityQueue<Integer> Maxpq = new PriorityQueue<Integer>(Collections.reverseOrder());
		PriorityQueue<Integer> Minpq = new PriorityQueue<Integer>();
		StringBuilder sb = new StringBuilder();
		
		int Max_size = 1;
		int Min_size = 0;
		Maxpq.add(sc.nextInt());
		sb.append(Maxpq.peek()).append('\n');
		for (int i = 1; i < n; i++)
		{
			if (Max_size > Min_size)
			{
				Minpq.add(sc.nextInt());
				Min_size++;
			}
			else
			{
				Maxpq.add(sc.nextInt());
				Max_size++;
			}
			if (Min_size != 0 && Maxpq.peek() > Minpq.peek())
			{
				int temp = Maxpq.poll();
				Maxpq.offer(Minpq.poll());
				Minpq.offer(temp);
			}
			sb.append(Maxpq.peek()).append('\n');
		}
		System.out.print(sb);
	}

}
