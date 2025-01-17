import random
import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

# 随机生成姓名、性别和手机号码
def generate_random_name():
    first_names = [
        "李", "王", "张", "刘", "陈", "杨", "赵", "黄", "周", "吴",
        "郑", "谢", "孙", "胡", "林", "郭", "何", "高", "马", "罗",
        "宋", "邓", "朱", "沈", "杨", "冯", "邱", "郑", "卢", "韦",
        "潘", "蒋", "蔡", "杜", "汪", "袁", "常", "郭", "冯", "崔",
        "邵", "汪", "朱", "邱", "许", "郑", "陶", "吕", "何", "周"
    ]
    
    last_names = [
        "晗曦", "天骐", "梓睿", "龙德", "芯玥", "姝慧", "鸿远", "宇彤", "泓杉", "梓鹤",
        "硕元", "郁星", "悠乐", "清玥", "泽然", "鸿羽", "丞浩", "珑皓", "江雨", "胤瀚",
        "禹彰", "明宸", "艺龙", "一怡", "润泰", "皓铭", "彬硕", "煊芸", "天名", "梦浩",
        "丰瑞", "烨菲", "惠琳", "雨希", "泽彦", "梦婕", "博润", "歆慕", "浩婷", "姝妍",
        "宸瑶", "子诺", "楷乐", "书芳", "清月", "弈安", "紫凌", "可颜", "卓阳", "亦妍",
        "宇权", "远昊", "芝莹", "煊涵", "琨钦", "卓宁", "宸雨", "小丽", "腾宇", "槿泽"
    ]
    
    return random.choice(first_names) + random.choice(last_names)

# 随机生成创业项目的评价内容
def generate_random_feedback():
    feedback_options = [
        "这个创业项目的创意非常新颖，值得关注。",
        "项目的执行速度非常快，期待早日上线。",
        "团队的努力和创新精神非常值得赞扬。",
        "非常看好这个项目的未来发展，期待更多的成果。",
        "这个创意非常有潜力，期待它能带来行业的变革。",
        "项目的创新性和市场需求匹配度很高。",
        "团队的执行力非常强，能够迅速推进项目。",
        "这个项目的商业模式很清晰，值得投资。",
        "从创意到实施的每一步都非常精彩，期待更多。",
        "这是一个非常有前景的创业项目，希望能够成功。",
        "团队非常有激情，对这个项目非常有信心。",
        "项目的商业价值巨大，值得关注。",
        "这个创意非常符合市场需求，期待能够尽快推出。",
        "这个项目的思路很独特，有望成为行业的领跑者。",
        "团队的协作精神非常强，执行力很高。",
        "这个项目非常符合当下趋势，应该能够快速成长。",
        "从创意到执行都很到位，未来可期。",
        "这个项目的潜力无限，已经有了初步的成功迹象。",
        "创意和执行兼备，是一个非常有竞争力的项目。",
        "这个创业项目的方向非常明确，市场前景广阔。",
        "期待这个项目能够顺利上线，并快速获得市场份额。",
        "团队在市场分析和产品设计方面做得非常好。",
        "项目的创新性和实用性非常突出，值得期待。",
        "这个项目非常有价值，市场需求很大。",
        "很高兴看到这么有创意的创业项目，希望能成功。",
        "创意非常棒，希望能够得到更多的支持。",
        "这个项目的商业模式非常清晰，非常有前景。",
        "团队做得很好，能够快速解决市场痛点。",
        "这个项目的方向非常对，市场非常看好。",
        "项目的创意非常符合时代潮流，非常值得投资。",
        "期待项目能够在短期内获得突破性进展。",
        "团队的执行力非常强，项目进展非常迅速。",
        "这个项目的创意非常有吸引力，值得深入了解。",
        "项目的市场定位非常精准，前景可期。",
        "这个创业项目的创意值得推广，市场需求大。",
        "非常期待这个项目能够顺利上线并获得成功。",
        "项目的创新性让人眼前一亮，期待更多的惊喜。",
        "这个创业项目有很强的社会影响力，值得关注。",
        "团队对市场的理解非常透彻，执行力也非常到位。",
        "这个项目的商业模式非常合理，市场前景广阔。",
        "非常看好这个创业项目的未来，期待早日看到成果。",
        "这个项目的构思非常独特，商业潜力巨大。",
        "团队在项目实施过程中表现非常专业，值得信赖。",
        "项目的创意非常有吸引力，市场反响很好。",
        "项目的推进速度很快，未来可期。",
        "这是一个非常有潜力的创业项目，期待它能够成功。",
        "项目的创意非常值得推广，市场前景非常乐观。",
        "团队非常有经验，相信这个项目能够成功。"
    ]
    
    return random.choice(feedback_options)

def generate_random_phone():
    return random.choice(["135", "138"]) + ''.join([str(random.randint(0, 9)) for _ in range(8)])

# 设置Selenium的Chrome WebDriver
def setup_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1200x800")  # 设置窗口大小
    # 使用 webdriver_manager 自动下载和配置 Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# 滚动到元素
def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView();", element)

# 安全点击
def safe_click(driver, element):
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element))
        scroll_to_element(driver, element)
        ActionChains(driver).move_to_element(element).click().perform()
        time.sleep(0.5)  # 等待点击完成
    except Exception as e:
        print(f"点击元素时发生错误: {e}")
        time.sleep(1)

# 等待元素可见并可交互，最多重试3次
def wait_for_element(driver, by, value, timeout=10, retries=3):
    retry = 0
    while retry < retries:
        try:
            element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
            return element
        except Exception as e:
            retry += 1
            print(f"等待元素失败，重试 {retry}/{retries}... 错误: {e}")
            time.sleep(0.5)
    print(f"未能找到元素: {value}")
    return None

# 自动填写问卷的函数
def fill_questionnaire(url, num_surveys, completed_surveys):
    driver = setup_chrome_driver()  # 每次开始填写问卷前重新初始化浏览器
    driver.get(url)
    time.sleep(2)

    # 随机生成姓名、性别、手机号码
    name = generate_random_name()
    phone = generate_random_phone()

    # 填写姓名
    name_input = wait_for_element(driver, By.ID, "name", timeout=10)
    name_input.send_keys(name)
    print(f"填写姓名: {name}")

    # 选择“我是他的”下拉选项
    relationship_select = Select(wait_for_element(driver, By.ID, "relation", timeout=10))
    relationship_select.select_by_visible_text(random.choice(["同学", "朋友", "老师"]))
    print("选择关系")

    # 选择性别
    gender_select = Select(wait_for_element(driver, By.ID, "sex", timeout=10))
    gender_select.select_by_visible_text(random.choice(["男", "女"]))
    print("选择性别")

    # 填写手机号码
    phone_input = wait_for_element(driver, By.ID, "phone", timeout=10)
    phone_input.send_keys(phone)
    print(f"填写手机号码: {phone}")

    # 点击确认信息按钮
    confirm_button = wait_for_element(driver, By.XPATH, "/html/body/div[2]/div[2]/div[5]/img", timeout=10)
    safe_click(driver, confirm_button)
    print("点击确认信息")

    # 点击开始评估按钮
    start_button = wait_for_element(driver, By.XPATH, "/html/body/div[2]/div[2]/img", timeout=10)
    safe_click(driver, start_button)
    print("点击开始评估")

    # 填写所有选项为A（针对每个问题）
    for i in range(1, 26):  # 假设有25个问题
        question_xpath = f"/html/body/div[3]/div[3]/div[{i}]/div[2]/label[1]"
        option = wait_for_element(driver, By.XPATH, question_xpath, timeout=10)
        if option:
            safe_click(driver, option)
            print(f"选择第{i}题的A选项")
        else:
            print(f"未能找到第{i}题的A选项")

    # 填写更多建议
    suggestion_input = wait_for_element(driver, By.XPATH, "/html/body/div[2]/div[1]/textarea", timeout=10)
    if suggestion_input and suggestion_input.is_enabled() and suggestion_input.is_displayed():
        scroll_to_element(driver, suggestion_input)
        pinjia = generate_random_feedback()
        suggestion_input.send_keys(pinjia)
        print("填写建议:", pinjia)
    else:
        print("评价输入框不可交互或不可见")

    # 提交问卷
    submit_button = wait_for_element(driver, By.XPATH, "/html/body/div[2]/div[2]/img", timeout=10)
    safe_click(driver, submit_button)
    print("提交问卷")

    # 更新已填写问卷数量
    completed_surveys[0] += 1
    print(f"已填写问卷数量: {completed_surveys[0]}")

    # 关闭浏览器
    driver.quit()
    print("关闭浏览器")

# 多线程执行填问卷
def start_multiple_surveys(url, total_surveys, max_threads=3):
    completed_surveys = [0]  # 使用列表存储已填写的问卷数量

    def worker():
        while completed_surveys[0] < total_surveys:
            fill_questionnaire(url, total_surveys, completed_surveys)
            time.sleep(1)

    threads = []
    for _ in range(min(max_threads, total_surveys)):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# 询问用户需要填写的问卷数量
total_surveys = int(input("请输入总共需要填写的问卷数量: "))
survey_url = input("请输入问卷链接: ")

# 启动多个窗口并行执行
start_multiple_surveys(survey_url, total_surveys)
