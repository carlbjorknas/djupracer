def reward_function(params):  

    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']

    lane_width = track_width / 2

    pos_reward = 1.0
    if distance_from_center > lane_width:
        pos_reward = 0.0
    else:
        pos_reward = (lane_width - distance_from_center) / lane_width

    speed_reward = speed / 4

    return (pos_reward / 2) + (speed_reward / 2)