from bisect import bisect_left, bisect_right

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

result = [3, 2, 4, 1, 0]


array = [[] for _ in range(10001)]
reverse_array = [[] for _ in range(10001)]


def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    return right_index - left_index


def solution(words, queries):
    answer = []

    for word in words:
        array[len(word)].append(word)
        reverse_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reverse_array[i].sort()

    for q in queries:
        if q[0] == "?":
            print(q, q[::-1].replace("?", "a"), q[::-1].replace("?", "z"))
            res = count_by_range(
                reverse_array[len(q)], q[::-1].replace("?", "a"), q[::-1].replace("?", "z")
            )
            print(res)
        else:
            res = count_by_range(array[len(q)], q.replace("?", "a"), q.replace("?", "z"))

        answer.append(res)

    return answer


solution(words, queries)
