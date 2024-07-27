# Функція жадібного алгоритму
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
    
    return result

amount = 113
greedy_result = find_coins_greedy(amount)
print("Жадібний алгоритм:", greedy_result)


# Функція динамічного програмування
def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    # dp[i] буде тримати мінімальну кількість монет для суми i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    # track[i] буде тримати номінал монети, яка була використана для dp[i]
    track = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                track[i] = coin
    
    result = {}
    i = amount
    while i > 0:
        coin = track[i]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        i -= coin
    
    return result

# Приклад використання:
amount = 113
dp_result = find_min_coins(amount)
print("Алгоритм динамічного програмування:", dp_result)

