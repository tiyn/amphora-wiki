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
    content_string = ''
    if path.exists(filename):
        title = open(filename).readline().rstrip('\n')
        text = open(filename).readlines()[1:]
        filename_no_end = filename.split('.', 1)[0]
        content_string += '<h1>' + title + '</h1>\n'
        if filename.endswith('.md'):
            content_string += gen_md_content(filename, 1)
    return content_string


def gen_md_content(path_ex, depth):
    content_string = ''
    if path.exists(path_ex):
        filename = path_ex.split('.', 1)
        fileend = filename[len(filename) - 1]
        header = '#'
        for i in range(depth):
            header += '#'
        header += ' '
        markdown_lines = open(path_ex, "r").readlines()[1:]
        markdown_text = ''
        for line in markdown_lines:
            markdown_text += line.replace('# ', header)
        content_string = markdown.markdown(
            markdown_text, extensions=["fenced_code", "tables"]
        )
    return content_string


def gen_query_res_string(query_str):
    src_results = search.search(query_str)
    res_string = ''
    res_string += '<ul>\n'
    for result in src_results:
        title = result['title']
        path = result['path']
        path = '/entry/' + path.split('/', 2)[2]
        res_string += '<li><a href="' + path + '">' + title + '</a></li>'
    res_string += '</ul>\n'
    return res_string
