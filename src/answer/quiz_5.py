def my_sort(data):
    return sorted(data, key=lambda x: (x % 3, x), reverse=True)
