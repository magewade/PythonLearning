def print_products(*args):
    products = []
    for product in args:
        if type(product) == str and product != "":
            products.append(product)

    if len(products) == 0:
        print("Нет продуктов")
    else:
        count = 1
        for i in products:
            print(f"{count}) {i}")
            count += 1




print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)