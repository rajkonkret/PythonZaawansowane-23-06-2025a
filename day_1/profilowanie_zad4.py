import cProfile
import random


def slow_search(data, target):
    for x in data:
        if x > target:
            return x

    return None


def fast_search(data, target):
    # szuka binarnie, zakłada posortowane dane
    left, right = 0, len(data) - 1
    result = None
    while left <= right:
        mid = (left + right) // 2  # dzielenie bez reszty
        if data[mid] > target:
            result = data[mid]
            right = mid - 1
        else:
            left = mid + 1
    return result


# def main():
#     size = 1_000_000
#     data = sorted(random.randint(0, size * 2) for _ in range(size))
#     target = size // 2
#
#     slow = slow_search(data, target)
#     fast = fast_search(data, target)
#     print(f"Slow: {slow}, Fast: {fast}")


def main():
    global fast, slow
    size = 1_000_000
    data = sorted(random.randint(0, size * 2) for _ in range(size))
    targets = [random.randint(0, size * 2) for _ in range(100)]

    for target in targets:
        slow = slow_search(data, target)
        fast = fast_search(data, target)

    print(f"Slow: {slow}, Fast: {fast}")


if __name__ == '__main__':
    cProfile.run('main()')
