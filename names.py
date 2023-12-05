def cal_mean(data):
    total_sum = 0
    
    for i in data:
        total_sum = i + total_sum
        
    n = len(data)

    mean = total_sum/n
    return (total_sum , mean)

ages = [4,3,7,6,5,2,8]
x = cal_mean(ages)

print(x)

#list numbers between (1,10)
for i in range (5,12):
    print(i)