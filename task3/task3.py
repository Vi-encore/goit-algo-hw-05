from timeit import timeit
from algo_search.boyer_moore_search import boyer_moore_search
from algo_search.kmp_search import kmp_search
from algo_search.rabin_karp_search import rabin_karp_search


def load_file(file):
    with open(file, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


text_1 = load_file("./task3/стаття1.txt")
text_2 = load_file("./task3/стаття2.txt")

text1_substring = "public static int binarySearch(int arr[], int elementToSearch)"
text2_substring = (
    "Було проведено 4 серії експериментів. Нижче наведено параметри кожної серії."
)
my_substring = "Цього тексту не існує в жодній статті"


def search_time(search_func, text, pattern):
    time = timeit(lambda: search_func(text, pattern), number=1000)
    return time


# Вигаданий підрядок і стаття номер 2
bm_time = search_time(boyer_moore_search, text_2, my_substring)
kmp_time = search_time(kmp_search, text_2, my_substring)
rk_time = search_time(rabin_karp_search, text_2, my_substring)
print("\n Результати для статті номер 2 з не існуючим підрядком")
print(f"Боєра-Мура: {bm_time} секунд")
print(f"Кнута-Морріса-Пратта: {kmp_time} секунд")
print(f"Рабіна-Карпа: {rk_time} секунд")

# Існуючий підрядок і стаття номер 2
bm_time = search_time(boyer_moore_search, text_2, text2_substring)
kmp_time = search_time(kmp_search, text_2, text2_substring)
rk_time = search_time(rabin_karp_search, text_2, text2_substring)
print("\n Результати для статті номер 2 з існуючим підрядком")
print(f"Боєра-Мура: {bm_time} секунд")
print(f"Кнута-Морріса-Пратта: {kmp_time} секунд")
print(f"Рабіна-Карпа: {rk_time} секунд")

# Існуючий підрядок і стаття номер 1
bm_time = search_time(boyer_moore_search, text_1, text1_substring)
kmp_time = search_time(kmp_search, text_1, text1_substring)
rk_time = search_time(rabin_karp_search, text_1, text1_substring)
print("\n Результати для статті номер 1 з існуючим підрядком")
print(f"Боєра-Мура: {bm_time} секунд")
print(f"Кнута-Морріса-Пратта: {kmp_time} секунд")
print(f"Рабіна-Карпа: {rk_time} секунд")
