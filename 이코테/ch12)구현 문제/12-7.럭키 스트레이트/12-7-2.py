n = input()

length = len(n) // 2 

left = sum(map(int, n[:length]))
right = sum(map(int, n[length:])) 

if left == right:
    print("LUCKY")
else:
    print("READY")
