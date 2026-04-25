from datetime import time
import pyautogui
import selenium
import time
import random
import json
#作用：导入浏览器驱动核心功能
# 用途：创建浏览器对象
from selenium import webdriver
#作用：导入键盘按键功能
#用途：模拟键盘操作
# # 模拟按回车键
# input_element.send_keys(Keys.ENTER)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# 作用：导入元素定位方式
# 用途：告诉 Selenium 用什么方式找元素
# # By 提供了多种定位方式
# wd.find_element(By.ID, 'phone')           # 通过ID
from selenium.webdriver.support.ui import WebDriverWait
# 作用：导入显式等待功能
#
# 用途：等待元素出现后再操作
#
# python
# # 最多等待10秒，直到元素出现
# wait = WebDriverWait(wd, 10)
# element = wait.until(EC.presence_of_element_located((By.ID, 'phone')))
from selenium.webdriver.support import expected_conditions as EC

#适配Google驱动
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#多线程
import threading



#####################################################################################
print('ご主人さま，你要看哪个呢？')
print("例如：https://mooc1.chaoxing.com/mycourse/studentstudy?chapterId=705032039&courseId=262336996&clazzid=143937452&cpi=490971353&enc=3f81db8d9162e31198db167256413961&mooc2=1&hidetype=0&openc=c44a08b1d065c90c0fef6b4b717d8494")
url = input()
print("输入学习通手机号")
Phone_number = input()
print("输入密码")
Password = input()

#选择浏览器驱动
while True:
    print("请选择驱动", 'Edge浏览器输入1(建议),Google Chrome输入2')
    Chrome_1 = input()
    if Chrome_1 == '1':
        #wd = webdriver.Edge()
        print('已选择Edge')
        time.sleep(0.2)
        break
    elif Chrome_1 == '2':
        #service = Service(ChromeDriverManager().install())
        #wd = webdriver.Chrome(service=service)
        print('已选择Google Chrome')
        time.sleep(2)
        break
    else:
        print('没有这个驱动选项')


#输入要抓的网址
#url = 'https://mooc1.chaoxing.com/mycourse/studentstudy?chapterId=705032039&courseId=262336996&clazzid=143937452&cpi=490971353&enc=3f81db8d9162e31198db167256413961&mooc2=1&hidetype=0&openc=c44a08b1d065c90c0fef6b4b717d8494'
time.sleep(1)

############################################################################################################################

#输入账号密码并回车
def inputNM():
    #窗口大小
    wd.set_window_size(1300, 1600)
    time.sleep(1)
    #元素有明确的 id	By.ID,
    #需要通过 class 查找	By.CSS_SELECTOR
    input_list = wd.find_element(By.ID, 'phone')
    input_list2 = wd.find_element(By.ID, 'pwd')
    print(input_list)
    time.sleep(0.5)
    input_list.send_keys(Phone_number)
    time.sleep(0.1)
    input_list2.send_keys(Password)
    time.sleep(0.1)
    #确认密码回车
    #wd内核,在网页中找到第一个 <button> 标签元素，然后点击它。click()运行
    wd.find_element(By.CSS_SELECTOR, 'button').click()
    time.sleep(5)
# 以上皆为登录
time.sleep(1)  # 等待登录跳转完成


##########################################################################
#这边的抓取逻辑是AI写的喵，我只负责找CSS和HTML.ID
time_1 = 10
def play_video_in_chaoxing(driver):
    #超星开刷
    try:
        #eng.....
        time.sleep(3)

        # 1. 先找到包含视频内容的iframe（id="iframe"）
        print("正在寻找视频iframe...")
        video_iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "iframe"))
        )
        print(" 找到视频iframe")

        # 2. 切换到iframe里面
        driver.switch_to.frame("iframe")
        print(" 已切换到iframe")

        # 3. 等待iframe内部加载
        time.sleep(3)

        # 4. 在iframe里面找video标签
        videos = driver.find_elements(By.TAG_NAME, "video")

        if videos:
            # 播放视频
            driver.execute_script("arguments[0].play();", videos[0])
            print(" 视频开始播放")
            duration = driver.execute_script("return arguments[0].duration;", videos[0])
            print(duration)
            return duration
        else:
            # 可能还有嵌套的iframe
            print("未找到video，尝试查找嵌套iframe...")
            inner_iframes = driver.find_elements(By.TAG_NAME, "iframe")
            print(f"iframe内还有 {len(inner_iframes)} 个iframe")

            for i, iframe in enumerate(inner_iframes):
                try:
                    print("10%")
                    driver.switch_to.frame(iframe)
                    print("30%")
                    videos = driver.find_elements(By.TAG_NAME, "video")
                    print("50%")
                    if videos:
                        print("70%")
                        driver.execute_script("arguments[0].play();", videos[0])
                        print(f" 在嵌套iframe[{i}]中找到视频并播放")
                        time.sleep(1)
                        print("100%")
                        duration = driver.execute_script("return arguments[0].duration;", videos[0])
                        time.sleep(2)

                        #用于变量dati(time_1)
                        time_1 = duration + 60
                        print(time_1)


                        return duration
                    driver.switch_to.parent_frame()
                except:
                    driver.switch_to.parent_frame()
                    continue

            print(" 未找到视频元素")
            return False

    except Exception as e:
        print(f" 播放失败: {e}")

        # 调试信息
        try:
            driver.switch_to.default_content()
            iframes = driver.find_elements(By.TAG_NAME, "iframe")
            print(f"主页面找到 {len(iframes)} 个iframe")
            for i, iframe in enumerate(iframes):
                print(f"iframe[{i}] id={iframe.get_attribute('id')}, src={iframe.get_attribute('src')}")
        except:
            pass

        return False
##################################################################################################################

#海内存知己，天涯若比邻
#auto刷题
def dati(time_1):
    # 定时长T为进度,time_1为总时长
    T = 0
    time.sleep(0.5)
    print(f"主人，视频要看{time_1}秒喵")
    while T <= time_1:
        print(f"勾修金さま，已帮你答题{T}喵")
        T = T + 1
        time.sleep(0.8)
        try:
            choices = wd.find_element(By.CSS_SELECTOR, 'label')
            #随机
            #从列表中随机random.choice选择一个元素
            random.choice(wd.find_elements(By.CSS_SELECTOR, 'label')).click()  # 随机选择A,B,C,D选项
            wd.find_element(By.ID, 'videoquiz-submit').click()#提交
            try:
                wd.find_element(By.CSS_SELECTOR, 'videoquiz-continue').click()#点击继续学习(点击提交后但还要确定一下)
            except:
                pass
                # print("没有{点击继续学习}，故直接跳过")
            time.sleep(0.2)
            print("答了一个喵~")
        except:
            pass  # 没有选择题则跳过
            #print("否")
            time.sleep(0.2)

#子进程版无条件循环自动答题2.0版本更新
#def dati():
#    while True:
#        try:
#            choices = wd.find_element(By.CSS_SELECTOR, 'label')
#            random.choice(wd.find_elements(By.CSS_SELECTOR, 'label')).click()#随机选择A,B选项
#            time.sleep(0.5)
#            #wd.find_element(By.ID, 'videoquiz-submit').click()#确定
#            time.sleep(5)
#            print("111")
#        except:
#            pass#没有选择题则跳过
#            print("222")
#            time.sleep(1)
##创建子进程t2 dati
#t2 = threading.Thread(target=dati)

###############################################################################################################################
#用无产阶级创造所有美好的荣光,来取代资产阶级生产关系下所鼓吹的愚蠢行径！
#一下为刷课对象

#初始行
x = 0
#从test.json读r,命为f
with open('test.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    #所有行
    x_max = len(lines)
    print(f"text.json中共有{x_max}项")

while True:
    if x <= x_max:
        with open('test.json', 'r', encoding='utf-8') as f:
            #读取文件对象 f 中的所有行,将读取结果赋值给变量 lines（通常是一个列表）
            lines = f.readlines()
            #读取x行内容
            video_1 = lines[x].strip()
            time.sleep(0.5)
            print(f"主人,是这个{video_1}视频吗?")


        # 以edge驱动打开并单独环境,wd为浏览器代称
        #wd = webdriver.Edge()
        if Chrome_1 == "1":
            wd = webdriver.Edge()
        if Chrome_1 == "2":
            service = Service(ChromeDriverManager().install())
            wd = webdriver.Chrome(service=service)
        wd.get(url)
        inputNM()
        # wd.find_element(By.CSS_SELECTOR, 'span[title="五六十年代创作的红色经典反特片（一）"]').click()
        print('请将鼠标放置要看课的目录，方便鼠标滑动查找喵')
        time.sleep(2)
        # 控制鼠标
        # pyautogui.scroll(5)
        time.sleep(2)

        #找到视频点击
        # 控制鼠标
        # wd.find_element(By.XPATH, f'//span[@title="{video_1}"]').click()
        scroll_1 = 0
        while True:
            try:
                wd.find_element(By.XPATH, f'//span[@title="{video_1}"]').click()
                break
            except:
                scroll_1 = scroll_1 + 1
                pyautogui.scroll(-1000)
                print('已帮主人下滑1000点单位！')
                time.sleep(0.2)
                if scroll_1 >= 10:
                    print('已经下滑鼠标找了10次喵，没有发现课程目标。怎么回事呢，ご主人様？')
                    scroll_1 = scroll_1 - 10
                    time.sleep(10)
                    print("那咱继续找喽~~~~~~~~")

        time.sleep(1)
        duration = play_video_in_chaoxing(wd)
        time.sleep(0.5)
        dati(duration)
        # 等待视频时长
        time.sleep(0.5)
        # wd.find_element(By.XPATH, f'//span[@title="{video_1}"]').click()
        # time.sleep(5)
        # play_video_in_chaoxing(wd)
        wd.close()  # 关闭


        #下一行text.json
        x = x + 1
    else:
        print("ご主人さま，所有任务已完成！")
        input()






























































































































































































































































































input()