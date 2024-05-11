def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Перемістити диск з {source} на {target}: 1")
        return [("move", source, target)]
    else:
        moves = hanoi(n-1, source, auxiliary, target)
        moves.append(("move", source, target))
        print(f"Перемістити диск з {source} на {target}: {n}")
        moves.extend(hanoi(n-1, auxiliary, target, source))
        return moves

def simulate_hanoi(n):
    rods = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print(f"Початковий стан: {rods}")
    
    moves = hanoi(n, 'A', 'C', 'B')
    
    for move in moves:
        _, src, dest = move
        disk = rods[src].pop()
        rods[dest].append(disk)
        print(f"Проміжний стан: {rods}")
    
    print(f"Кінцевий стан: {rods}")

n_disks = int(input("Введіть кількість дисків: "))
simulate_hanoi(n_disks)
