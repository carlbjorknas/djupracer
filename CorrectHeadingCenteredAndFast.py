import math

def reward_function(params):  

    track_width = params['track_width']
    lane_width = track_width / 2

    distance_from_center = params['distance_from_center']
    speed = params['speed']    
    heading = params['heading']      
    
    waypoints = params['waypoints']   
    closest_waypoints = params['closest_waypoints']   
    #prev_waypoint = waypoints[closest_waypoints[0]]
    next_waypoint = waypoints[closest_waypoints[1]]  

    car_x = params['x']
    car_y = params['y']

    ## reward for position
    pos_reward = 1.0
    if distance_from_center > lane_width:
        pos_reward = 0.0
    else:
        pos_reward = (lane_width - distance_from_center) / lane_width

    ## reward for speed
    speed_reward = speed / 4

    ## reward for heading
    # Calculate the direction to next waypoint in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    next_waypoint_direction_from_car = math.degrees(math.atan2(next_waypoint[1] - car_y, next_waypoint[0] - car_x))

    # Calculate the difference between the direction to the next waypoint and the heading direction of the car
    direction_reward = 0.0
    direction_diff = abs(next_waypoint_direction_from_car - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    if direction_diff < 45:
        direction_reward = (45 - direction_diff) / 45

    return 0.5 * direction_reward + 0.3 * pos_reward + 0.2 * speed_reward