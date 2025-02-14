# ⭐⭐⭐⭐⭐
# 어려운 문제

from bisect import bisect_left, bisect_right

def cnt_range(arr, left_value, right_value):
    left_index = bisect_left(arr, left_value)
    right_index = bisect_right(arr, right_value)
    return right_index - left_index

def solution(words, queries):
    word_length = {} 
    reversed_word_length = {}  #💡???o와 같은거는 뒤집어서 o???으로 구해야하기에 reverse도 저장해둠

    for word in words:
        length = len(word)
        if length not in word_length:
            word_length[length] = []
            reversed_word_length[length] = []
        word_length[length].append(word)
        reversed_word_length[length].append(word[::-1])


    for length in word_length:
        word_length[length].sort()
        reversed_word_length[length].sort()

    answer = []

    for query in queries:
        length = len(query)
        if length not in word_length:
            answer.append(0)
            continue

        if query[0] == "?":  # 접두사에 ?가 있는 경우 (뒤집어서 처리)
            query = query[::-1]
            target_list = reversed_word_length[length]
        else:
            target_list = word_length[length]

        # ?를 a와 z로 바꿔서 범위를 구함
        left_query = query.replace("?", "a")
        right_query = query.replace("?", "z")

        answer.append(cnt_range(target_list, left_query, right_query))

    return answer



words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))