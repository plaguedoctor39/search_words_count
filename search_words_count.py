queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'питон',
    'как работать со списками питон',
    'list'
]
words = 0
sum_words = []

for word in queries:
    words += 1
    for letter in word:
        if letter == ' ':
            words += 1
        else:
            pass
    sum_words.append(words)
    words = 0

sum_words_uniq = list(set(sum_words))
print('Распределение поисковых запросов по количеству слов:')
for n in sorted(sum_words_uniq):
    if n == 1:
        print(f'\tзапрос состоящий из {n} слова: {round(sum_words.count(n) / (len(sum_words) / 100))}%')
    else:
        print(f'\tзапросов состоящих из {n} слов: {round(sum_words.count(n) / (len(sum_words) / 100))}%')
#print(sum_words)
#print(sum(sum_words))