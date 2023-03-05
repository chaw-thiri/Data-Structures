def nonConstructibleChange(coins):
    TotalCheckedCoins = 0
    coins.sort()
    for coin in coins:
      if TotalCheckedCoins+1 < coin: # in this example, the currently checked coin is 7 and the remaining coin is 22, so 8 cannot be created.
        return TotalCheckedCoins+1
      TotalCheckedCoins += coin

    return TotalCheckedCoins+1

array = [1,1,2,3,22]
print(nonConstructibleChange(array))