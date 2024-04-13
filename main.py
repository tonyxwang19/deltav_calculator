import math
import tkinter as tk

# 地球引力常数和半径（以米为单位）
gravity = 4 * (10 ** 14)
radius = 6371000

def price(orbit_height,fuel):
    return orbit_height*fuel+644724

# 计算霍曼转移轨道的Δv
def hohmann_orbit_delta_v_calculation(ri, rf):
    # 将起始半径和结束半径从千米转换为米，并加上地球半径
    ri = (ri * 1000) + radius
    rf = (rf * 1000) + radius
    # 计算Δv的两个部分
    a = math.sqrt(gravity / ri)*(math.sqrt(2*rf/(ri+rf))-1)
    b = math.sqrt(gravity / rf)*(1-math.sqrt(2 * ri / (ri + rf)))
    return a + b

def fuel_mass_calculation(deltav,ex_v,in_m):
    final_mass = (in_m)/math.exp(deltav/ex_v)
    fuel_mass = in_m-final_mass
    return fuel_mass
# 计算一般情况下的Δv
def delta_v_calculation(mass, fuel, payload_mass, exhaust_v):
    # 计算Δv
    delta_v = exhaust_v * math.log(((mass + payload_mass) / ((mass - fuel) + payload_mass)), math.e)
    return delta_v

# 当按钮被点击时执行的函数
def on_button_click():
    try:
        # 计算一般情况下的Δv
        result1 = delta_v_calculation(int(entry_1.get()), int(entry_2.get()), int(entry_3.get()), int(entry_4.get()))
        # 更新结果标签
        label_result1.config(text="Max Delta V:" + str(round(result1,3)))
    except ValueError:
        label_result1.config(text="Illegal Value Input")
    try:
        # 计算霍曼转移轨道的Δv
        result2 = hohmann_orbit_delta_v_calculation(int(entry_5.get()), int(entry_6.get()))
        # 更新结果标签
        label_result2.config(text="Required Delta V:" + str(round(result2, 3)))
    except ValueError:
        label_result2.config(text="Illegal Value Input")

    # 计算霍曼转移轨道的Δv
    result4 = round(fuel_mass_calculation(result2, int(entry_4.get()), int(entry_1.get()) + int(entry_3.get())), 3)
    # 更新结果标签
    label_result4.config(text="Required Fuel Mass:" + str(result4))

    result3 = price(int(entry_6.get()) - int(entry_5.get()), int(entry_2.get()))
    # 更新结果标签
    label_result3.config(text="Required Payment:" + str(result3))

    if result1 > result2:
        if result4<=int(entry_2.get()):
            open_popup(state1="The Delta V is enough for this mission.",state2="The fuel is enough for the mission")
        else:
            open_popup(state1="The Delta V is enough for this mission.",state2="The fuel is not enough for the mission")
    else:
        if result4 <= int(entry_2.get()):
            open_popup(state1="The Delta V is not enough for this mission.", state2="The fuel is enough for the mission")
        else:
            open_popup(state1="The Delta V is not enough for this mission.",state2="The fuel is not enough for the mission")

def open_popup(state1,state2):
    popup = tk.Toplevel()
    popup.title("Result")

    label = tk.Label(popup, text=state1)
    label.pack()

    label_fuel = tk.Label(popup, text=state2)
    label_fuel.pack()

    button_close = tk.Button(popup, text="Close", command=popup.destroy)
    button_close.pack()

# 创建主窗口
root = tk.Tk()
root.title("Delta V Calculator")

# 创建标签和输入框
label_1 = tk.Label(root, text="Please input product mass")  # 产品质量标签
label_1.pack()
entry_1 = tk.Entry(root)  # 产品质量输入框
entry_1.pack()

label_2 = tk.Label(root, text="Please input fuel mass")  # 燃料质量标签
label_2.pack()
entry_2 = tk.Entry(root)  # 燃料质量输入框
entry_2.pack()

label_3 = tk.Label(root, text="Please input payload mass")  # 载荷质量标签
label_3.pack()
entry_3 = tk.Entry(root)  # 载荷质量输入框
entry_3.pack()

label_4 = tk.Label(root, text="Please input exhausting velocity")  # 推出速度标签
label_4.pack()
entry_4 = tk.Entry(root)  # 推出速度输入框
entry_4.pack()

# 分隔线
label_separator1 = tk.Label(root, text="--------------------")  # 分隔线
label_separator1.pack()

label_5 = tk.Label(root, text="Please input initial orbit height(km)")  # 初始轨道高度标签
label_5.pack()
entry_5 = tk.Entry(root)  # 初始轨道高度输入框
entry_5.pack()

label_6 = tk.Label(root, text="Please input final orbit height(km)")  # 最终轨道高度标签
label_6.pack()
entry_6 = tk.Entry(root)  # 最终轨道高度输入框
entry_6.pack()

# 分隔线
label_separator2 = tk.Label(root, text="--------------------")  # 分隔线
label_separator2.pack()

# 创建结果标签
label_result1 = tk.Label(root, text="")  # 结果标签1
label_result1.pack()

label_result2 = tk.Label(root, text="")  # 结果标签2
label_result2.pack()

label_result3 = tk.Label(root, text="")  # 结果标签3
label_result3.pack()

label_result4 = tk.Label(root, text="")  # 结果标签4
label_result4.pack()

# 创建按钮
button = tk.Button(root, text="Calculate!", command=on_button_click)  # 计算按钮
button.pack()

# 运行主循环
root.mainloop()
