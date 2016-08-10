def my_sort2(data):
    return sorted(data, key=lambda x: (x % 3, x), reverse=True)
