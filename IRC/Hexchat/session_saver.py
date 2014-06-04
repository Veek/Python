import hexchat

__module_name__ = "Session Saver"
__module_version__ = "0.1"
__module_description__ = "Periodically saves current session for next start"


def debug(msg):
    msg = str(msg)
    hexchat.prnt('{}'.format(msg))

#-----------------------------------------------------------------------
def get_tab_data():
    tab_data = {}
    for pref in hexchat.list_pluginpref():
        if len(pref) > 8 and pref[:8] == 'session_':
            network = pref[8:]
            channels = hexchat.get_pluginpref('session_' + network).split(',')
            tab_data[network] = channels

    return tab_data


def join_channels(channels):
    delay = hexchat.get_prefs('irc_join_delay') + 10
    for chan in channels:
        if len(chan) and chan[0] != '#':
            hexchat.command('timer {} query -nofocus {}'.format(delay, chan))
        else:
            hexchat.command('timer {} join {}'.format(delay, chan))


def load_session():
    tab_data = get_tab_data()
    for network in tab_data.keys():
        hexchat.del_pluginpref('session_' + network)
        if not hexchat.get_context():
            hexchat.command('server irc://"{}"/'.format(network))
            join_channels(tab_data[network])
        else:
            hexchat.command('server irc://"{}"/'.format(network))
            hexchat.find_context(server=network).set()
            join_channels(tab_data[network])

#-----------------------------------------------------------------------
def save_session(userdata):
    networks = {}

    for chan in hexchat.get_list('channels'):
        if chan.type == 2 or chan.type == 3: # Ignore notices and server tabs
            if not chan.network in networks:
                networks[chan.network] = []  # Append a new empty entry
            if (chan.channelkey):
                networks[chan.network].append(chan.channel + ' ' + chan.channelkey)
            else:
                networks[chan.network].append(chan.channel)

    for network, channels in networks.items():
        hexchat.set_pluginpref('session_' + network, ','.join(channels))

    return hexchat.EAT_ALL


#-----------------------------------------------------------------------
load_session()
hexchat.hook_timer(10000, save_session) # Save every 1 minute
