def maximumProfit(prices):
    # Write your code here.
    mini=float('inf')
    maxi=float('-inf')
    for i in range(len(prices)):
        mini=min(mini,prices[i])
        maxi=max(maxi,prices[i]-mini)
    return maxi