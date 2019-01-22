t = int(input())

for i in range(t):
    dict_word, number_phrase = map(int, input().split())
    ans = ['NO'] * dict_word
    phrases = []
    words = list(map(str, input().split()))
    for j in range(number_phrase):
        number_words_and_phrase = input().split()
        phrases += number_words_and_phrase[1:]
    for word in words:
        if word in phrases:
            ans[words.index(word)] = 'YES'
    print(*ans)
