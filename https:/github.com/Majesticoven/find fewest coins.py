def find_fewest_coins(coins, target):
    min_coin_list = [0]
    
    for x in range(target):
        min_coin_list.append(target+1)

    for index in range(len(min_coin_list)):
        for coin in coins: 
            if index-coin>=0:    
                min_coin_list[index] =(min(min_coin_list[index-coin]+1,min_coin_list[index]))
    print(min_coin_list)            
    least_coins = min_coin_list[-1]
    change_given = []
    coins.reverse()
    for x in range(min_coin_list[-1]):
        for coin in coins:
            if target - coin >= 0 and min_coin_list[target-coin] == least_coins-(x+1):
                change_given.append(coin)
                target -= coin 
        
    return change_given


print(find_fewest_coins([1,2,5,10,21,50], 63 ))

