# %% 8.3.2
def get_formatted_name(first_name: str, last_name: str, middle_name=''):
    """Return a neatly formatted full name."""
    if type(first_name) != str or type(last_name) != str:
        raise TypeError('first_name and last_name must be of type str.')
    if middle_name:
        full_name = first_name.strip().title() + " " + middle_name.strip().title() + " " + last_name.strip().title()
    else:
        if first_name == '' and last_name == '':
            full_name = ''
        else:
            full_name = first_name.strip().title() + " " + last_name.strip().title()
    return full_name

# %% 8.5
def make_pizza_with_no_size(*toppings):
    for i in toppings:
        print(i)

make_pizza_with_no_size('pepperoni', 'mushrooms', 'green peppers', 'extra cheese')
make_pizza_with_no_size(('pepperoni', 'mushrooms', 'green peppers', 'extra cheese'))

# %% 8.5.1 python did not do type checking in runtime, should be enabled in vscode
def make_pizza(size: int, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    print(toppings)

make_pizza(5, 'pepperoni', 'mushrooms', 'green peppers', 'extra cheese')
make_pizza(5, ('pepperoni', 'mushrooms', 'green peppers', 'extra cheese'))
make_pizza(5, *('pepperoni', 'mushrooms', 'green peppers', 'extra cheese'))

# %% 10.1.1
with open('pi_digits.txt', 'r') as f:
    for line in f:
        print(line.strip())

# %% 10.3.6
filename = 'alice.txt'

def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # 计算该文件大致包含多少个单词。”
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt', '.']
for file in filenames:
    print(file)
    count_words(file)

# %%
