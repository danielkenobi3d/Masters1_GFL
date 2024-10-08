# in this file it is explained how to use variables.
my_name = 'daniel ruiz vargas'
string_number = '67.8'
the_number = 45
new_variable = 5.5
print(string_number + str(45))
# for each in dir(my_name):
#     print(each)
# capitalize casefold center count encode endswith expandtabs
# find format format_map  index isalnum isalpha
# isascii isdecimal isdigit isidentifier islower
# isnumeric isprintable isspace istitle isupper
# join ljust lower lstrip maketrans partition removeprefix
# removesuffix replace rfind rindex rjust rpartition
# rsplit rstrip split splitlines startswith strip swapcase
# title translate upper zfill
print(my_name.capitalize())
print(my_name.count('a'))
print(my_name.find('ruiz'))

base_string='C_{}_rig_{}'

print(base_string.format('arm', 'CTRL') )

my_list = [5, 2 , 'daniel', 'rubika']

print(my_list[2])
print(my_list[1])

for each in my_list:
    print(each)

print(list(range(12)))


