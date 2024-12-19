# TODO Напишите функцию для поиска индекса товара
def search_index(the_search_list, item):
    for index, current_item in enumerate(the_search_list):
        if current_item == item:
            return index   # индексы товаров начинаются с 0

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
