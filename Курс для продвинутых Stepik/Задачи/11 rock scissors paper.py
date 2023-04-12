value_1, value_2 = input(), input()
player_1 = 'Тимур'
player_2 = 'Олег'
draw = "ничья"
values = ['камень', 'ящерица', 'Спок', 'ножницы', 'бумага']
ind_1 = values.index(value_1)
ind_2 = values.index(value_2)


def game(index_1, index_2):
    if index_1 == index_2:
        return draw
    elif (index_1 - index_2) % 2 == 0:
        return values[max(index_1, index_2)]
    else:
        return values[min(index_1, index_2)]


if game(ind_1, ind_2) == value_1:
    print(player_1)
elif game(ind_1, ind_2) == value_2:
    print(player_2)
else:
    print(game(ind_1, ind_2))
