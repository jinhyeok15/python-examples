def solution(key, lock):
    key_map = []
    lock_map = []
    extra_lock_map = []
    for y in range(len(key)):
        for x in range(len(key)):
            if key[y][x] == 1:
                key_map.append((y, x))
    for y in range(len(lock)):
        for x in range(len(lock)):
            if lock[y][x] == 0:
                lock_map.append((y, x))
            else:
                extra_lock_map.append((y, x))

    if not lock_map: True
    extended_lock_map = transfer(lock_map, (len(key), len(key)))
    extended_extra_lock_map = transfer(extra_lock_map, (len(key), len(key)))
    for _ in range(4):
        for i in range(len(key_map)):
            key_map[i] = turn(key_map[i], len(key))
        for y in range(len(key)+len(lock)):
            for x in range(len(key)+len(lock)):
                transfered_key_map = transfer(key_map, (y, x))
                set_t, set_e, set_ee = set(transfered_key_map), set(extended_lock_map), set(extended_extra_lock_map)
                if set_t >= set_e:
                    if (set_t-set_e) & set_ee: continue
                    else: return True
    return False


def turn(path, size):
    return (path[1], size-1-path[0])


def transfer(pathes, to_move):
    result = []
    for path in pathes:
        result.append((path[0]+to_move[0], path[1]+to_move[1]))
    return result


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
