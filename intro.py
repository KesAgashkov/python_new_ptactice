##1
def hide_card(card):
    return "*"*12 + card.replace(" ", "")[12:]

##2
def same_parity(sp):
    if not sp:
        return []
    n = sp[0]%2
    if not n:
        return [el for el in sp if el%2 == 0]
    else:
        return [el for el in sp if el%2 == 1]

 ## или вот так
def same_parity(nums):
    return [i for i in nums if i % 2 == nums[0] % 2]

##3

def is_valid(pin):
    return (not(pin.isspace()) and len(pin) in (4,5,6) and pin.isdigit())

##4

def print_given(*args, **kwargs):
    for el in args:
        print(el, type(el))
    for k,v in sorted(kwargs.items()):
        print(k, v, type(v))

# print_given(b=2, d=4, c=3, a=1)

##5

def convert(st):
    low = 0
    up = 0
    for el in st:
        if el.isalpha():
            if el.islower():
                low+=1
            else:
                up+=1
    return st.lower() if low>=up else st.upper()

# print(convert("pi31415!"))

##5

def filter_anagrams(word, words):
    w = sorted(list(word))
    res= []
    for el in words:
        c = sorted(list(el))
        print(c)
        if c == w:
            res.append(el)
    print(el)

# или так
def filter_anagrams(word, anagrams):
    return [anagram for anagram in anagrams if sorted(anagram) == sorted(word)]

##6

def likes(names):
    if not names:
        return "Никто не оценил данную запись"
    elif len(names) == 1:
        return f"{names[0]} оценил(а) данную запись"
    elif len(names) == 2:
        return f"{names[0]} и {names[1]} оценили данную запись"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} и {names[2]} оценили данную запись"
    else:
        return f"{names[0]}, {names[1]} и {len(names)-2} других оценили данную запись"

##7

def index_of_nearest(numbers, number):
    if not numbers:
        return -1
    min =abs(numbers[0] - number)
    for el in numbers:
        if abs(el - number) < min:
            min = el - number
    return numbers.index(min+number)

# print(index_of_nearest([734234423423423, 5343423423546463423, 934234423423423423, -1], 0))

##8