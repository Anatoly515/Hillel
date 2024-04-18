 #   бази данних
 #   списки (list), кортежі (type), словники (dict), множники (set, frozenset)

 #   deque, bytea, range - структури данних

 #    змінювання (mutable)
 #    list, dict. set
 # незмінювання (immutable)
 # frozenset, tuple


#  tuple (kortej) данні які не змінюються
#  Forma zapuzy


empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))


single_el_tuple = (42,)
print(single_el_tuple)
print(type(single_el_tuple))

mix_tuple = (1, "hello", 3.14, True)
print(mix_tuple)
print(type(mix_tuple))

rare_form_tuple = 1, 'hello', 3.14, True
print(rare_form_tuple)
print(type(rare_form_tuple))


# Dostyp do elementiv
my_tuple = (10, 20, 30, 40, 50)

first_element = my_tuple[0]
second_element = my_tuple[1]
third_element = my_tuple[2]

print(first_element)
print(second_element)
print(third_element)

#
# count()
_tuple = (1, 2, 3, 2, 4, 2, 5)
count_of_2 = _tuple.count(2)
print('count of name:', count_of_2)

#  index()
index_of_2 = _tuple.index(2)
print('index 2:', index_of_2 )
print('index 2:= ', _tuple.index(3))

# Розрізи (slices)

sub_tuple = _tuple[2::6]
print(sub_tuple)
print('full tuple', _tuple)
print('sub tupel', sub_tuple)

#  Розпакування (unboxing)

a, b, c = (10, 20, 30)
print(a)
print(b)
print(c)

# формування кортежів з інших данних
my_str = 'Hello world'
tuple_from_str = tuple(my_str)
print(tuple_from_str)
my_list = [1, 2, 3, 'Python', True]

tuple_from_list = tuple(my_list)
print(tuple_from_list)

