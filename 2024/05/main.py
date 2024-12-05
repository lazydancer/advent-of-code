
def is_correct(update, order_rules):
    for a, b in order_rules:
        if a in update and b in update:
            idx_a = update.index(a)
            idx_b = update.index(b)
            if idx_a > idx_b:
                return False
    return True


def part_1():
    with open('input', 'r') as f:
        content = f.read()

    order_rules_part, updates_part = content.strip().split('\n\n')
    order_rules = [line.strip().split('|') for line in order_rules_part.strip().split('\n')]
    updates = [line.strip().split(',') for line in updates_part.strip().split('\n')]

    result = 0
    for update in updates:
        if is_correct(update, order_rules):
            result += int(update[len(update) // 2])

    print(result)


def order(update, order_rules):
    while True:
        swapped = False
        for a, b in order_rules:
            if a in update and b in update:
                idx_a = update.index(a)
                idx_b = update.index(b)
                if idx_a > idx_b:
                    update[idx_a], update[idx_b] = update[idx_b], update[idx_a]
                    swapped = True
        if not swapped:
            break
    return update


def part_2():
    with open('input', 'r') as f:
        content = f.read()

    order_rules_part, updates_part = content.strip().split('\n\n')
    order_rules = [line.strip().split('|') for line in order_rules_part.strip().split('\n')]
    updates = [line.strip().split(',') for line in updates_part.strip().split('\n')]

    incorrect_updates = []
    for update in updates:
        if not is_correct(update, order_rules):
            incorrect_updates.append(update)

    result = 0
    for incorrect_update in incorrect_updates:
        fixed_update = order(incorrect_update, order_rules)
        result += int(fixed_update[len(fixed_update) // 2])

    print(result)


part_1()
part_2()