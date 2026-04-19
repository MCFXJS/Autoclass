import json
import time
x = 0

print('开始初始化数据')
time.sleep(1)
print('1.请关掉杀毒软件','(操作完成请enter)')
input()
print('2.此设置会重置并清空test.json文件,这将会消失很长一段时间','(操作完成请enter)')
input()
print('准备就绪!')

#输入
with open('test.json', 'w', encoding='utf-8') as f:
    print("输入你要刷取的单个课程title名称。也可以选择手动编辑text.json文件进行。")
    print('输入完成后输入 stop ')
    while True:

        title = input()
        if title == "stop":
            print(f'一共{x}个数据')
            break

        else:
            f.write(title+'\n')
            x = x + 1
print('初始化数据完成','(操作完成请enter)')
input()





# with open(文件路径, 模式, 编码) as 变量名:
#     # 对文件进行操作
#     # 代码块结束后自动关闭文件
# 常用模式
# 模式	说明
# 'r'	只读（默认）
# 'w'	写入（会覆盖原有内容）
# 'a'	追加（在文件末尾添加）
# 'r+'	读写
# 'x'	创建新文件，如果存在则报错
