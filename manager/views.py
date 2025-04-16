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
        if len(match.groups()) == 3:
            prefix, href_value, suffix = match.group(1), match.group(2), match.group(3)
        else:
            prefix, href_value, suffix = match.group(1), match.group(2), ''

        if href_value.endswith('.html') and not href_value.startswith(('http', '/', '#')):
            return f'{prefix}/html-preview/{href_value}/{suffix}'
        return match.group(0)

    def rewrite_src(match):
        src_value = match.group(2)
        if not src_value.startswith(('http', '/', 'data:', '#')):
            return f'{match.group(1)}/static/{src_value}{match.group(3)}'
        return match.group(0)
    
    quoted_href_pattern = r'(href\s*=\s*["\'])([^"\']+)(["\'])'

    # Pattern for unquoted hrefs
    unquoted_href_pattern = r'(href\s*=\s*)([^\s>]+)'
    
    src_pattern = r'(src\s*=\s*[\'"]?)([^\'"\s>]+)([\'"]?)'

    content = re.sub(quoted_href_pattern, rewrite_href, content, flags=re.IGNORECASE)
    content = re.sub(unquoted_href_pattern, rewrite_href, content, flags=re.IGNORECASE)
    content = re.sub(src_pattern, rewrite_src, content, flags=re.IGNORECASE)

    return render(request, 'main.html', {'html_content': content})


def show_pre(request, filename):
    filename = unquote(filename)
    file_path = os.path.join(settings.MEDIA_ROOT, 'pre', filename)

    if not os.path.exists(file_path):
        return HttpResponseNotFound("File not found")

    with open(file_path, encoding='utf-8', errors='replace') as f:
        content = f.read()

    def rewrite_href(match):
        if len(match.groups()) == 3:
            prefix, href_value, suffix = match.group(1), match.group(2), match.group(3)
        else:
            prefix, href_value, suffix = match.group(1), match.group(2), ''

        if href_value.endswith('.html') and not href_value.startswith(('http', '/', '#')):
            return f'{prefix}/pre-preview/{href_value}/{suffix}'
        return match.group(0)

    def rewrite_src(match):
        src_value = match.group(2)
        if not src_value.startswith(('http', '/', 'data:', '#')):
            return f'{match.group(1)}/static/{src_value}{match.group(3)}'
        return match.group(0)
    
    quoted_href_pattern = r'(href\s*=\s*["\'])([^"\']+)(["\'])'

    # Pattern for unquoted hrefs
    unquoted_href_pattern = r'(href\s*=\s*)([^\s>]+)'
    
    src_pattern = r'(src\s*=\s*[\'"]?)([^\'"\s>]+)([\'"]?)'

    content = re.sub(quoted_href_pattern, rewrite_href, content, flags=re.IGNORECASE)
    content = re.sub(unquoted_href_pattern, rewrite_href, content, flags=re.IGNORECASE)
    content = re.sub(src_pattern, rewrite_src, content, flags=re.IGNORECASE)

    return render(request, 'main.html', {'html_content': content})

def show_pre2(request, filename):
    filename = unquote(filename)
    file_path = os.path.join(settings.MEDIA_ROOT, 'pre2', filename)

    if not os.path.exists(file_path):
        return HttpResponseNotFound("File not found")

    with open(file_path, encoding='utf-8', errors='replace') as f:
        content = f.read()

    def rewrite_href(match):
        if len(match.groups()) == 3:
            prefix, href_value, suffix = match.group(1), match.group(2), match.group(3)
        else:
            prefix, href_value, suffix = match.group(1), match.group(2), ''

        if href_value.endswith('.html') and not href_value.startswith(('http', '/', '#')):
            return f'{prefix}/pre2-preview/{href_value}/{suffix}'
        return match.group(0)

    def rewrite_src(match):
        src_value = match.group(2)
        print(src_value)
        if not src_value.startswith(('http', '/', 'data:', '#')):
            return f'{match.group(1)}/static/{src_value}{match.group(3)}'
        return match.group(0)
    
    quoted_href_pattern = r'(href\s*=\s*["\'])([^"\']+)(["\'])'

    # Pattern for unquoted hrefs
    unquoted_href_pattern = r'(href\s*=\s*)([^\s>]+)'
    
    src_pattern = r'(src\s*=\s*[\'"]?)([^\'"\s>]+)([\'"]?)'

    content = re.sub(quoted_href_pattern, rewrite_href, content, flags=re.IGNORECASE)
    content = re.sub(unquoted_href_pattern, rewrite_href, content, flags=re.IGNORECASE)
    content = re.sub(src_pattern, rewrite_src, content, flags=re.IGNORECASE)

    return render(request, 'main.html', {'html_content': content})




def capivara_view(request):
    return render(request, 'capiporter.html', {'message': 'Welcome to my site!'})