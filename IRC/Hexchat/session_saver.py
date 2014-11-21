import hexchat
import time

__module_name__ = "Session Saver"
__module_version__ = "0.1"
__module_description__ = "Periodically saves current session for next start"


def debug(msg):
    hexchat.prnt('DEBUG: {}'.format(msg))

#-----------------------------------------------------------------------
def get_tab_data():
    '''Returns a list of network= channels'''
    tab_data = {}
    for pref in hexchat.list_pluginpref():
        if len(pref) > 8 and pref[:8] == 'session_':
            network = pref[8:]
            channels = hexchat.get_pluginpref('session_' + network).split(',')
            tab_data[network] = channels
    return tab_data


def join_channels(channels):
    '''Joins the list of channels for a server that's been logged
    into'''
    delay = hexchat.get_prefs('irc_join_delay')
    for chan in channels:
        if len(chan) and chan[0] != '#':
            hexchat.command('timer {} query -nofocus {}'.format(delay, chan))
        else:
            hexchat.command('timer {} join {}'.format(delay, chan))


def load_session():
    '''Loads a saved session'''
    tab_data = get_tab_data()
#    debug(tab_data)
    for network in tab_data.keys():
        if not hexchat.get_context():
            hexchat.command('server irc://"{}"/'.format(network))
            join_channels(tab_data[network])
        else:
            hexchat.command('server irc://"{}"/'.format(network))
            hexchat.find_context(server=network).set()
            join_channels(tab_data[network])
        hexchat.del_pluginpref('session_' + network)

#-----------------------------------------------------------------------
def save_session(userdata):
    '''Saves the network|channels dictionary in pluginpref'''
    networks = {}
    channels = hexchat.get_list('channels')

    # Add all the servers
    for chan in channels:
        if chan.type == 1:
            networks[chan.network] = []

    # Add selected channels. networks={'freenode':[chan1, chan2 key, chan3], 'dalnet':[]}
    for chan in channels:
        if chan.type == 2 or chan.type == 3: # Ignore notices and server tabs
            if (chan.channelkey):
                networks[chan.network].append(chan.channel + ' ' + chan.channelkey)
            else:
                networks[chan.network].append(chan.channel)

    # session_freenode, chan1,cha2 key,chan3
    for network, channels in networks.items():
        if len(network):
            hexchat.set_pluginpref('session_' + network, ','.join(channels))
#    debug(networks)
    return hexchat.EAT_ALL

def connected():
    time.sleep(1)
#-----------------------------------------------------------------------
load_session()
hexchat.hook_timer(500000, save_session) # Save every x minutes
# hexchat.hook_unload(save_session) # Doesn't work with X11 Quit
