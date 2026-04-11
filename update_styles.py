import os
import glob
import re

new_style = """
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        :root { 
            --bg: #b2e0f6; 
            --brown-deep: #4a2e1c; 
            --pink-pastel: #4a8cb0; 
            --purple-royal: #5992bd; 
            --text-color: #2d1c0b; 
        }
        html { scroll-behavior: smooth; }
        body { 
            font-family: 'Lora', serif; 
            line-height: 1.8; 
            color: var(--text-color); 
            background-color: #016180; 
            padding: 40px 20px; 
            background-image: radial-gradient(circle, #4a8cb0 1px, transparent 1px), radial-gradient(circle, #4a8cb0 1px, transparent 1px);
            background-size: 60px 60px; 
            background-position: 0 0, 30px 30px; 
            background-attachment: fixed; 
        }
        .wrap { 
            max-width: 900px; 
            margin: 0 auto; 
            background: var(--bg); 
            border-radius: 12px; 
            padding: 40px; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.1); 
        }
        header.article-header { 
            background: transparent;
            padding: 0 0 20px 0; 
            margin-bottom: 30px; 
            border-bottom: 3px solid var(--pink-pastel); 
            text-align: center; 
            box-shadow: none;
            border-radius: 0;
        }
        .back-nav { 
            font-family: 'Lora', serif; 
            text-decoration: none; 
            color: var(--brown-deep); 
            font-weight: bold; 
            font-size: 1rem; 
            display: inline-block; 
            margin-bottom: 20px; 
            transition: all 0.2s; 
            text-transform: uppercase;
        }
        .back-nav:hover { color: #fff; text-decoration: underline; transform: none; }
        h1 { 
            font-family: 'Lora', serif; 
            font-size: clamp(2rem, 5vw, 2.6rem); 
            font-weight: 600; 
            color: var(--brown-deep); 
            line-height: 1.3; 
            margin-bottom: 16px; 
            letter-spacing: -0.5px; 
        }
        .date, .meta { 
            color: #4a2e1c; 
            font-size: 1.1rem; 
            display: flex; 
            justify-content: center; 
            gap: 16px; 
            font-style: italic; 
            margin-bottom: 0;
        }
        main.wrap { margin-top: 0; background: transparent; padding: 0; box-shadow: none; }
        article { padding: 12px 0; background: var(--bg); border-radius: 12px; padding: 40px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        article h2 { 
            font-family: 'Lora', serif; 
            font-size: 1.5rem; 
            font-weight: 600; 
            color: var(--brown-deep); 
            margin-top: 0px; 
            margin-bottom: 15px; 
            padding-top: 0; border-top: none; padding-left: 0;
        }
        article h3 { font-family: 'Lora', serif; font-size: 1.3rem; color: var(--purple-royal); margin-top: 32px; margin-bottom: 16px; }
        article p { margin-bottom: 20px; font-size: 1.1rem; line-height: 1.85; text-indent: 1.5em; }
        article p.no-indent { text-indent: 0; }
        em { color: var(--purple-royal); font-style: italic; }
        blockquote, article blockquote { 
            font-style: normal; 
            margin: 30px 40px; 
            color: #4a2e1c; 
            background: #e0f2fe; 
            padding: 25px; 
            border-left: 10px solid #4c2c17; 
            border-radius: 5px; 
            font-size: 1.1rem; 
            text-indent: 0; 
        }
        footer { margin-top: 60px; padding-top: 30px; text-align: center; font-family: 'Lora', serif; font-size: 0.85rem; color: var(--bg); border-top: 1px solid var(--pink-pastel); font-weight: 400; }
        @media (max-width: 640px) {
            header.article-header, main.wrap { padding: 24px; border-width: 0; box-shadow: none; }
            .wrap { margin: 10px; border-radius: 8px; }
            h1 { font-size: 1.8rem; }
            article h2 { font-size: 1.4rem; }
        }
    </style>
"""

# Process all .html files in the blogs directory
for filepath in glob.glob("/Users/roxy/Documents/GitHub/roxy-portfolio/blogs/*.html"):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace style tags
    new_content = re.sub(r'<style>.*?</style>', new_style.strip(), content, flags=re.DOTALL)
    
    with open(filepath, 'w') as f:
        f.write(new_content)
        
print("Updated styles for all blog html files!")
