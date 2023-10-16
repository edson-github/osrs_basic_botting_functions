import json


def get_live_info():
    '''Returns specific live information from the game client via the Status Socket plugin.'''
    try:
        with open('live_data.json', "r+") as f:
            data = json.load(f)
        return data
    except:
        pass

def update_inventory():
    """Updates the current inventory."""
    data = get_live_info()
    return data['inventory'] if data != None else None

def update_positon():
    """Updates the current position of the player."""
    data = get_live_info()
    return (
        [data['worldPoint']['x'], data['worldPoint']['y']]
        if data != None
        else None
    )
def update_run_energy():
    """Updates the current run energy."""
    run_energy = None
    data = get_live_info()
    while data is None:
         data = get_live_info()
    return data['run energy']

def update_camera_angle():
    """Updates current camera angle."""
    data = get_live_info()
    return data['camera']['yaw'] if data != None else None

get_live_info()
t = update_run_energy()
print(t)
