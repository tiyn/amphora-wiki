import config
import search

import datetime
from datetime import datetime
import os
from os import path
import pathlib

import markdown

ENTRY_DIR = config.ENTRY_DIR
WEBSITE = config.WEBSITE


def gen_stand_string(path_ex):
    filename = os.path.join(ENTRY_DIR, path_ex)
    result = ''
    if path.exists(filename):
        title = open(filename,encoding='utf-8').readline().rstrip('\n')
        text = open(filename,encoding='utf-8').readlines()[1:]
        filename_no_end = filename.split('.', 1)[0]
        result += '<h1>' + title + '</h1>\n'
        if filename.endswith('.md'):
            result += gen_md_content(filename, 1)
    return result


def gen_md_content(path_ex, depth):
    result = ''
    if path.exists(path_ex):
        filename = path_ex.split('.', 1)
        fileend = filename[len(filename) - 1]
        header = '#'
        for i in range(depth):
            header += '#'
        header += ' '
        markdown_lines = open(path_ex, 'r',encoding='utf-8').readlines()[1:]
        markdown_text = ''
        for line in markdown_lines:
            markdown_text += line.replace('# ', header)
        result = markdown.markdown(
            markdown_text, extensions=["fenced_code", "tables", "nl2br"])
    return result


def gen_query_res_string(query_str):
    src_results = search.search(query_str)
    res_string = ''
    res_string += '<ul>\n'
    for result in src_results:
        title = result['title']
        path = result['path']
        preview = create_preview(path)
        path = '/entry/' + path.split('/', 2)[2]
        res_string += '<li><a href="' + path + '">' + title + '</a><br>'
        res_string += '<div class="description">' + preview + '</div>'
        res_string += '</li>'
    res_string += '</ul>\n'
    return res_string


def create_preview(path):
    file = open(path, 'r',encoding='utf-8')
    first_lines = file.readlines()
    preview = ''
    preview_length = 3
    for i, line in enumerate(first_lines):
        if i > preview_length:
            break
        if not line.isspace():
            preview += line + '<br>'
        else:
            preview_length += 1
    return preview
