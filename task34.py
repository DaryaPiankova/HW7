def check_for_rythm(data):
    result_list = list(map(lambda word: word.count("а"), data))
    return len(set(result_list)) == 1


my_list = input('Введите стишок: ').split()
if (check_for_rythm(my_list)):
    print('Парам пам-пам')
else:
    print('Пам парам')
