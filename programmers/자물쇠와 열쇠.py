def solution(key, lock):
    key_map = []
    lock_map = []
    for y in range(len(key)):
        for x in range(len(key)):
            if key[y][x] == 1:
                key_map.append((y, x))
            if lock[y][x] == 0:
                lock_map.append((y, x))

    if not lock_map: True

    for _ in range(4):
        for i in range(len(key_map)):
            key_map[i] = turn(key_map[i], len(key))
        for y in range(len(key)+len(lock)):
            for x in range(len(key)+len(lock)):
                if set(transfer(key_map, (y, x))) >= set(lock_map):
                    return True
    return False


def turn(path, size):
    return (path[1], size-1-path[0])


def transfer(pathes, to_move):
    result = []
    for path in pathes:
        result.append((path[0]+to_move[0], path[1]+to_move[1]))
    return result
