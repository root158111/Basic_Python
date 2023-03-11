from collections import deque
nums = [i for i in range(1,6)]
dq = deque(nums)
print(dq)
dq.rotate(1)
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)
dq.append(8)
print(dq)
dq.appendleft(8)
print(dq)
print(dq.count(8))
dq.reverse()
print(dq)

