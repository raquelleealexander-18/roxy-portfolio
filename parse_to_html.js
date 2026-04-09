const fs = require('fs');

const input = fs.readFileSync('Built World, Built Knowledge.txt', 'utf8');

const paragraphs = input.split('\n').map(p => p.trim()).filter(p => p.length > 0);

let htmlContent = '';

for (let i = 0; i < paragraphs.length; i++) {
    const p = paragraphs[i];
    if (p === 'Oppression is driven not by individual, unconscious syndromes but by social ideologies that are embodied, and precisely because ideologies are embodied, their effects are readable, and must be read, in the construction and history of societies.') {
        htmlContent += `<blockquote>${p}<br><cite>Siebers 2008, 32</cite></blockquote>\n\n`;
        i++; // skip 'Siebers 2008, 32'
    } else if (p.startsWith('Introduction') || p.startsWith('Section One:') || p.startsWith('Section Two:') || p.startsWith('Section Three:') || p.startsWith('Section Four:') || p.startsWith('Conclusion') || p.startsWith('Bibliography')) {
        htmlContent += `<h2>${p}</h2>\n\n`;
    } else if (p === '“Knowledge is socially situated […] Identities are socially constructed […] Some bodies are excluded by dominant social ideologies […]”' || p.includes('Knowledge is socially situated') || p.includes('Tobin 2008, 33')) {
        if (p.includes('Tobin 2008, 33')) {
            // Already handled
        } else {
            htmlContent += `<blockquote>${p}<br><cite>Tobin 2008, 33</cite></blockquote>\n\n`;
            i++; 
        }
    } else if (p.startsWith('Built Worlds, Built Knowledge') || p.startsWith('By Roxy Alexander') || p === '1' || p.includes('---------------') || p === 'Built Worlds, Built Knowledge: Disability, Space, and Epistemic Exclusion' || p === 'By Roxy Alexander') {
        // Skip metadata at bottom
    } else if (p.startsWith('FIGURE 1:')) {
        htmlContent += `<figure>\n  <img src="images/capitol-crawl.jpg" alt="The Capitol Crawl">\n  <figcaption>${p}</figcaption>\n</figure>\n\n`;
    } else if (p.match(/^1\s+“A ‘place of public accommodation’”/)) {
        htmlContent += `<div class="footnotes"><p id="footnote-1"><strong>1:</strong> ${p.substring(2)}</p></div>\n\n`;
    } else if (p.startsWith('[RA1]')) {
        htmlContent += `<div class="footnotes"><p id="footnote-ra1"><strong>[RA1]:</strong> ${p.substring(5)}</p></div>\n\n`;
    } else if (p.startsWith('[RA2]')) {
        htmlContent += `<div class="footnotes"><p id="footnote-ra2"><strong>[RA2]:</strong> ${p.substring(5)}</p></div>\n\n`;
    } else {
        htmlContent += `<p>${p}</p>\n\n`;
    }
}

const template = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Built Worlds, Built Knowledge | Roxy Alexander</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="description" content="Extending genealogical disability theory into social epistemology by demonstrating how built environments themselves can enact epistemic oppression." />
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400..700;1,400..700&family=Titan+One&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    :root { --bg: #b2e0f6; /* Matching the portfolio style */ --brown-deep: #4a2e1c; --pink-pastel: #4a8cb0; --purple-royal: #5992bd; --text-color: #2d1c0b; }
    html { scroll-behavior: smooth; }
    body { font-family: 'Lora', serif; line-height: 1.8; color: var(--text-color); background-color: #016180; padding: 40px 20px; 
           background-image: radial-gradient(circle, #4a8cb0 1px, transparent 1px), radial-gradient(circle, #4a8cb0 1px, transparent 1px);
           background-size: 60px 60px; background-position: 0 0, 30px 30px; background-attachment: fixed; }
    .wrap { max-width: 900px; margin: 0 auto; background: var(--bg); border-radius: 12px; padding: 40px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
    header.article-header { padding-bottom: 20px; margin-bottom: 30px; border-bottom: 3px solid var(--pink-pastel); text-align: center; }
    .back-nav { font-family: 'Lora', serif; text-decoration: none; color: var(--brown-deep); font-weight: bold; font-size: 1rem; display: inline-block; margin-bottom: 20px; transition: all 0.2s; align-self: flex-start; }
    .back-nav:hover { color: #fff; text-decoration: underline; }
    h1 { font-family: 'Lora', serif; font-size: clamp(2rem, 5vw, 2.6rem); font-weight: 600; color: var(--brown-deep); line-height: 1.3; margin-bottom: 16px; letter-spacing: -0.5px; }
    .meta { color: #4a2e1c; font-size: 1.1rem; display: flex; justify-content: center; gap: 16px; font-style: italic; }
    article { padding: 12px 0; }
    article h2 { font-family: 'Lora', serif; font-size: 1.5rem; font-weight: 600; color: var(--brown-deep); margin-top: 40px; margin-bottom: 15px; }
    article p { margin-bottom: 20px; font-size: 1.1rem; line-height: 1.85; text-indent: 1.5em; }
    article p.no-indent { text-indent: 0; }
    article blockquote { font-style: normal; margin: 30px 40px; color: #4a2e1c; background: #e0f2fe; padding: 25px; border-left: 10px solid #4c2c17; border-radius: 5px; font-size: 1.1rem; text-indent: 0; }
    article blockquote cite { font-style: normal; font-weight: bold; display: block; margin-top: 10px; text-align: right; }
    .footnotes { margin-top: 40px; border-top: 1px solid var(--pink-pastel); padding-top: 20px; font-size: 0.95rem; }
    .footnotes p { text-indent: 0; margin-bottom: 10px; }
    figure { margin: 30px 0; text-align: center; }
    figcaption { font-size: 0.95rem; color: #4a2e1c; font-style: italic; margin-top: 10px; }
  </style>
</head>
<body>

<div class="wrap">
<a href="writing.html" class="back-nav">← Back to Writing</a>
  <header class="article-header">
    <h1>Built Worlds, Built Knowledge: Disability, Space, and Epistemic Exclusion</h1>
    <div class="meta"><span>By Roxy Alexander</span><span>|</span><span>March 2026</span></div>
  </header>
  <main>
    <article>
        ${htmlContent}
    </article>
  </main>
</div>

</body>
</html>
`;

fs.writeFileSync('built-world-built-knowledge.html', template);
console.log('Done rendering HTML');
