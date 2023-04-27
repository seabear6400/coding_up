a, b = map(int, input().split())

print("True" if (a and not b) or (not a and b) else "False")#둘이 서로 다르면 True 둘이 같다면 False가 나오는 함수이다.
