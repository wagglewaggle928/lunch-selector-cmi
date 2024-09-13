Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random
import json
import os

# 午餐选项列表
lunch_options = [
    "🍲 市民麻辣香锅", "🍜 凤凰孔一凡", "🥟 沙县小吃", "🍛 卓悦敏华", "🍲 麻辣烫", 
    "🍲 石锅拌饭", "🍔 麦当劳", "🍗 肯德基", "🥣 胡辣汤", "🍤 喜家德", 
    "🍜 螺狮粉", "🍜 凤凰粿条", "🥢 马记永", "🥢 食堂5层", "🥢 食堂6层", 
    "🥢 食堂7层", "🍲 云南米线", "🍲 贵州米线", "🥟 小杨生煎", "🐟 酸菜鱼"
]

# 记录文件名
record_file = "lunch_record.json"

# 读取记录文件
def load_record():
    if os.path.exists(record_file):
        with open(record_file, "r") as file:
            return json.load(file)
    else:
        return {option: 0 for option in lunch_options}

# 保存记录
def save_record(record):
    with open(record_file, "w") as file:
        json.dump(record, file)

# 随机选择午餐
def choose_lunch():
    return random.choice(lunch_options)

# 显示菜单
def show_menu():
...     print("今天的午餐选择有：")
...     for option in lunch_options:
...         print(option)
... 
... # 主程序
... def main():
...     record = load_record()
...     chosen_options = []
...     
...     print("欢迎来到可爱又有趣的午餐选择器！")
...     show_menu()
... 
...     # 用户可以选择三次
...     for i in range(3):
...         input(f"\n第 {i+1} 次选择，按 Enter 开始...")
...         choice = choose_lunch()
...         print(f"第 {i+1} 次选择的午餐是: {choice}")
...         chosen_options.append(choice)
... 
...     print("\n今天你可以选择以下三次结果之一：")
...     for i, option in enumerate(chosen_options, 1):
...         print(f"{i}. {option}")
...     
...     # 最终选择
...     final_choice = int(input("\n请选择你最终想吃的午餐（输入1-3的数字）："))
...     selected_lunch = chosen_options[final_choice - 1]
... 
...     print(f"\n你最终选择的午餐是: {selected_lunch}！好好享受吧！")
... 
...     # 更新记录
...     record[selected_lunch] += 1
...     save_record(record)
... 
...     print("\n午餐选择统计：")
...     for option, count in record.items():
...         print(f"{option}: {count} 次")
... 
... # 运行主程序
... if __name__ == "__main__":
