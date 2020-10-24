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
    """
    Creates a html-string for a file.
    If the file is markdown it will convert it.
    This functions ensures upscaling for future formats.

    Parameters:
    path_ex: path to a file.

    Returns:
    string: html-formatted string string equivalent to the file
    """
    filename = os.path.join(ENTRY_DIR, path_ex)
    result = ''
    if path.exists(filename):
        title = open(filename,encoding='utf-8').readline().rstrip('\n').lstrip('#').lstrip(' ')
        text = open(filename,encoding='utf-8').readlines()[1:]
        filename_no_end = filename.split('.', 1)[0]
        result += '<h1>' + title + '</h1>\n'
        if filename.endswith('.md'):
            result += gen_md_content(filename, 1)
    return result


def gen_md_content(path_ex, depth):
    """
    Convert a markdown file to a html string.

    Parameters:
    path_ex (string): path to the markdown file
    depth (int): starting depth for markdown headings

    Returns:
    string: html-formatted string string equivalent to the markdown file
    """
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


def gen_arch_string(path_ex):
    """
    Creates and returns an index string of every file in the path_ex.

    Parameter:
    path_ex: path to the dir to show

    Returns:
    string: html-formatted archive-string
    """
    full_path = os.path.join(ENTRY_DIR, path_ex)
    if path.exists(full_path):
        name_list = os.listdir(full_path)
        full_list = [os.path.join(full_path, i) for i in name_list]
        contents = sorted(full_list, key=os.path.getctime)
        content_string = ''
        last_month = ''
        for file in reversed(contents):
            filename = pathlib.PurePath(file)
            if os.path.isfile(filename):
                title = open(filename).readline().rstrip('\n').lstrip('#').lstrip(' ')
                entry_or_namespace = 'entry'
            elif os.path.isdir(filename):
                title = filename.name
                entry_or_namespace = 'namespace'
            else:
                continue
            filename = filename.name
            if filename[0] != '.' and filename.__contains__('.'):
                filename = filename.split('.', 1)[0]
            content_string += '<li>'
            content_string += title + ' ['
            content_string += '<a href="' + '/'+ entry_or_namespace +'/' + \
                path_ex.rstrip("/") + '/' +  pathlib.PurePath(file).name + '">' + 'standalone' + '</a>'
            content_string += '] <br>'
            content_string += '</li>\n'
        content_string += '</ul>\n'
        return content_string



def gen_query_res_string(query_str):
    """
    Return the results of a query.

    Parameters:
    query_str (string): term to search

    Returns:
    string: html-formated search result
    """
    src_results = search.search(query_str)
    res_string = ''
    res_string += '<ul>\n'
    for result in src_results:
        title = result['title']
        path = result['path']
        preview = create_preview(path)
        path = '/entry/' + path.split('/', 2)[2]
        res_string += '<li><a href="' + path + '">' + markdown.markdown(title) + '</a><br>'
        res_string += '<div class="description">' + preview + '</div>'
        res_string += '</li>'
    res_string += '</ul>\n'
    return res_string


def create_preview(path):
    """
    Create a preview of a given article and return it.

    Parameters:
    path (string): path to the article

    Returns:
    string: html-formated preview
    """
    file = open(path, 'r',encoding='utf-8')
    first_lines = file.readlines()
    preview = ''
    preview_length = 3
    for i, line in enumerate(first_lines):
        if i == 0:
            continue
        if i > preview_length:
            break
        if not line.isspace():
            preview += markdown.markdown(line) + '<br>'
        else:
            preview_length += 1
    preview += '...<br>'
    return preview

print(gen_arch_string('system-software'))
