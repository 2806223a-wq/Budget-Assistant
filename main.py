from budget import BudgetAssistant

# Показываем меню программы
def show_menu():
    print("\n" + "═" * 40)
    print("      БЮДЖЕТНЫЙ ПОМОЩНИК      ")
    print("═" * 40)
    print("1. Добавить расход")
    print("2. Сумма за период")
    print("3. День с максимальным расходом")
    print("4. Сортировка категорий")
    print("5. Отменить последний расход")
    print("6. Показать дерево")
    print("7. Показать все расходы")
    print("8. Выход")
    print("═" * 40)

# Главная функция программы
def main():

    # Создаем объект программы
    app = BudgetAssistant()

    print("Добро пожаловать!")
    print("Категории: Еда, Транспорт, Жильё, Развлечения")

    # Бесконечный цикл меню
    while True:

        # Показываем меню
        show_menu()

        # Пользователь выбирает действие
        choice = input("Выберите действие (1-8): ").strip()

        if choice == "1":
            try:
                # Ввод данных о расходе
                day = int(input("День (1-31): "))
                amount = float(input("Сумма: "))
                category = input("Категория: ").strip().capitalize()

                # Добавляем расход
                app.add_expense(day, amount, category)

            except:
                print("Ошибка! Введите числа правильно")

        elif choice == "2":
            try:
                # Ввод периода
                a = int(input("День A: "))
                b = int(input("День B: "))

                # Считаем сумму за период
                app.get_sum_by_period(a, b)

            except:
                print("Ошибка!")

        elif choice == "3":
            # День с максимальным расходом
            app.find_max_expense_day()

        elif choice == "4":
            # Сортировка категорий
            app.sort_categories()

        elif choice == "5":
            # Отмена последнего расхода
            app.undo_last()

        elif choice == "6":
            # Показ дерева расходов
            app.show_tree()

        elif choice == "7":
            # Показ всех расходов
            app.show_all_expenses()

        elif choice == "8":
            # Выход из программы
            print("До свидания!")
            break

        else:
            print("Неверный выбор")

# Запуск программы
if __name__ == "__main__":
    main()