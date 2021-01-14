from functools import lru_cache
import time
inp1 = int(input("Enter how many values you cache"))

@lru_cache(maxsize= inp1)
def unknown_func(n):
    time.sleep(n)

print("wait 4 second")
unknown_func(4)
print("wait 5 second")
unknown_func(5)
print("wait 6 second")
unknown_func(6)

print("check6")
unknown_func(6)
print("check5")
unknown_func(5)
print("check4")
unknown_func(4)
print("end")
