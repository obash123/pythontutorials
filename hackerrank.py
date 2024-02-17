numbers = int(input())
s = set(map(int, input().split()))
commands = int(input())

for i in range(commands):
    action = input().split()
    met = action[0]

    try:
        if met == "remove":
            s.remove(int(action[-1]))
        elif met == "discard":
            s.discard(int(action[-1]))
        elif met == "pop" and s:
            s.pop()
    except KeyError: pass

print(sum(s))