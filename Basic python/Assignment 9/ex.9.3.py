def FindSumAvg(list_x):
    sm=0
    avg=0
    for i in list_x:
        sm+=i
    avg=sm/len(list_x)
    return sm,avg

lt=[1,2,3.5,4.5,5]
sm,avg=FindSumAvg(lt)
print(f"The total sum is {sm} and the average is {avg}")
