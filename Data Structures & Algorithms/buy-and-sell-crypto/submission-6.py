class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_i, buy_price = 0, prices[0]
        sell_j, sell_price = len(prices)-1, prices[-1]
        i, j = 0, len(prices)-1

        while i + 1 < sell_j or j - 1 > buy_i:
            if i + 1 < sell_j:
                i += 1
            if j - 1 > buy_i:
                j -= 1
            if prices[j] > sell_price:
                sell_j = j
                sell_price = prices[j]
            if prices[i] < buy_price and i < sell_j:
                buy_i = i
                buy_price = prices[i]
        profit = sell_price - buy_price
        return max(profit, 0)