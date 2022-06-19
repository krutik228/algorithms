a = input()
b = input()
cost = 0
for i in range(max(len(b), len(a))):
    try:
        if a[i] == b[i]:
            continue
        elif a[i] != b[i]:
            cost += 1
    except:
        cost += abs(len(a) - len(b))
        break
print(cost)

