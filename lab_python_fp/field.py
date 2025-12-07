goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]

def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) == 1:
            yield item[args[0]]
        else:
            yield {key: item[key] for key in args}

if __name__ == "__main__":
    print(list(field(goods, 'title')))
    print(list(field(goods, 'title', 'price')))
    