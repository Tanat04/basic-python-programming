num_list = [2, 3, 15, 0, 2, 3, 0, 7, 4, 0]
product = 1

for num in num_list:
    if num == 0:
        if num_list.index(num_list[num]) == len(num_list)-1:
            continue
        else:
            num_list = num_list[num_list.index(num)+1:]
            pos0 = num_list.index(0)
            for i in range(0,pos0):
                if num_list[i] % 2 ==1:
                    product *= num_list[i]
            num_list = num_list[pos0+1:]
    if num != 0 and 0<num<9:
        product *= num
        
print(product)
print(num_list)