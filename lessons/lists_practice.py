grocery_list: list[str] = ["bananas", "milk", "bread"]

print(grocery_list[0])
print(["Kris", "Kreme", "P"][2])
print(grocery_list[len(grocery_list) - 1])
# print(grocery_list[len(grocery_list)])

grocery_list.pop(2)
grocery_list[1] = "eggs"
grocery_list.append("eggs")
print(grocery_list)

name: str = "Jack"
name_as_list: list[str] = list(name)
print(name)
print(name_as_list)

####
print("_____________")
####

x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0
print(x)
print(y)

####
print("_____________")
####


def lessen(my_list: list[int]):
    idx: int = 0
    while idx < len(my_list):
        my_list[idx] = my_list[idx] - 1
        idx += 1


msg: list[int] = [4, 5, 6]
lessen(msg)

print(msg)
