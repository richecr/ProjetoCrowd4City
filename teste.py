import math

a = [0,1,2,3,4,5,6,7,8,9,10]

data = []
start = 0
end = 4
limit = len(a)
i = math.ceil(limit / 4)

for go in range(i):
    print("{}: {}".format(start, end))
    id_b = a[start:end]
    start += 4
    end += 4
    print(id_b)
