def hanoi_towers(n, source, temp, target):
    if n > 0:
        hanoi_towers(n - 1, source, target, temp)
        big_disk = source.pop()
        target.append(big_disk)
        #print(hanoi_game) # Allows to see the thinking of the recursive fairy step by step
        hanoi_towers(n - 1, temp, source, target)
        return hanoi_game


source = [4,3, 2, 1]
temp = []
target = []

n = len(source)

hanoi_game = (source, temp, target)
print(hanoi_game)

print(hanoi_towers(n, source, temp, target))
