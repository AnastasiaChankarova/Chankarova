money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
while True:
    ostat = spend - salary
    if ostat > money_capital:
        break

    month += 1
    money_capital -= ostat
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", month)
