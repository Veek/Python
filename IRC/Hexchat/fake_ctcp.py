import re, random, hexchat
from subprocess import Popen, PIPE

__module_name__ = 'Fake CTCP'
__module_version__ = '0.1'
__module_description__ = 'Fakes unessential CTCP requests: VERSION PING TIME'

FAKE_VERSION = 'pinoyChat v1.3.3.4 -  Windows XP SP2,'\
               ' @400MHz Celeron Mendocino, Administrator:password'


def debug(msg):
    hexchat.prnt('{}'.format(msg))


def get_mangled_date():
    date_s = Popen(['date', '+"%a %b %d"'], stdout=PIPE).communicate()[0].rstrip()
    date_s=date_s[1:-1]

    hour = random.randint(00, 24)
    min = random.randint(00, 60)
    sec = random.randint(00, 60)

    date = str(date_s) + ' ' + str(hour) + ':' + str(min) + ':' + str(sec)

    return date


def extract_sender(word):
    pat = '^:(.+?)!'
    m = re.search(pat, word[0])
    if m:
        name = m.groups(1)[0]

    return name


def ctcp_reply(nick, cmd, msg):
    hexchat.command('nctcp {} {} {}'.format(nick, cmd, msg))


def ctcp_callback(word, word_eol, userdata):
    sending_nick = extract_sender(word)
    recv_cmd = word_eol[0]

    if 'VERSION' in recv_cmd:
       ctcp_reply(sending_nick, 'VERSION', FAKE_VERSION)
       debug(recv_cmd)
       return hexchat.EAT_ALL
    elif 'TIME' in recv_cmd:
       ctcp_reply(sending_nick, 'TIME', get_mangled_date())
       debug(recv_cmd)
       return hexchat.EAT_ALL
    elif 'PING' in recv_cmd:
       ctcp_reply(sending_nick, 'PING', 10)
       debug(recv_cmd)
       return hexchat.EAT_ALL

    return hexchat.EAT_NONE


#-------------------------------------------------------------
hexchat.prnt('CTCP script loaded')
hexchat.hook_server('PRIVMSG', ctcp_callback)
