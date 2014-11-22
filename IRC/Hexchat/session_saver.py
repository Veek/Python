import hexchat
import time

__module_name__ = "Session Saver"
__module_version__ = "0.1"
__module_description__ = "Periodically saves current session for next start"


def debug(msg):
    hexchat.prnt('DEBUG: {}'.format(msg))

#-----------------------------------------------------------------------
def get_tab_data():
    # Returns a dict of network=[channels]. Uses addon_python.conf:
    # session_freenode = #test,#foo
    # list_pluginpref() returns the key 'session_freenode'
    # get_pluginpref('session_freenode') returns the comma delimited channel list
    tab_data = {}
    for pref in hexchat.list_pluginpref():
        if len(pref) > 8 and pref[:8] == 'session_':
            network = pref[8:]
            channels = hexchat.get_pluginpref('session_' + network).split(',')
            if len(channels):
                tab_data[network] = channels
            else:
                tab_data[network] = None
    return tab_data


def connect_server(network):
    hexchat.command('server irc://"{}"/'.format(network))


#def join_channels(channels):
#    # /join the list of channels, for a server that's been logged
#    # into
#    delay = hexchat.get_prefs('irc_join_delay')
#    for chan in channels:
#        if len(chan) and chan[0] != '#':
#            hexchat.command('timer {} join {}'.format(delay, chan))
#
#
#def process_channels(tab_data):
#    # Get the Tab data, iterate the channel list for
#    network = hexchat.get_info('network')


def setup_channels(word, word_eol, user_data):
    # Callback for: server motd-received event
    # Unhook and /join channels
    hexchat.unhook(setup_channels)
    hexchat.prnt('FOOOOOOOOOOOOOOOOOO')
    x = hexchat.list_pluginpref()
    hexchat.prnt(x)


#-----------------------------------------------------------------------
def save_session(userdata):
    # Saves the network|channels dictionary in pluginpref
    networks = {}
    channels = hexchat.get_list('channels')

    if not hexchat.get_context():
        return

    # Build dictionary 'networks'
    #  Iterate 'channels' and add all the servers
    for chan in channels:
        if chan.type == 1:
            networks[chan.network] = []

    # Iterate 'channels' and add channels.
    # networks={'freenode':[chan1, chan2, chan3], 'dalnet':[]}
    for chan in channels:
        if chan.type == 2 or chan.type == 3: # Ignore notices and server tabs
            networks[chan.network].append(chan.channel)

    # Iterate 'networks' and store in hexchat.pluginpref as
    # session_freenode = chan1,chan2. This is written to
    # 'addon_python.conf' eventually.
    for network, channels in networks.items():
        if len(network):
            hexchat.set_pluginpref('session_' + network, ','.join(channels))
    return hexchat.EAT_ALL


#-----------------------------------------------------------------------
# Load the previous session:
# 1. Setup a hook for '376' RPL_ENDOFMOTD (RFC-1459). When we receive
# this we know we are connected to the server and can connect to its
# channels.
# 2. Load the servers, every time you receive their 'motd' the
# corresponding channels are loaded
hexchat.hook_server('376', setup_channels)

tab_data = get_tab_data()
for network in tab_data.keys():
    connect_server(network)


hexchat.hook_timer(10000, save_session) # Save every x minutes
# hexchat.hook_unload(save_session) # Doesn't work with X11 Quit
