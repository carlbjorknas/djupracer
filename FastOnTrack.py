def reward_function(params):

    # input variables
    off_track = params['is_offtrack']
    speed = params['speed']

    if off_track:
        return 0
    
    return speed