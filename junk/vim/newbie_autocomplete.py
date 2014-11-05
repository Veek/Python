import vim
import sys
import glob
import re
from newbie_lib import debug

min_token_size = 2
std_lib = '/usr/lib/python2.6/'
snippet_file = '/root/snippets.vim'

language_keywords = ('and elif if print as else import raise assert ' +
'except in return break exec is try class finally lambda while ' +
'continue for not with def from or yield del global pass')

# global log file handle
f = open('/tmp/foo', 'a')
# global start and base values passed by vim. Initialized in __main__
start = ''
base = ''

def p(txt):
    txt = str(txt) + '\n' + '\n'
    f.write(txt)
    f.flush()

def slurp_file(file_name):
    contents = open(file_name, 'r')
    return contents

def set_line_empty():
    import string
    line = vim.current.line
    row, col = vim.current.window.cursor

    line = str(line[0:col])
    line = line.strip()

    if not len(line):
        vim.command('let l:start = -1')

def tokenize_buffer(contents):
    re_strip = re.compile('[^a-zA-Z0-9_]+')
    contents = re.sub(re_strip, ' ', contents)

    tokens = [token for token in contents.split()]
    return tokens

def filter_tokens(token_list):
    global min_token_size
    tokens = []
    for token in token_list:
        if ((len(token) > min_token_size) & (token not in tokens)):
            tokens.append(token)
    return tokens

def build_keyword_list():
    # parse Python keywords
    keyword_tokens = [
      dict(word=token, menu='keyword')
          for token in language_keywords.split()
    ]

    # parse current buffer
    cur_line_no = int(vim.eval('line(".")'))
    buf_contents = vim.current.buffer[:]

    top_half = buf_contents[0:cur_line_no]
    top_half.reverse()

    bot_half = buf_contents[cur_line_no:]

    top_half.extend(bot_half)
    cur_buf_tokens = tokenize_buffer( str(top_half))

    cur_buf_tokens = [
      dict(word=token, abbr=token, menu='current_buffer', info=token)
          for token in cur_buf_tokens if len(token) > 1
     ]

    # parse snippet file
    contents = slurp_file(snippet_file)


    token_list = []
    token_list = keyword_tokens + cur_buf_tokens
    return token_list

def build_module_list(user_txt):
    import inspect
    tokens = user_txt.split('.')
    imp_obj = __import__(tokens[0])
    eval_list = dir(imp_obj)
    eval_list = [item for item in eval_list
                        if ('_' not in item) & (len(item) > 2)]
    for token in eval_list:
        print(token)
        name_txt = str(getattr(token, __name__, ''))
        info_txt = str(getattr(token, __name__, ''))
        type_txt = str(type(token))
        if 'class' in type_txt:
            menu_txt = type_txt
        elif 'function' in type_txt:
            menu_txt = str(inspect.formatargspec(*inspect.getargspec(token)))
        else:
            menu_txt = ''
        cur_buf_tokens = []
        cur_buf_tokens.extend(
            dict(word=name_txt, abbr='', menu=menu_txt, info='')
        )
    return cur_buf_tokens

def set_start():
    line = vim.current.line
    (row, col) = vim.current.window.cursor

    line = line[0:col]
    words = line.split()

    if len(words):
        offset = len(line.rstrip()) - len(words[-1])
        vim.command('let l:start = ' + str(offset))
    else:
        vim.command('let l:start = -1')

def set_base():
    global base

    if '.' in base:
        key_words = build_module_list(base)
        for word_dict in key_words:
            vim.command('call complete_add(' + str(word_dict) + ')')
        return

    key_words = build_keyword_list()

    result_str=[]
    for word_dict in key_words:
        if re.match(base, word_dict['word']):
            vim.command('call complete_add(' + str(word_dict) + ')')

    # parse modules
    for path in glob.glob('/usr/lib/python2.6/[a-zA-Z0-9]*.py'):
        parent_dir, file_name = path.split('/')[-2:]
        token = file_name.split('.')[0]
        if re.match(base, token):
            module_name = dict(word=token, abbr=token, menu=parent_dir,
                                info=token)
            vim.command('call complete_add(' + str(module_name) + ')')

    if vim.command('call complete_check()'):
        return

def __main__():
    import imp

    global f, start, base

    start = str(vim.eval('a:start'))
    base = str(vim.eval('a:base'))

    f = open('/tmp/foo', 'a')

    if start == '1':
        set_start()
    elif base:
       set_base()
