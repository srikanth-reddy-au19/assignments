nums = list(map(int, input("Enter data: ").split()))

def spy_game(nums):
    x=[]
    for i in nums:
        if i == 0:
            x.append(i)
        elif i==7:
            x.append(i)
        else:
            None
    return x == [0,0,7]
print(spy_game(nums))