def append_value(val, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(val)
    return target_list

print(append_value(1))
print(append_value(2))
print(append_value(3,[]))
print(append_value(4))


# my_string = '  hey there  '
# cleaned = my_string.strip().upper()
# print(my_string) # same b/c string is immutable
# print(cleaned)

# my_list = ['a','b','c']
# my_new_list = my_list.append('d')
# print(my_list)
# print(my_new_list)

