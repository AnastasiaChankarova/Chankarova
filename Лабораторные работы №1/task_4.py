
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

statistik = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
statistik["Общее количество"] = len(users)
statistik["Уникальные посещения"] = len(set(users))

print(statistik)



