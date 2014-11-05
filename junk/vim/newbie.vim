
function! Cut() range
python3 << EOF
import vim
from newbie_lib import debug

stop  = int(vim.eval('a:lastline'))
start = int(vim.eval('a:firstline'))

x = stop - start + 1

vim.command('y')
vim.command(':normal! gv')

if x == 1:
    vim.command('let @".="%s"'.format(vim.current.buffer[start - 1]))
    del vim.current.buffer[start - 1]
else:
    while x > 0:
        vim.command('let @"="%s"'.format(vim.current.buffer[start - 1]))
        del vim.current.buffer[start - 1]
        x -= 1

vim.command(':call feedkeys("\<Esc>")')
vim.command(':normal! ^')
EOF
endfunction


function! Paste()
python3 << EOF
import vim
from newbie_lib import debug

quote_register = vim.eval('@"')
length = len(quote_register.split('\n'))

cw = vim.current.window
(row, col) = cw.cursor

vim.command(':normal! ' + str(length) + 'O')
cw.cursor = (row, col)

vim.command(':normal! p')
vim.command(':normal! i')
EOF
endfunction

function! Comment() range
python3 << EOF
import vim
from newbie_lib import debug
cb = vim.current.buffer
stop  = int(vim.eval('a:lastline')) - 1
start = int(vim.eval('a:firstline')) - 1

lines=[]
while start <= stop:
    cb[start] = '#' + cb[start]
    start += 1
EOF
endfunction


function! Sort()
python3 << EOF
import vim
cr = vim.current.range
line = cr[0]
line = line.split()
fmt_str = ['%8s' for word in line]
fmt_str = ' '.join(fmt_str)

line = tuple([word for word in line])
print(fmt_str)
cr[0]= fmt_str % line
EOF
endfunction

function! My_dir(fname)
python3 << EOF
import vim
blah = vim.eval('a:fname')
if str(blah) == 'None':
    cb = vim.current.buffer
    cb[0] = ' .vimrc'
    cb.append(' .vim/plugins/')
    cb.append('              newbie.vim')
EOF
endfunction


function! Save_file()
python3 << EOF
import newbie_lib as nl
nl.save_file()
EOF
endfunction

function! Snippets()
python3 << EOF

EOF
endfunction

function! Build_program()
python3 << EOF
import os, re, vim
from subprocess import Popen, PIPE
from newbie_lib import vim_cmd

file_handlers = {
    'python' : 'python3.2',
    'shell'  : 'bash',
}

buffer = vim.current.buffer
path_name = buffer.name

file_name = os.path.basename(path_name)
root, ext = os.path.splitext(file_name)

cr = vim.current.range
line = cr[0]

cmd_s = Popen(['file', '-i', file_name], stdout=PIPE).communicate()[0].rstrip()

pat = 'python'
if re.match(pat, str(cmd_s)):
    vim_cmd('python3.2 ' + str(file_name))

def python():
    cmd = 'python3.2 ' + str(file_name)
    vim_cmd(cmd)

def shell():
    cmd = 'bash ' + str(file_name)
    vim_cmd(cmd)

def c_plus_plus():
    cmd = 'g++ ' + str(file_name)
    vim_cmd(cmd)

def c99():
    cmd = 'gcc ' + str(file_name) + "; a.out"
    vim_cmd(cmd)

ext_handlers = {
    '.py'  : python,
    '.sh'  : shell,
    '.cpp' : c_plus_plus,
    '.c'   : c99,
}

if 'xxx' in file_name:
    default_handler()

if ext:
    try:
            handler = ext_handlers[ext]
            handler()
    except KeyError:
        pass
EOF
endfunction


function! Align(start, end)
python3 << EOF
buffer = vim.current.buffer
start = int(vim.eval('a:start'))
end = int(vim.eval('a:end'))
tokens=[]
for n in range(start, end+1):
    line = buffer[n-1].split()
    tokens.append(line)

count = len(tokens)
EOF
endfunction


function! OpenFile()
python3 << EOF
import vim
import re
buffer = vim.current.buffer
name = str(buffer.name)
if re.match('None', name):
    vim.command(':e ')
else:
    vim.command(':tabnew')
    vim.command(':e ')
EOF
endfunction

"-----------------------------------------------------------------------
function! MyBalloonExpr()
let cursor_text = v:beval_text

python3 << EOF
import vim
b = vim.current.buffer
r = vim.current.range
cursor_text = vim.eval('l:cursor_text')
#f.write(str(cursor_text))
EOF
endfunction

"-----------------------------------------------------------------------
function! Tab_line()
let l:fmt_str = ''
"'%#TabLineSel#%1T %{MyTabLabel(1)} %#TabLineFill#%T'

python3 << EOF
import vim
no_of_tabs = int(vim.eval('tabpagenr("$")'))
cur_tab_no = int(vim.eval('tabpagenr()'))
last_tab_no = int(vim.eval("tabpagenr('$')"))

fmt_str = ''
for i in range(no_of_tabs):
    if i + 1  == cur_tab_no:
        fmt_str += '%#TabLineSel#'
    else:
        fmt_str += '%#TabLine#'

    fmt_str += '%' + str(i + 1) + 'T '

    fmt_str += '%{My_tab_label(' + str(i + 1) + ')}'


fmt_str +=  ' %#TabLineFill#%T'

if last_tab_no > 1:
    fmt_str += '%=%#TabLine#%999Xclose'

fmt_str = '"' + fmt_str + '"'
vim.command('let l:fmt_str = ' + str(fmt_str))
EOF

return fmt_str
endfunction

function! My_tab_label(n)
    let buflist = tabpagebuflist(a:n)
    let winnr = tabpagewinnr(a:n)
    let bname = bufname(buflist[winnr - 1])

python3 << EOF
import vim
cur_tab_no = int(vim.eval('tabpagenr()'))
bname = str(vim.eval('l:bname'))
#f.write(str(bname))
n = int(vim.eval('a:n'))
if cur_tab_no != n:
    bname = bname.split('/')
    bname = bname[-1]

#f.write(str(bname) + str(n)+ str(cur_tab_no) +'\n')
vim.command('let l:bname = "' + str(bname) + '"')
EOF

    return a:n . ':' . bname
endfunction


"-----------------------------------------------------------------------
func! Tab_wrapper()
    let l:start = 0
python3 << EOF
import  newbie_autocomplete as ml
import imp
imp.reload(ml)
ml.set_line_empty()
EOF
    if l:start == -1
       return "\<Tab>"
    else
       return "\<C-X>\<C-O>"
    endif
endfunction


func! Auto_complete(start, base)
    let l:start = a:start
    let l:base  = a:base
    let l:res   = []
python3 << EOF
import newbie_autocomplete as ml
import imp
imp.reload(ml)
ml.__main__()
EOF
    if a:start
        return l:start
endfunction
