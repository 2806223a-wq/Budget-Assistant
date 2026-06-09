class TreeNode:
    def __init__(self, name, amount=None):
        self.name = name          # Название узла
        self.amount = amount      # Хранит сумму расхода
        self.children = []        # Список дочерних узлов

# Ищем категорию по названию
def find_category(node, category_name):

    # Если нашли нужную категорию
    if node.amount is None and node.name == category_name:
        return node

    # Проверяем все дочерние узлы
    for child in node.children:
        result = find_category(child, category_name)

        # Если категория найдена, возвращаем ее
        if result:
            return result

    # Если ничего не нашли
    return None

# Добавляем новую трату в выбранную категорию
def add_expense_to_tree(root, category_name, amount):

    # Ищем нужную категорию
    cat = find_category(root, category_name)

    if cat:
        # Создаем узел с суммой траты
        new_node = TreeNode(str(amount), amount)

        # Добавляем трату в категорию
        cat.children.append(new_node)

        return True

    # Категория не найдена
    return False

# Выводим дерево на экран
def print_tree(node, level=0):

    # Создаем отступ для каждого уровня дерева
    indent = "  " * level

    # Если это трата, выводим сумму
    if node.amount is not None:
        print(f"{indent}{node.name} руб.")
    else:
        # Если это месяц или категория, выводим название
        print(f"{indent}{node.name}")

    # Выводим все дочерние элементы
    for child in node.children:
        print_tree(child, level + 1)