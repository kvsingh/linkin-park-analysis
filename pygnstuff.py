import pygn

# NOTE: Gracenote API has built-in fuzzy matching to artist and track.
from collections import defaultdict

def get_gn_multiple(search, dictionary, item):
    '''
    Helper function to get multiple items within Gracenote record
    '''
    for i in search[item].iteritems():
        dictionary[item + '_' + i[0]] = i[1]['TEXT']

def get_mood(artist, track):
    '''
    Gets artist and track information from Gracenote
    '''
    #print artist, track
    clientid = 'your-gracenote-client-id'
    userid = pygn.register(clientid)

    gn_dict = defaultdict(list)
    gn_info = pygn.search(clientid, userid, artist=artist, track=track)

    try:
        gn_dict['gnid'] = gn_info['track_gnid']
    except:
        return None

    # artist specific info
    for a in ['artist_origin', 'artist_type', 'artist_era']:
        get_gn_multiple(gn_info, gn_dict, a)
    # track specific info
    for s in ['genre', 'mood', 'tempo']: # can potentially drop 'tempo' since Spotify has already captured this
        get_gn_multiple(gn_info, gn_dict, s)

    #return dict(gn_dict)
    return gn_dict['mood_1']

