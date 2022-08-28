#decode&encode
main_b = b'r\xc3\xa9sum\xc3\xa9'
print(main_b)
main_str = main_b.decode()
print(main_str)
main_b_latin = main_str.encode('Latin1')
print(main_b_latin)
main_str_latin = main_b_latin.decode('Latin1')
print(main_str_latin)
