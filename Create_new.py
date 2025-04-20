import os
from datetime import datetime

file_name = input("Enter Blog name: ") + '.html'
title = input("Title the blog: ")
choose_theme = int(input("Enter theme (1-2): "))

# === Themes ===
if choose_theme == 1:
    css = """   """
else:
    css = """   """

# === Timestamp ===
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d ~ %H:%M:%S")

# === Make sure Blog directory exists ===
blog_dir = "Blogs"
os.makedirs(blog_dir, exist_ok=True)  # Create if not exists

# === Full path to the new blog file ===
file_path = os.path.join(blog_dir, file_name)

# === File Creation ===
if not os.path.exists(file_path):
    with open(file_path, 'w+', encoding='utf-8') as file:
        file.write(f"""<!DOCTYPE html>
<html lang="en">
<head> 
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>{css}</style>
</head>
<body>
    <div class="whole">
        <div class="greetings">
            <h1>{title}</h1>
        </div>
        <div class="timestamp">
            <p><em>Written on: {timestamp}</em></p>
        </div>
        <div class="blog-content">
            <p>Write down, son... your thoughts are windborne letters sealed in time.</p>
        </div>
    </div>
</body>
</html>
""")
    print(f"Blog created successfully ➜ {file_path}")
else:
    print("New name needed hero ... :-(")
