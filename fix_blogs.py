import re
import glob

nav_header = """
    <header style="padding: 50px 50px 30px 50px; background: rgb(181, 212, 250); text-align: center; margin: 0; position: sticky; top: 0; z-index: 1000; border-bottom: 5px solid var(--pink-pastel);">
        <h1 style="font-family: 'Fascinate', cursive; font-size: 50px; color: var(--brown-deep);">Roxy Alexander</h1>
        <h2 style="font-style: italic; font-size: 20px; font-weight: 400; color: var(--text-color); margin-bottom: 16px;">Writing</h2>
        <nav role="navigation" aria-label="Site navigation" style="margin-top: 20px;">
            <a href="../index.html" style="text-decoration: none; color: var(--text-color); font-weight: bold; padding: 0 14px; display: inline-block;">Home</a>
            <a href="../about.html" style="text-decoration: none; color: var(--text-color); font-weight: bold; padding: 0 14px; display: inline-block;">About</a>
            <a href="../research.html" style="text-decoration: none; color: var(--text-color); font-weight: bold; padding: 0 14px; display: inline-block;">Research</a>
            <a href="../writing.html" style="text-decoration: none; color: var(--text-color); font-weight: bold; padding: 0 14px; display: inline-block;">Writing</a>
            <a href="../resources.html" style="text-decoration: none; color: var(--text-color); font-weight: bold; padding: 0 14px; display: inline-block;">Resources</a>
            <a href="../podcast.html" style="text-decoration: none; color: var(--text-color); font-weight: bold; padding: 0 14px; display: inline-block;">Podcast</a>
            <a href="../index.html#contact" style="text-decoration: none; color: var(--text-color); font-weight: bold; padding: 0 14px; display: inline-block;">Contact</a>
        </nav>
        <hr style="border: none; border-top: 3px solid var(--pink-pastel); margin-top: 10px;">
    </header>
"""

fascinate_font = '<link href="https://fonts.googleapis.com/css2?family=Fascinate&display=swap" rel="stylesheet">'

for filepath in glob.glob("/Users/roxy/Documents/GitHub/roxy-portfolio/blogs/*.html"):
    with open(filepath, "r") as f:
        content = f.read()

    # Add Fascinate font link
    if "Fascinate" not in content and "</head>" in content:
        content = content.replace("</head>", f"    {fascinate_font}\n</head>")

    # Add general navigation header right after <body>
    if "Site navigation" not in content and "<body>" in content:
        content = content.replace("<body>", f"<body>\n{nav_header}")

    with open(filepath, "w") as f:
        f.write(content)

print("Updated blogs with top navigation header.")
