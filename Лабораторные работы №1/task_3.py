
one_bytes = 4
pages = 100
lines = 50
chars = 25

total_chars = chars * lines * pages
total_bytes = total_chars * one_bytes

disket_size = 1.44 * 1024 * 1024
number_books = int(disket_size // total_bytes)

print("Количество книг, помещающихся на дискету:", number_books)

