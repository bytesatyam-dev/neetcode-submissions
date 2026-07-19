class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            profit_that_day = prices[i] - lowest_buy_price
            lowest_buy_price = min(prices[i], lowest_buy_price)
            if profit_that_day >= 0:
                max_profit = max(profit_that_day, max_profit)

        return max_profit
