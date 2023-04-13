def find_combinations(n):
    def backtrack(combination, last_positions, count, total, result):
        if count == 2*total:
            result.append(combination[:])
            return

        for num in range(1, total+1):
            if num in last_positions:
                last_pos = last_positions[num]
                if count - last_pos >= n:
                    combination[count] = num
                    last_positions[num] = count
                    backtrack(combination, last_positions, count+1, total, result)
                    last_positions[num] = last_pos
            else:
                combination[count] = num
                last_positions[num] = count
                backtrack(combination, last_positions, count+1, total, result)
                del last_positions[num]

    result = []
    combination = [0] * (2*n)
    last_positions = {}
    backtrack(combination, last_positions, 0, n, result)
    return result


print(find_combinations(4))