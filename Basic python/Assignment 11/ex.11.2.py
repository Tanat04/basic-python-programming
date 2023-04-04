def list_sum(num_list):
    if num_list < 10:
        return num_list
    else:
        return num_list%10 + list_sum(num_list//10)

print(list_sum(345))