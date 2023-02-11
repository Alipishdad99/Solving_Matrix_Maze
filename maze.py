import tkinter as tk
import time
def open_file(): # تابعی که فایل را باز میکند
    file = open("matrix.txt", "r") # باز کردن فایل
    read = file.readlines() # خواندن فایل
    maze1 = [] # ایجاد یک لیست برای ذخیره مسیر
    for line in read:
        temp_list=[] # حلقه ای که تا زمانی که خط های فایل تمام نشود اجرا میشود
        for char in line:
            if char in '01':
                temp_list.append(int(char)) # اضافه کردن اعداد به لیست
        maze1.append(temp_list) # اضافه کردن لیست به لیست

    return maze1 # برگرداندن مسیر
def solve_maze(maze, start, end): #تابعی که مسیر را حل میکند
    
    stack = [] # ایجاد یک لیست برای ذخیره مسیر

    stack.append(start) # اضافه کردن مقدار اولیه به لیست

    maze[start[0]][start[1]] = 2 # تغییر مقدار اولیه به 2
    
    row = [-1, 0, 1, 0] # ایجاد یک لیست برای ذخیره مقادیر ردیف
    
    col = [0, 1, 0, -1] # ایجاد یک لیست برای ذخیره مقادیر ستون
    
    while stack: # حلقه ای که تا زمانی که لیست خالی نباشد اجرا میشود
    
        current = stack.pop() # حذف مقدار آخرین مسیر از لیست
    
        i, j = current[0], current[1] # ایجاد متغیر های جدید برای ذخیره مقادیر ردیف و ستون
    
        if current == end: # اگر مسیر آخر با مقدار انتها برابر باشد
    
            return True # مسیر را برمیگرداند
    
        for k in range(4): # حلقه ای که تا زمانی که 4 بار اجرا شود اجرا میشود
    
            x, y = i + row[k], j + col[k]  # ایجاد متغیر های جدید برای ذخیره مقادیر ردیف و ستون
    
            if x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0]) and maze[x][y] == 0: # اگر مقادیر ردیف و ستون بزرگتر از صفر و کوچکتر از طول لیست باشد و مقدار آن در لیست برابر صفر باشد
    
                stack.append((x, y)) # مقدار را به لیست اضافه میکند
    
                maze[x][y] = 2 # مقدار را در لیست به 2 تغییر میدهد
    
                draw_path(x, y) # تابعی که مسیر را رسم میکند
    
                time.sleep(0.5) # تاخیر برای رسم مسیر

    return False # اگر مسیری وجود نداشت برمیگرداند

def draw_path(x, y): # تابعی که مسیر را رسم میکند
    canvas.delete("cat") # حذف تصویر قبلی
    canvas.create_image(y * cell_size + cell_size // 2, x * cell_size + cell_size // 2, image=cat, tags="cat") # ایجاد تصویر جدید
    window.update()

def draw_maze(maze): # تابعی که مسیر را رسم میکند
    for i in range(len(maze)): # حلقه ای که تا زمانی که طول لیست اجرا میشود
        for j in range(len(maze[0])): # حلقه ای که تا زمانی که طول لیست اجرا میشود
            if maze[i][j] == 1: # اگر مقدار آن در لیست برابر 1 باشد
                canvas.create_rectangle(j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size, fill="black")
Maze = open_file() # فراخوانی تابع

maze = Maze # ایجاد متغیر جدید برای ذخیره مسیر

start = (0, -1) # مقدار اولیه
end = (len(maze) - 1, len(maze) - 1) # مقدار انتها

window = tk.Tk() # ایجاد پنجره
window.title("Solve Maze") # عنوان پنجره
cell_size = 100 # اندازه سلول
canvas = tk.Canvas(window, width=len(maze) * cell_size, height=len(maze) * cell_size) # ایجاد یک لیست برای ذخیره مسیر
canvas.pack() # نمایش لیست

cat = tk.PhotoImage(file="run.png") # ایجاد تصویر 

draw_maze(maze) # فراخوانی تابع

if solve_maze(maze, start, end): # اگر مسیری وجود داشت
    print("The maze has a solution!") # پیامی که در صورت وجود مسیر نمایش داده میشود
else: # اگر مسیری وجود نداشت
    print("The maze has no solution.") # پیامی که در صورت عدم وجود مسیر نمایش داده میشود

window.mainloop() # اجرای پنجره
