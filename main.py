import os
from openai import OpenAI
from PIL import Image
import pytesseract
import requests

# 设置 Tesseract 的安装路径（Windows 需要）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 初始化客户端
client = OpenAI(
    api_key="75aaa5837e148b567ba15405e9a5422f97c1d0b6",  # 替换为你的星河大模型 API Key
    base_url="https://aistudio.baidu.com/llm/lmapi/v3"  # 星河大模型的 API 域名
)

def extract_text_from_image(image_path):
    """
    使用 OCR 从图片中提取文字
    """
    try:
        # 打开图片
        image = Image.open(image_path)
        # 使用 pytesseract 提取文字
        text = pytesseract.image_to_string(image, lang='chi_sim')  # 中文识别
        return text.strip()  # 去除空白字符
    except Exception as e:
        return None  # 如果提取失败，返回 None

def describe_image(image_path):
    """
    使用百度图像描述 API 描述图片内容
    """
    # 百度图像描述 API 的 URL 和 API Key
    api_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/image_classify/image_description"
    access_token = "75aaa5837e148b567ba15405e9a5422f97c1d0b6"  # 替换为你的百度 Access Token

    # 读取图片
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    # 发送请求
    headers = {"Content-Type": "application/json"}
    params = {"access_token": access_token}
    response = requests.post(api_url, headers=headers, params=params, data=image_data)

    # 解析响应
    if response.status_code == 200:
        result = response.json()
        return result.get("result", {}).get("description", "无法描述图片内容")
    else:
        return f"描述图片时出错：{response.status_code}, {response.text}"

def deepseek_generate(prompt):
    """
    使用 DeepSeek 生成文本
    """
    try:
        response = client.chat.completions.create(
            model="ernie-3.5-8k",  # 替换为支持的模型名称
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200  # 控制生成文本的最大长度
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"生成文本时出错：{e}"

def generate_advertisement(image_path):
    """
    根据图片内容生成广告文案
    """
    # 提取图片中的文字
    image_text = extract_text_from_image(image_path)

    # 如果图片中没有文字，描述图片内容
    if not image_text:
        print("图片中没有文字，正在描述图片内容...")
        image_text = describe_image(image_path)

    # 生成广告文案
    text_prompt = f"请根据以下图片内容生成一段广告文案：{image_text}"
    ad_text = deepseek_generate(text_prompt)

    return f"🖼️ 图片内容：{image_text}\n📢 广告文案：{ad_text}"

def process_folder(folder_path):
    """
    处理文件夹中的所有图片并生成广告文案
    """
    # 获取文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否为图片
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(folder_path, filename)
            print(f"处理图片: {filename}")
            print(generate_advertisement(image_path))
            print("-" * 50)

# 处理文件夹中的图片
folder_path = "D:/model/input"  # 替换为你的文件夹路径
process_folder(folder_path)