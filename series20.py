from os import system
from functools import reduce
import random
system('clear')


def generate_lst(n):            # List generatsiya qilish uchun funksiya
    main_lst, idx = [ i for i in range(0, 15)], 0
    my_lst = list()
    while idx < n:
        random_char = random.choice(main_lst)
        my_lst.append(random_char)
        idx += 1
    return my_lst


# Series 20
def bigger_right(n):
    count, my_lst = 0, generate_lst(n)

    for i in my_lst[:-1]:
        if i < my_lst[my_lst.index(i) + 1]:
            count += 1
            print(i)
    print(f'List: {my_lst}\nSoni: {count}')

#bigger_right(6)


# Series 21

def increaseTrue(n):
    my_lst = generate_lst(n)
    print(my_lst)
    return True if sorted(my_lst) == my_lst else False

#print(increaseTrue(3))


# Series 22

def decreaseIndex(n):
    my_lst, idx, var = generate_lst(n), 0, list()
    print(my_lst)
    while idx < len(my_lst)-1:
        var = [True, idx + 1]
        if my_lst[idx] <= my_lst[idx + 1]:
            var[0] = False
            break
        idx += 1
    return 0 if var[0] else var[1]

#print(decreaseIndex(3))


# Series 23

def crazyList():
    my_lst, idx, var = [1, 3, 2, 6, 3, 9, 8], 1, list()           #   arra list -> [5, 3, 4, 2, 6], [1, 3, 2, 6, 3, 9, 8]
    while idx < len(my_lst)-1:
        var = [True, idx]
        if not (my_lst[idx-1] < my_lst[idx] > my_lst[idx+1] or my_lst[idx-1] > my_lst[idx] < my_lst[idx+1]):
            var[0] = not var[0]
            break
        idx += 1
    return 0 if var[0] else var[1]

#print(crazyList())


# Series 24

def sum_between(n):         # [0, 4, 4, 2, 0] , [0, 5, 0, 1, 1]
    my_lst = [random.randint(0, 5) for _ in range(n)] # random elementlardan list generatsiya qilish
    print(my_lst)

    idx, count_sum, flag = len(my_lst)-1, 0, False
    if my_lst.count(0) >= 2:
        while idx >= 0:

            if my_lst[idx] == 0:
                flag = not flag

            if flag:
                count_sum += my_lst[idx]
            idx -= 1
        return count_sum
    else: return False

#print(sum_between(5))


#   Series 25

class Solution:

    def sum_(self, n):
        my_lst = [1, 5, 0, 9,0, 1, 2, 0, 4, 0, 9]
        flag, idx, lst_idx = False, None, list()

        for i in my_lst:
            if i == 0:
                lst_idx.append(my_lst.index(i))

        return sum(my_lst[min(lst_idx):max(my_lst)])

obj = Solution()
print(obj.sum_(2))


#   Series 26

def degree(n, k):

    my_lst = [random.randint(0, 5) for _ in range(n)]  # random elementlardan list generatsiya qilish
    print(my_lst)

    for i in my_lst:
        result = 1
        for _ in range(k):
            result *= i

        print(f"{i} - {result}")

#degree(4, 3)


#   Series 27

def match_degree(n):
    num_list = [random.randint(0, 5) for _ in range(n)]

    idx, var = 1, 1
    for i in num_list:

        while idx <= var:
            result = i ** idx
            print(f"{i} ** {idx} = {result}")
            idx += 1
        var += 1
#match_degree(4)


#   Series 28

def do_something(n):
    num_list = [random.randint(0, 5) for _ in range(n)]
    print(num_list)
    var = n
    for num in num_list:
        idx = 1
        result = 1
        while idx <= var:
            result *= num
            idx += 1
        print(f"{num} ** {var} = {result}")
        var -= 1

#do_something(4)


# Series 29

class Solution:
    def __init__(self, n, k):
        self.num_elem = n
        self.num_lst = k
        self.Lst = list()

    def make_lists(self):

        idx = 0
        while idx < self.num_lst:
            self.Lst.append([random.randint(0, 5) for _ in range(self.num_elem)])
            idx += 1

    def sum_(self):
        return sum([sum(lst) for lst in self.Lst])

obj = Solution(4, 3)
obj.make_lists()
print(obj.Lst)
print(obj.sum_())

