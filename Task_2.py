import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Визначення нової функції
def f(x):
    return np.sin(x)

# Межі інтегралу
a = 0
b = np.pi

# Метод Монте-Карло для обчислення інтегралу
def monte_carlo_integration(f, a, b, num_samples=10000):
    # Генеруємо випадкові зразки в межах від a до b
    samples = np.random.uniform(a, b, num_samples)
    # Обчислюємо значення функції для кожного зразка
    sample_evaluations = f(samples)
    # Обчислюємо середнє значення та множимо на (b - a)
    return (b - a) * np.mean(sample_evaluations)

# Обчислення інтегралу методом Монте-Карло
монте_карло_результат = monte_carlo_integration(f, a, b)
print("Результат Монте-Карло:", монте_карло_результат)

# Перевірка результату за допомогою функції quad
quad_результат, quad_помилка = quad(f, a, b)
print("Результат за допомогою quad:", quad_результат)

# Графік функції та область під кривою
x = np.linspace(a, b, 400)
y = f(x)

fig, ax = plt.subplots()
# Малюємо функцію
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
# Заповнюємо область під кривою
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
# Додаємо межі інтегрування
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = sin(x) від {a} до {b}')
plt.grid()
plt.show()
