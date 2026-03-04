import math

git = 22.7
sql = 35.2
english = 28.3
django = 31.8
linux = 30.5

def analyze_skills_geometric():
    # Находим минимум и максимум
    min_val = min(git, sql, english, django, linux)
    max_val = max(git, sql, english, django, linux)
    
    # Вычисляем произведение
    product = min_val * max_val
    
    # Извлекаем квадратный корень
    geom_mean = math.sqrt(product)
    
    # Округляем до двух знаков
    rounded = round(geom_mean, 2)
    
    # Выводим результат
    print(f"Среднее геометрическое между наименее и наиболее популярным навыком (в %): {rounded}")

# Вызов функции для проверки
analyze_skills_geometric()