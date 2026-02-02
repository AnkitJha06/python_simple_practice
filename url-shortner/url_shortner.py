import string
import random
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# Mock Database
url_db = {}

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Super Black Theme Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shorty | URL Shortener</title>
    <style>
        :root {
            --bg-color: #000000;
            --card-bg: #0a0a0a;
            --accent: #00d4ff;
            --text: #ffffff;
            --input-bg: #111111;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text);
            font-family: 'Inter', -apple-system, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            background-color: var(--card-bg);
            padding: 2.5rem;
            border-radius: 16px;
            box-shadow: 0 0 20px rgba(0, 212, 255, 0.1);
            border: 1px solid #1a1a1a;
            width: 100%;
            max-width: 400px;
            text-align: center;
        }

        h1 { margin-bottom: 1.5rem; font-weight: 800; letter-spacing: -1px; }
        h1 span { color: var(--accent); }

        input[type="text"] {
            width: 100%;
            padding: 12px;
            margin-bottom: 1rem;
            background: var(--input-bg);
            border: 1px solid #222;
            border-radius: 8px;
            color: white;
            box-sizing: border-box;
            outline: none;
            transition: border 0.3s;
        }

        input[type="text"]:focus { border-color: var(--accent); }

        button {
            width: 100%;
            padding: 12px;
            background-color: var(--accent);
            border: none;
            border-radius: 8px;
            color: #000;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.2s, opacity 0.2s;
        }

        button:hover { opacity: 0.9; transform: translateY(-1px); }

        .result {
            margin-top: 2rem;
            padding: 1rem;
            background: #111;
            border-radius: 8px;
            border-left: 4px solid var(--accent);
        }

        a { color: var(--accent); text-decoration: none; word-break: break-all; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Shorty<span>.</span></h1>
        <form method="POST" action="/shorten">
            <input type="text" name="long_url" placeholder="Paste your long link here..." required>
            <button type="submit">Shorten Link</button>
        </form>
        
        {% if short_url %}
        <div class="result">
            <p style="font-size: 0.8rem; color: #666; margin: 0;">Your short link:</p>
            <a href="{{ short_url }}" target="_blank">{{ short_url }}</a>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form.get('long_url')
    if not long_url.startswith(('http://', 'https://')):
        long_url = 'http://' + long_url
        
    short_code = generate_short_code()
    url_db[short_code] = long_url
    
    # Use request.host_url to get the actual domain automatically
    short_url = f"{request.host_url}{short_code}"
    return render_template_string(HTML_TEMPLATE, short_url=short_url)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    long_url = url_db.get(short_code)
    if long_url:
        return redirect(long_url)
    return "Link expired or not found", 404

if __name__ == '__main__':
    app.run(debug=True)