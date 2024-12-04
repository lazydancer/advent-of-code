def part_1():
    with open('input', 'r') as f:
        word_search = [list(line.strip()) for line in f]

    word = 'XMAS'

    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
        (0, -1),
        (-1, 0),
        (-1, -1),
        (-1, 1)
    ]


    rows = len(word_search)
    cols = len(word_search[0])

    def check_word(x, y, dx, dy):
        for k in range(len(word)):
            nx, ny = x + k * dx, y + k * dy
            if not (0 <= nx < rows and 0 <= ny < cols):
                return False
            if word_search[nx][ny] != word[k]:
                return False
        return True 


    count = 0
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_word(i, j, dx, dy):
                    count += 1

    print(count)



def part_2():
    with open('input', 'r') as f:
        word_search = [list(line.strip()) for line in f]

    diagonal_words = {'MAS', 'SAM'}

    count = 0

    rows = len(word_search)
    cols = len(word_search[0])

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            diag1 = word_search[i-1][j-1] + word_search[i][j] + word_search[i+1][j+1]
            diag2 = word_search[i-1][j+1] + word_search[i][j] + word_search[i+1][j-1]


            if diag1 in diagonal_words and diag2 in diagonal_words:
                count += 1


    print(count)


part_1()
part_2()