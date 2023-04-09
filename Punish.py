import math

def reward_function(params):  

    track_width = params['track_width']
    lane_width = track_width / 2

    distance_from_center = params['distance_from_center']
    speed = params['speed']    
    heading = params['heading']  
    steering_angle = params['steering_angle']
    
    waypoints = params['waypoints']   
    closest_waypoints = params['closest_waypoints']   
    #prev_waypoint = waypoints[closest_waypoints[0]]
    next_waypoint = waypoints[closest_waypoints[1]]  

    car_x = params['x']
    car_y = params['y']

    off_track = params['is_offtrack']

    if off_track:
        return -50.0

    ## reward for position
    pos_reward = 1.0
    if distance_from_center > lane_width:
        pos_reward = 0.0
    else:
        pos_reward = (lane_width - distance_from_center) / lane_width

    ## reward for speed
    speed_reward = speed / 4

    ## reward for direction
    direction_reward = calc_direction_reward(car_x, car_y, heading, steering_angle, next_waypoint[0], next_waypoint[1])

    return 0.5 * direction_reward + 0.4 * pos_reward + 0.1 * speed_reward

def calc_direction_reward(car_x, car_y, heading, steering_angle, next_x, next_y):

    # Calculate the direction to next waypoint in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    next_waypoint_direction_from_car = math.degrees(math.atan2(next_y - car_y, next_x - car_x))

    # Calculate the difference between the direction to the next waypoint and the heading direction of the car
    direction_reward = 0.0
    direction_diff = next_waypoint_direction_from_car - heading
    if direction_diff > 180:
        direction_diff = direction_diff - 360
    elif direction_diff < -180:
        direction_diff = direction_diff + 360

    if abs(direction_diff) < 45:
        direction_reward = (45 - abs(direction_diff)) / 90 + 0.5
    # Car is pointing to the right of the next waypoint but steers to the left    
    elif direction_diff > 0: 
        if steering_angle > 10:
            direction_reward = 0.4
        elif steering_angle > 0:
            direction_reward = 0.2
    # Car is pointing to the left of the next waypoint but steers to the right     
    elif direction_diff < 0: 
        if steering_angle < -10:
            direction_reward = 0.4
        elif steering_angle < 0:
            direction_reward = 0.2
        
    return direction_reward