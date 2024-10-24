import os
import json

# 设置文件夹路径
img_folder = os.path.join(os.getcwd(), 'img')

# 生成 JSON 结构
data = {
    "name": "App Store ICON",
    "description": "图标来自苹果商店，144px",
    "icons": []
}

# 遍历 img 文件夹
for filename in os.listdir(img_folder):
    if filename.endswith('.png'):
        icon = {
            "name": filename,
            "url": f"https://raw.githubusercontent.com/huskydsb/icon/main/img/{filename}"
        }
        data["icons"].append(icon)

# 输出 JSON 到文件
output_file = os.path.join(os.getcwd(), 'icons.json')
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"JSON 文件已生成: {output_file}")
