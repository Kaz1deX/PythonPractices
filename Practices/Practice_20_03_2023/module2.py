from module import GLOBAL_VAR
from module1 import func1
import module


def func2():
    print("func2")
    print(GLOBAL_VAR)
    print(module.GLOBAL_VAR)


func1()
func2()
print()
GLOBAL_VAR = 10
func1()
func2()
print()
module.GLOBAL_VAR = 10
func1()
func2()
print()
