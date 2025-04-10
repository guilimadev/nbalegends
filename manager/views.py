import os
from django.conf import settings
from django.http import HttpResponseNotFound
from django.shortcuts import render
from urllib.parse import unquote
import re



def show_html(request, filename):
    filename = unquote(filename)
    file_path = os.path.join(settings.MEDIA_ROOT, 'htmls', filename)
    
    if not os.path.exists(file_path):
        return HttpResponseNotFound("File not found")

    with open(file_path, encoding='utf-8') as f:
        content = f.read()

    # Rewrite relative links to point to the /html-preview/ route
    def rewrite_link(match):
        href_value = match.group(2)
        if href_value.endswith('.html') and not href_value.startswith(('http', '/', '#')):
            return f'{match.group(1)}/html-preview/{href_value}{match.group(3)}'
        return match.group(0)

    # Regex breakdown:
    # 1. Group 1: href= (with optional spacing and opening quote)
    # 2. Group 2: actual filename
    # 3. Group 3: closing quote (optional)
    pattern = r'(href\s*=\s*[\'"]?)([^\'"\s>]+)([\'"]?)'
    content = re.sub(pattern, rewrite_link, content, flags=re.IGNORECASE)

    return render(request, 'main.html', {'html_content': content})
