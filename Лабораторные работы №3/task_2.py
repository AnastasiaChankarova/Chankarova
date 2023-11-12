participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
def find_common_participants(participants1, participants2, zn= ","):
    participants_list1 = participants1.split(zn)
    participants_list2 = participants2.split(zn)
    all_participants = list(set(participants_list1).intersection(participants_list2))
    all_participants.sort()

    return all_participants
# TODO Провеьте работу функции с разделителем отличным от запятой

participants = find_common_participants(participants_first_group, participants_second_group)
print("Список общих участников:", participants)
