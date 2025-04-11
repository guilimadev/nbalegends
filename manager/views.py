import os
from django.conf import settings
from django.http import HttpResponseNotFound
from django.shortcuts import render
from urllib.parse import unquote, quote
from django.shortcuts import redirect
import re

def redirect_to_default_html(request):
    return redirect('/html-preview/Headlines.html/')

def show_html(request, filename):
    filename = unquote(filename)
    file_path = os.path.join(settings.MEDIA_ROOT, 'htmls', filename)

    if not os.path.exists(file_path):
        return HttpResponseNotFound("File not found")

    with open(file_path, encoding='utf-8', errors='replace') as f:
        content = f.read()

    def rewrite_href(match):
        href_value = match.group(2)
        print(href_value)
        if href_value.endswith('.html') and not href_value.startswith(('http', '/', '#')):
            encoded_href = quote(href_value)
            return f'{match.group(1)}/html-preview/{encoded_href}{match.group(3)}'
        return match.group(0)

    def rewrite_src(match):
        src_value = match.group(2)
        if not src_value.startswith(('http', '/', 'data:', '#')):
            return f'{match.group(1)}/static/{src_value}{match.group(3)}'
        return match.group(0)

    href_pattern = r'(href\s*=\s*[\'"])([^\'"]+)([\'"])'
    src_pattern = r'(src\s*=\s*[\'"]?)([^\'"\s>]+)([\'"]?)'

    content = re.sub(href_pattern, rewrite_href, content, flags=re.IGNORECASE)
    content = re.sub(src_pattern, rewrite_src, content, flags=re.IGNORECASE)

    return render(request, 'main.html', {'html_content': content})
