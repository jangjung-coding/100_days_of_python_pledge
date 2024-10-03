# Tkinter

import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tk.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(expand=True)

# Advanced Python Arguments

# Unlimited Arguments : 무한 인수를 사용하면 함수에 전달되는 인수의 개수를 미리 정하지 않고 필요한 만큼의 인수를 전달할 수 있습니다.
# def add(*args):
#     print(args)
#     return sum(args)

# print(add(1, 2, 3, 4, 5))

# Keyword Arguments : 키워드 인수를 사용하면 함수에 전달되는 인수의 이름을 지정하여 전달할 수 있습니다.
# def calculate(n, **kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)

# calculate(2, add=3, multiply=5)

window.mainloop()