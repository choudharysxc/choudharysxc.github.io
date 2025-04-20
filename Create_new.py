import os
from datetime import datetime

file_name = input("Enter Blog name: ") + '.html'
title = input("Title the blog: ")
choose_theme = int(input("Enter theme (1-2): "))

# You can add more themes later if you'd like
if choose_theme == 1:
    css = """
    @import url('https://fonts.googleapis.com/css2?family=Shadows+Into+Light&display=swap');

    html, body {
      margin: 0;
      padding: 0;
      overflow: hidden;
      height: 100%;
      background-color:#FFD87C;
    }

    .whole {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      position: relative;
      z-index: 1;
      padding: 10px;
    }

    .greetings {
      color: #475841;
      font-size: 5vw;
      font-family: "Shadows Into Light", cursive;
      margin-bottom: 30px;
      text-align: center;
    }

    @media (max-width: 600px) {
      .greetings {
        font-size: 6vw;
      }
    }
    """
else:
    css = """@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,500&family=Roboto+Mono&display=swap');

html, body {
  margin: 0;
  padding: 0;
  background: linear-gradient(to bottom, #f9f5ef, #d7eafc);
  font-family: 'Playfair Display', serif;
  color: #4a4a4a;
  height: 100%;
  overflow-x: hidden;
}

body::before {
  content: "";
  position: fixed;
  top: 0; left: 0;
  width: 100%;
  height: 100%;
  background: url('https://i.imgur.com/o1LGLTp.png') no-repeat center center;
  background-size: cover;
  opacity: 0.08;
  z-index: -1;
}

.whole {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 4vh 5vw;
  min-height: 100vh;
}

.greetings {
  font-size: 3rem;
  margin-bottom: 1rem;
  text-align: center;
  color: #3e3e3e;
  font-style: italic;
  letter-spacing: 1px;
}

.timestamp {
  font-family: 'Roboto Mono', monospace;
  font-size: 0.9rem;
  color: #8b8b8b;
  margin-bottom: 2rem;
}

.blog-content {
  font-size: 1.2rem;
  max-width: 800px;
  line-height: 1.7;
  text-align: justify;
  background-color: rgba(255,255,255,0.7);
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0,0,0,0.06);
}

@media (max-width: 768px) {
  .greetings {
    font-size: 2rem;
  }

  .blog-content {
    padding: 1.2rem;
    font-size: 1rem;
  }
}
"""

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d ~ %H:%M:%S")

if not os.path.exists(f"Blog/{file_name}"):
    with open(file_name, 'w+') as file:
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
else:
	print("New name needed hero ... :-(")

