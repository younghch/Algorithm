package leetcode;

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
public class BestTimeToBuyAndSellStockII {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int buy = prices[0];

        for (int i = 1; i < prices.length; i++) {
            int cur = prices[i];
            int next = i == prices.length - 1 ? 0 : prices[i + 1];

            if (cur < buy && cur < next) buy = cur;
            if (cur > buy && cur > next) {
                profit += cur - buy;
                buy = next;
            }
        }
        return profit;
    }

    public int maxProfitBetter(int[] prices) {
        int profit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1])
                profit += prices[i] - prices[i - 1];
        }
        return profit;
    }
}
