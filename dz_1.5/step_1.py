proceed = int(input("Выручка: "))
outlay = int(input("Ввести затраты: "))
if proceed > outlay:
    profitability = proceed-outlay
    rent = profitability/proceed
    print(f"Отличная работа,фирма отработала с прибылью.Есть {profitability} рентабельность")
    worker = int(input("Сколько людей работает на фирме: "))
    print(f"{profitability/worker} прибыль для одного сотрудника")
elif proceed == outlay:
    print("Не плохо")
else:
    print("Удачи")