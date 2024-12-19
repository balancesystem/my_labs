def find_common_participants(first_group, second_group, separ = ","):
    first_list = set(first_group.split(separ))
    second_list = set(second_group.split(separ))
    result_intersection = list(first_list.intersection(second_list))
    result_intersection.sort()
    return result_intersection

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, separ="|"))