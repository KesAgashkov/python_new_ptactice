import pickle
import sys
import os

#1
def record_obj_to_pickle():
    dogs = {'Ozzy': 2, 'Filou': 7, 'Luna': 4, 'Skippy': 11, 'Barco': 13, 'Balou': 10, 'Laika': 15}

    with open('dogs.pkl', mode='bw') as file:
        pickle.dump(dogs, file)

# record_obj_to_pickle()

#2
def extract_func_from_pickle():
    filename, *arg = [el.strip() for el in sys.stdin]
    print(filename)
    print(arg)
    with open(filename, "rb") as file:
        f_pickle = pickle.load(file)
    print(f_pickle(*arg))
# extract_func_from_pickle()

#3
def filter_dump(filename, objects, typename):
    res = []
    res = [el for el in objects if type(el)==typename]
    with open(filename, "wb") as file:
        pickle.dump(res, file)

#4
def last_task():
    compare = 0
    with open(input(), "rb") as file:
        check = int(input())
        ob_pickle = pickle.load(file)
        if type(ob_pickle) == dict:
            res = [el for el in ob_pickle if type(el) == int]
            if res: compare = sum(res)
        else:
            res = [el for el in ob_pickle if type(el) == int]
            if res: compare = max(res) * min(res)
    print("Контрольные суммы совпадают" if check == compare else "Контрольные суммы не совпадают")


import gc
# from pympler import asizeof
# import sys
#
# lst1 = [1, [10,5,4]]
#
# print(sys.getsizeof(lst1))
# print(asizeof.asizeof(lst1))

print(gc.isenabled())