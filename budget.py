from tree import TreeNode, add_expense_to_tree, print_tree

# Основной класс программы
class BudgetAssistant:

    def __init__(self):

        # Создаем корень дерева
        self.root = TreeNode("Июнь")

        # Список категорий расходов
        self.categories = ["Еда", "Транспорт", "Жильё", "Развлечения"]

        # Добавляем категории в дерево
        for cat in self.categories:
            self.root.children.append(TreeNode(cat))

        # Расходы по дням месяца
        self.daily_expenses = [0] * 32

        # Массив префиксных сумм
        self.prefix_sums = [0] * 32

        # Список всех расходов
        self.all_expenses = []

        # Стек для отмены последнего действия
        self.undo_stack = []

    # Обновляем префиксные суммы
    def update_prefix_sums(self):

        for i in range(1, 32):
            self.prefix_sums[i] = self.prefix_sums[i - 1] + self.daily_expenses[i]

    # Добавляем новый расход
    def add_expense(self, day, amount, category):

        # Проверяем день
        if day < 1 or day > 31:
            print("Ошибка: день должен быть от 1 до 31")
            return False

        # Проверяем сумму
        if amount <= 0:
            print("Ошибка: сумма должна быть больше 0")
            return False

        # Проверяем категорию
        if category not in self.categories:
            print("Ошибка: нет такой категории")
            return False

        # Сохраняем расход для отмены
        self.undo_stack.append((day, amount, category))

        # Добавляем расход в дерево
        add_expense_to_tree(self.root, category, amount)

        # Добавляем сумму в нужный день
        self.daily_expenses[day] += amount

        # Сохраняем расход в общий список
        self.all_expenses.append((day, amount, category))

        # Пересчитываем префиксные суммы
        self.update_prefix_sums()

        print(f"Добавлено: день {day}, {category}, {amount} руб.")
        return True

    # Отменяем последний добавленный расход
    def undo_last(self):

        # Если стек пустой
        if not self.undo_stack:
            print("Нечего отменять")
            return False

        # Берем последний расход
        day, amount, category = self.undo_stack.pop()

        # Убираем сумму из нужного дня
        self.daily_expenses[day] -= amount

        # Удаляем расход из списка
        for i in range(len(self.all_expenses) - 1, -1, -1):
            if self.all_expenses[i] == (day, amount, category):
                self.all_expenses.pop(i)
                break

        # Пересчитываем суммы
        self.update_prefix_sums()

        print(f"Отменено: день {day}, {category}, {amount} руб.")
        return True

    # Считаем расходы за период
    def get_sum_by_period(self, day_a, day_b):

        # Проверяем правильность периода
        if day_a < 1 or day_b > 31 or day_a > day_b:
            print("Ошибка: неверный период")
            return 0

        # Получаем сумму за выбранные дни
        result = self.prefix_sums[day_b] - self.prefix_sums[day_a - 1]

        print(f"Сумма за дни {day_a}-{day_b}: {result} руб.")
        return result

    # Ищем день с самым большим расходом
    def find_max_expense_day(self):

        # Если расходов нет
        if not self.all_expenses:
            print("Нет расходов")
            return None

        # Храним сумму расходов для каждого дня
        day_total = [0] * 32

        # Считаем расходы по дням
        for day, amount, _ in self.all_expenses:
            day_total[day] += amount

        # Считаем первый день максимальным
        max_day = 1
        max_amount = day_total[1]

        # Ищем максимальную сумму
        for day in range(2, 32):
            if day_total[day] > max_amount:
                max_amount = day_total[day]
                max_day = day

        print(f"День с максимальным расходом: {max_day}, сумма: {max_amount} руб.")
        return max_day

    # Сортируем категории по сумме расходов
    def sort_categories(self):

        # Словарь для хранения сумм по категориям
        cat_total = {}

        # Для каждой категории ставим 0
        for cat in self.categories:
            cat_total[cat] = 0

        # Считаем суммы по категориям
        for _, amount, category in self.all_expenses:
            cat_total[category] += amount

        # Создаем список для сортировки
        cat_list = []

        # Добавляем категории с расходами
        for cat in self.categories:
            if cat_total[cat] > 0:
                cat_list.append([cat, cat_total[cat]])

        # Сортировка вставками
        for i in range(1, len(cat_list)):
            key_cat, key_sum = cat_list[i]
            j = i - 1

            while j >= 0 and cat_list[j][1] < key_sum:
                cat_list[j + 1] = cat_list[j]
                j = j - 1

            cat_list[j + 1] = [key_cat, key_sum]

        print("\nКатегории по сумме трат (от больших к малым):")

        # Выводим результат
        for cat, total in cat_list:
            print(f"  {cat}: {total} руб.")

        return cat_list

    # Показываем дерево расходов
    def show_tree(self):
        print("\n═══ ДЕРЕВО ТРАТ ═══")
        print_tree(self.root)

    # Показываем все расходы
    def show_all_expenses(self):

        # Если список пустой
        if not self.all_expenses:
            print("Нет расходов")
            return

        print("\nВсе расходы:")

        # Выводим каждый расход
        for day, amount, cat in self.all_expenses:
            print(f"  День {day}: {cat} - {amount} руб.")