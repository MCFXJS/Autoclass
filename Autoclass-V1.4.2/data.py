from datetime import time
import pyautogui
import selenium
import time
import random
import json
import requests
from bs4 import BeautifulSoup
# 作用：导入浏览器驱动核心功能
# 用途：创建浏览器对象
from selenium import webdriver
# 作用：导入键盘按键功能
# 用途：模拟键盘操作
# # 模拟按回车键
from selenium.webdriver.common.by import By
# 作用：导入元素定位方式
# 用途：告诉 Selenium 用什么方式找元素
# # By 提供了多种定位方式
from selenium.webdriver.support.ui import WebDriverWait
# 作用：导入显式等待功能
#
# 用途：等待元素出现后再操作
#
# python
# # 最多等待10秒，直到元素出现
from selenium.webdriver.support import expected_conditions as EC

# 适配Google驱动
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# 导入提取课程所需的库
import re
from urllib.parse import urlparse, parse_qs


def extract_course_names_from_html(html_content):
    """
    使用BeautifulSoup从HTML中提取所有课程名称
    提取规则：查找所有 class="posCatalog_name" 的span标签中的title属性值
    不提取单元标题 (class="posCatalog_title")
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # 查找所有 class="posCatalog_name" 的span标签（这是课程标签）
    course_spans = soup.find_all('span', class_='posCatalog_name')

    # 提取title属性值（课程名称）
    course_names = []
    for span in course_spans:
        title = span.get('title')
        if title:  # 确保title存在
            title = title.strip()
            if title:  # 排除空字符串
                course_names.append(title)

    return course_names


def extract_course_names_from_page_source(driver):
    """
    从当前浏览器页面源码中提取课程名称
    使用Selenium获取页面源码，然后用BeautifulSoup解析
    """
    # 获取当前页面源码
    page_source = driver.page_source

    # 使用BeautifulSoup解析
    soup = BeautifulSoup(page_source, 'html.parser')

    # 查找所有 class="posCatalog_name" 的span标签
    course_spans = soup.find_all('span', class_='posCatalog_name')

    # 提取title属性值
    course_names = []
    for span in course_spans:
        title = span.get('title')
        if title:
            title = title.strip()
            if title:
                course_names.append(title)

    return course_names


def save_courses_to_files(text_names, text_file='text.json'):
    """
    保存课程名称到文件
    text_file: 文本文件，每行一门课，顶格写
    """
    # 保存为文本格式（每行一门课，顶格写）
    with open(text_file, 'w', encoding='utf-8') as f:
        for name in text_names:
            f.write(name + '\n')

    print(f"✓ 已保存 {len(text_names)} 门课程到 {text_file}")


    return True


def print_courses(text_names):
    """打印所有课程名称"""
    print(f"\n共找到 {len(text_names)} 门课程：")
    print("-" * 50)
    for name in text_names:
        print(name)
    print("-" * 50)


def wait_for_page_load(driver, timeout=30):
    """
    等待页面加载完成
    """
    try:
        WebDriverWait(driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        return True
    except:
        print("页面加载超时")
        return False


def scroll_to_load_courses(driver, max_scrolls=5):
    """
    滚动页面以加载所有课程（如果页面是动态加载的）
    """
    for i in range(max_scrolls):
        # 滚动到页面底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        # 检查是否还有更多内容
        new_height = driver.execute_script("return document.body.scrollHeight")
        old_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == old_height:
            break



#########################################################################################################################################

print("ご主人さま,请输入学习通要抓取单个学科下课程的网页地址","data.exe文件用于将课程名称标签（title）自动编辑鱼text.json中")
print("例如（请不要复制这个，这个只是例子）：https://mooc1.chaoxing.com/mycourse/studentstudy?chapterId=705032039&courseId=262336996&clazzid=143937452&cpi=490971353&enc=3f81db8d9162e31198db167256413961&mooc2=1&hidetype=0&openc=c44a08b1d065c90c0fef6b4b717d8494")
url = input()
print("输入学习通手机号")
Phone_number = input()
print("输入密码")
Password = input()

while True:
    print("请选择驱动", 'Edge浏览器输入1(建议),Google Chrome输入2')
    Chrome_1 = input()
    if Chrome_1 == '1':
        wd = webdriver.Edge()
        print('已选择Edge')
        time.sleep(0.2)
        break
    elif Chrome_1 == '2':
        service = Service(ChromeDriverManager().install())
        wd = webdriver.Chrome(service=service)
        print('已选择Google Chrome')
        time.sleep(2)
        break
    else:
        print('没有这个驱动选项')

time.sleep(1)


def inputNM():
    # 窗口大小
    wd.set_window_size(1300, 1600)
    time.sleep(1)
    # 元素有明确的 id	By.ID,
    # 需要通过 class 查找	By.CSS_SELECTOR
    input_list = wd.find_element(By.ID, 'phone')
    input_list2 = wd.find_element(By.ID, 'pwd')
    print(input_list)
    time.sleep(0.5)
    input_list.send_keys(Phone_number)
    time.sleep(0.1)
    input_list2.send_keys(Password)
    time.sleep(0.1)
    # 确认密码回车
    # wd内核,在网页中找到第一个 <button> 标签元素，然后点击它。click()运行
    wd.find_element(By.CSS_SELECTOR, 'button').click()
    time.sleep(5)


# 以上皆为登录
time.sleep(1)  # 等待登录跳转完成

# 正式打开运行
wd.get(url)
inputNM()
time.sleep(3)  # 等待页面加载






#课程抓取#####################################################################################
print("\n" + "=" * 60)
print("开始抓取课程列表...")
print("=" * 60)

# 等待页面完全加载
wait_for_page_load(wd, 30)

# 可选：滚动页面以加载所有课程（如果页面是动态加载的）
print("正在滚动页面加载所有课程...")
scroll_to_load_courses(wd, max_scrolls=5)

# 等待目录树加载完成
try:
    # 等待课程目录元素出现
    WebDriverWait(wd, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "posCatalog_name"))
    )
    print("✓ 课程目录加载成功")
except:
    print("等待超时，可能部分课程未加载")

# 方法1：直接从当前页面源码提取
print("\n正在从当前页面提取课程名称...")
text_names = extract_course_names_from_page_source(wd)

if text_names:
    print_courses(text_names)
    save_courses_to_files(text_names, 'text.json')
else:
    print("未从当前页面提取到课程，尝试获取完整章节页面...")

    # 方法2：如果当前页面没有，尝试获取章节列表页面
    try:
        # 查找目录树容器
        catalog_tree = wd.find_element(By.CLASS_NAME, "posCatalog")
        if catalog_tree:
            # 展开所有章节
            try:
                # 点击展开所有章节的按钮（如果有）
                expand_buttons = wd.find_elements(By.CSS_SELECTOR, ".posCatalog_title")
                for button in expand_buttons:
                    try:
                        button.click()
                        time.sleep(0.3)
                    except:
                        pass
            except:
                pass

            time.sleep(2)

            # 重新提取
            text_names = extract_course_names_from_page_source(wd)

            if text_names:
                print_courses(text_names)
                save_courses_to_files(text_names, 'text.json')
            else:
                print("仍然未找到课程数据")
    except Exception as e:
        print(f"提取失败: {e}")

# 方法3：使用requests直接请求章节API（备用方案）
if not text_names:
    print("\n尝试使用备用方案获取数据...")

    try:
        # 获取当前页面的cookie
        cookies = wd.get_cookies()
        cookie_dict = {cookie['name']: cookie['value'] for cookie in cookies}

        # 从当前URL获取参数
        current_url = wd.current_url
        parsed_url = urlparse(current_url)
        params = parse_qs(parsed_url.query)

        course_id = params.get('courseId', ['262336996'])[0]
        clazz_id = params.get('clazzid', ['143937452'])[0]
        cpi = params.get('cpi', ['490971353'])[0]

        # 构建章节列表API URL
        chapter_url = f"https://mooc2-ans.chaoxing.com/mooc2-ans/mycourse/stu?courseid={course_id}&clazzid={clazz_id}&cpi={cpi}&pageHeader=1"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        response = requests.get(chapter_url, headers=headers, cookies=cookie_dict, timeout=10)
        response.encoding = 'utf-8'

        if response.status_code == 200:
            text_names = extract_course_names_from_html(response.text)
            if text_names:
                print_courses(text_names)
                save_courses_to_files(text_names, 'text.json')
            else:
                print("备用方案也未找到课程数据")
        else:
            print(f"备用方案请求失败: {response.status_code}")
    except Exception as e:
        print(f"备用方案出错: {e}")

print("\n" + "=" * 60)
print("抓取完成！")
print("生成的文件：")
print("  - text.json (文本格式，每行一门课)")
print("=" * 60)

# 保持浏览器打开，方便查看
print("\n浏览器将保持打开状态，按回车键关闭浏览器并退出...")
input()

# 关闭浏览器
wd.quit()




