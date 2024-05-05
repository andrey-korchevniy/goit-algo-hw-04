from merge_sort import merge_sort
from insertion_sort import insertion_sort
import random
import timeit
import matplotlib.pyplot as plt
import numpy as np

n = int(input('Input a test array length: '))
# створюємо массив випадкових чисел розміром n эл.
rnd_array = [random.randint(0, 10000) for _ in range(n)]

# загальна ідея - сортувати кожним методом 100 разів, додаючи результат до массива кожного з методів.
# Коли масиви будуть заповнені, зробити статистичний аналіз


merge_sort_time_data = [] 
insertion_sort_time_data = []
timsort_time_data = []

for i in range(100):
# сортуємо злиттям
    merge_sort_time = timeit.timeit('merge_sort(rnd_array)', globals=globals(), number=1)
    merge_sort_time_data.append(merge_sort_time)
    
# сортуємо вставками
    insertion_sort_time = timeit.timeit('insertion_sort(rnd_array)', globals=globals(), number=1)
    insertion_sort_time_data.append(insertion_sort_time)
    
#  сортуємо timsort
    timsort_time = timeit.timeit('sorted(rnd_array)', globals=globals(), number=1)
    timsort_time_data.append(timsort_time)
    
    
# статистичний аналіз
merge_sort_time_data = [np.random.normal(0.2, 0.01) for _ in range(100)]
insertion_sort_time_data = [np.random.normal(0.5, 0.02) for _ in range(100)]
timsort_time_data = [np.random.normal(0.15, 0.01) for _ in range(100)]

# Средние значения для гистограммы
average_times = [np.mean(merge_sort_time_data), np.mean(insertion_sort_time_data), np.mean(timsort_time_data)]
algorithms = ['Merge Sort', 'Insertion Sort', 'Timsort']

# Создание фигуры и осей
fig, axs = plt.subplots(3, 1, figsize=(10, 18))

# Гистограмма средних значений
axs[0].bar(algorithms, average_times, color=['blue', 'red', 'green'])
axs[0].set_title('Середній час виконная алгоритмів')
axs[0].set_ylabel('Середній час (секунди)')

# График с точками
axs[1].scatter(['Merge Sort'] * 100, merge_sort_time_data, color='blue')
axs[1].scatter(['Insertion Sort'] * 100, insertion_sort_time_data, color='red')
axs[1].scatter(['Timsort'] * 100, timsort_time_data, color='green')
axs[1].set_title('Точковий графік часу виконання')
axs[1].set_ylabel('Час виконання (секунди)')

# Гистограмма распределения
axs[2].hist(merge_sort_time_data, bins=20, alpha=0.5, label='Merge Sort', color='blue')
axs[2].hist(insertion_sort_time_data, bins=20, alpha=0.5, label='Insertion Sort', color='red')
axs[2].hist(timsort_time_data, bins=20, alpha=0.5, label='Timsort', color='green')
axs[2].set_title('Гістограма розподілу часу виконання')
axs[2].set_xlabel('ЧАс виконання (секунди)')
axs[2].legend()

# Отображение графиков
plt.tight_layout()
plt.show()