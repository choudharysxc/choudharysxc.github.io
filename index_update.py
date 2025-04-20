import os
from bs4 import BeautifulSoup

# Step 1: Get all .html files in Blogs dir except 'main.html'
blog_dir = 'Blogs'
all_files = os.listdir(blog_dir)
blog_files = [file for file in all_files if file.endswith('.html') and file.lower() != 'main.html']

# Step 2: Open and parse main.html
main_path = os.path.join(blog_dir, 'main.html')
with open(main_path, 'r+', encoding='utf-8') as H:
    soup = BeautifulSoup(H, 'html.parser')
    
    # Step 3: Find the <ul> element (assuming there's only one)
    ul = soup.find('ul')
    if ul:
        ul.clear()  # wipe the current contents

        for blog in blog_files:
            blog_name = os.path.splitext(blog)[0].replace('_', ' ').title()
            li = soup.new_tag('li')
            a = soup.new_tag('a', href=blog, style="text-decoration: none; color:#475841")
            a.string = blog_name
            li.append(a)
            ul.append(li)
    
    # Step 4: Write the modified HTML back
    H.seek(0)
    H.write(str(soup))
    H.truncate()

print("Updated main.html with blog links:")
print(blog_files)
