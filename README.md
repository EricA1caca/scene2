# scene2
This project is an automation tool designed to generate advertising copy by analyzing the content of images.
# 基于图像内容生成广告文案的工具

## 项目简介
本项目是一个自动化工具，旨在通过分析图片内容生成广告文案。它结合了OCR（光学字符识别）、图像描述和自然语言生成技术，能够从图片中提取文字或描述图片内容，并基于这些信息生成相关的广告文案。适用于广告创意、电商平台、社交媒体等多种场景。

## 主要功能
1. **OCR文字提取**：
   - 使用 `pytesseract` 库从图片中提取文字，支持中文识别。
   - 如果图片中没有文字，系统会自动调用图像描述功能。

2. **图像内容描述**：
   - 使用百度的图像描述 API 对图片内容进行描述，生成简短的文字说明。
   - 该功能适用于没有文字的图片，确保系统能够理解图片内容。

3. **广告文案生成**：
   - 使用 DeepSeek 或类似的自然语言生成模型，根据提取的文字或图像描述生成广告文案。
   - 生成的文案可以根据图片内容进行定制，适用于广告、营销等场景。

4. **批量处理**：
   - 支持批量处理文件夹中的图片，自动为每张图片生成广告文案。
   - 用户可以指定文件夹路径，系统会自动遍历文件夹中的所有图片文件。

## 技术栈
- **OCR**：使用 `pytesseract` 进行文字提取，支持多语言（尤其是中文）。
- **图像描述**：调用百度的图像描述 API 对图片内容进行描述。
- **自然语言生成**：使用 DeepSeek 或类似的模型生成广告文案。
- **Python 库**：
  - `PIL`：用于图片处理。
  - `requests`：用于发送 HTTP 请求。
  - `openai`：用于与自然语言生成模型交互。

## 使用方法

### 1. 安装依赖
首先，确保你已经安装了 Python 3.x，然后安装所需的 Python 库：

```bash
pip install pillow pytesseract requests openai


运行步骤

1. 配置 Tesseract OCR

Windows 用户：需要安装 Tesseract OCR，并设置正确的路径。可以在代码中修改以下路径：
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

Linux/Mac 用户：可以通过包管理器安装 Tesseract，例如：
sudo apt-get install tesseract-ocr


2. 配置 API 密钥

替换代码中的 api_key 和 access_token，使用你自己的百度 API 和 DeepSeek API 密钥。
api_key = "你的星河大模型 API Key"
access_token = "你的百度 Access Token"


3. 运行脚本
指定包含图片的文件夹路径，运行脚本即可批量生成广告文案。
python main.py


##生成结果展示

以下是基于图片内容生成的广告文案示例：
处理图片: example.jpg
🖼️ 图片内容：这是一张展示美丽风景的图片，有蓝天白云和绿色的草地。
📢 广告文案：感受大自然的魅力！蓝天白云与绿草如茵，带你逃离城市的喧嚣，享受宁静与美好。快来体验这片纯净的自然风光吧！

--------------------------------------------------

代码结构

image-to-ad/
│── .gitignore
│── LICENSE
│── README.md
│── main.py
│── requirements.txt
