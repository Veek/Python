import vim
import subprocess as sp

def debug(*args, **kwargs):
    f = open('/tmp/vim.xxx', 'a')
    txt = str(args) + str(**kwargs) + '\n\n'
    f.write(txt)
    f.flush(); f.close()


def locate_a_binary(file_name):
    try:
        file_location = sp.check_output(['whereis', file_name])
    except sp.CalledProcessError as err:
        debug(err)

def locate_a_file(file_name):
    file_location = sp.check_output(['locate', file_name])


def vim_cmd(cmd):
    vim.command(':!tput clear;' + str(cmd))

def save_file():
    buffer = vim.current.buffer
    file_name = buffer.name
    if file_name:
        vim.command(':w!')
    else:
        vim.command(':w! ./xxx')

def build_program():
    pass
#locate_a_binary_file('ls')
