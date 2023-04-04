import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

value = [None] * 1024
next_ptr = [None] * 1024
prev_ptr = [None] * 1024
empty_min_idx = 1  # まだ使用していない配列の要素で、最も小さいインデックス
start_ptr = 0  # リストの先頭のインデックス
end_ptr = 1023  # リストの末尾の次のインデックス


def push_bak(a):
    global empty_min_idx
    new_ptr = empty_min_idx
    empty_min_idx += 1
    prev_last = prev_ptr[end_ptr]

    value[new_ptr] = a
    prev_ptr[new_ptr] = prev_last
    next_ptr[new_ptr] = end_ptr
    next_ptr[prev_last] = new_ptr
    prev_ptr[end_ptr] = new_ptr

def delete_back():
    back_ptr = prev_ptr[end_ptr]
    if back_ptr != start_ptr:
        to_be_last = prev_ptr[back_ptr]
        next_ptr[to_be_last] = end_ptr
        prev_ptr[end_ptr] = to_be_last


def print_list_values():
    current_ptr = start_ptr
    while current_ptr != end_ptr:
        if current_ptr != start_ptr:
            print(value[current_ptr])
        current_ptr = next_ptr[current_ptr]


n, k = MI()
value[start_ptr] = -1
value[end_ptr] = -1
next_ptr[start_ptr] = end_ptr
next_ptr[end_ptr] = -1
prev_ptr[end_ptr] = start_ptr
prev_ptr[start_ptr] = -1

for i in range(n):
    a = int(input())
    push_bak(a)

for i in range(k):
    delete_back()

print_list_values()
