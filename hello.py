import os
# 关键：指定系统 Python 中的 Tcl 库路径（你的系统 Python 路径是 C:\Python\Python313）
os.environ['TCL_LIBRARY'] = r'C:\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python\Python313\tcl\tk8.6'

import tkinter as tk

# 创建主窗口
window = tk.Tk()
# 添加标签
label = tk.Label(window, text='Hello, World!')
label.pack()
# 显示窗口并进入GUI事件循环
window.mainloop()

#print("hello, world!")
#height = float(input('身高(cm)：'))
#weight = float(input('体重(kg)：'))
#bmi = weight / (height / 100) ** 2
#print(f'{bmi = :.1f}')
#if 18.5 <= bmi < 24:
#    print('你的身材很棒！')
#import time


#for _ in range(1):
#    print('hello, world')
#    time.sleep(1)