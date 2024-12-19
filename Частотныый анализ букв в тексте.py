def count_letters(inc_string):
    inc_lower_string = inc_string.lower()
    char_dict = {}
    for char in inc_lower_string:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        elif char.isalpha():
            char_dict[char] = 1
    return char_dict


def calculate_frequency(test_dict):
    count_item = sum(test_dict.values())
    new_dict = {}
    for item in test_dict:
        new_dict[item] = test_dict[item] / count_item
    return new_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

dict_to_print = calculate_frequency(count_letters(main_str))
for item in dict_to_print:
    print(f"{item}: {dict_to_print[item]:.2f}")
