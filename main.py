def get_matrix(n, m, value):
    # Создаем пустой список для матрицы
    matrix = []
    # Внешний цикл для строк матрицы
    for i in range(n):
        # Добавляем новый пустой список для каждой строки
        row = []
        # Внутренний цикл для столбцов матрицы
        for j in range(m):
            # Добавляем значение value в текущий ряд
            row.append(value)
        # Добавляем заполненный ряд в матрицу
        matrix.append(row)
    # Возвращаем заполненную матрицу
    return matrix
# Примеры использования функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
# Выводим результаты на экран
print(result1)
print(result2)
print(result3)