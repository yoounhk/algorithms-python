stu_no = [39, 14, 67, 105]
stu_name = ['Justin', 'Jonh', 'Mike', 'Summer']

number = 39

for i in range(len(stu_no)):
    if stu_no[i] == number:
        print(stu_name[i])
        find = True
        break
if find != True:
    print('?')
