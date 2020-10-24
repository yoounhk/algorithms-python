str = 'ba'

isPalindrome = True
for i in range(len(str) // 2):
    if str[i] != str[len(str) - 1 - i]:
        isPalindrome = False
        break

print("회문임") if isPalindrome else print("회문아님")
