word = input() + ' запретил букву'

literals = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к',
            'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
            'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

counter = 0

def collect(w_set):
    ready_line = ""
    for i in range(len(w_set)):
        ready_line += w_set[i]
    return ready_line.strip()


word_list = list(word)
while collect(word_list) != '':
    if literals[counter] in word_list:
        print(collect(word_list).replace("  "," "), literals[counter])
        while literals[counter] in word_list:
            word_list.remove(literals[counter])
            # print(word_list)
    counter += 1




