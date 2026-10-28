class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        while r <= len(prices)-1:
            if prices[l] < prices[r]:
                if profit <= (prices[r]-prices[l]):
                    profit = prices[r]-prices[l]
            if prices[l] > prices[r]:
                l = r
            r +=1
            
            print(f"PROFIT {profit},\nLEFT: {l},\nRIGHT:{r}")
        return profit