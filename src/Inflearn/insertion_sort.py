list = [5,3,2,31,6,4,8]
sorted_ = [list.pop(0)]
while list:
    poped = list.pop(0)
    print(sorted_)
    for i in range(len(sorted_)):
        if poped < sorted_[i]:
            sorted_.insert(i, poped)
            print(sorted_)
            break
        if i == len(sorted_) - 1:
            sorted_.append(poped)
            print(sorted_)
            break