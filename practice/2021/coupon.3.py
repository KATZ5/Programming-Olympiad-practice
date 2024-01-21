n, k = map(int, input().split())
candy_amount1 = n
candy_amount2 = 0
no_of_coupons = n 
y = 0

while no_of_coupons >= k:
    candy_amount2 = no_of_coupons // k
    no_of_coupons = candy_amount2 + no_of_coupons % k
    y = y + candy_amount2


candy_amount = y + candy_amount1
print(candy_amount)
