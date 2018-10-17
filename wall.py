def solution(H):
    block_count = 0
    stack = []

    for height in H:
        while stack and stack[-1] > height:
            stack.pop()

        if stack and stack[-1] == height:
            continue
        elif not stack or stack[-1] < height:
            stack.append(height)
            block_count += 1
    return block_count


if __name__ == '__main__':
    H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
    print(solution(H))
