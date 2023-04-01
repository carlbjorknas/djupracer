# Idé: 
# Kombinera nedanstående för högsta belöning
# I första hand, bilen ska vara hyfsat i mitten
# I andra hand, bilen ska vara på väg åt rätt håll
# I tredje hand, bilen ska ha hög hastighet

import math

def reward_function(params):

    # input variables
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']        
    prev_waypoint = waypoints[closest_waypoints[0]]
    next_waypoint = waypoints[closest_waypoints[1]]

    pos_reward = reward_for_position(track_width, distance_from_center)

    if pos_reward < 1.0:
        return pos_reward

    heading_reward = reward_for_heading(heading, prev_waypoint, next_waypoint)

    return heading_reward

def reward_for_position(track_width, distance_from_center):
    track_side_width = track_width / 2
    off_center = distance_from_center / track_side_width
    off_center_percent = off_center * 100

    if off_center_percent < 50:
        return 1.0
    elif off_center_percent < 90:
        return 0.1
    else:
        return 1e-3

def reward_for_heading(heading, prev_waypoint, next_waypoint):
    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_waypoint[1] - prev_waypoint[1], next_waypoint[0] - prev_waypoint[0])
    # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

     # Penalize the reward if the difference is too large
    if direction_diff < 5:
        return 1.0
    if direction_diff < 10:
        return 0.5

    return 1e-3
    #return float(reward)
        


# "all_wheels_on_track": Boolean,        # flag to indicate if the agent is on the track
# "x": float,                            # agent's x-coordinate in meters
# "y": float,                            # agent's y-coordinate in meters
# "closest_objects": [int, int],         # zero-based indices of the two closest objects to the agent's current position of (x, y).
# "closest_waypoints": [int, int],       # indices of the two nearest waypoints.
# "distance_from_center": float,         # distance in meters from the track center 
# "is_crashed": Boolean,                 # Boolean flag to indicate whether the agent has crashed.
# "is_left_of_center": Boolean,          # Flag to indicate if the agent is on the left side to the track center or not. 
# "is_offtrack": Boolean,                # Boolean flag to indicate whether the agent has gone off track.
# "is_reversed": Boolean,                # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
# "heading": float,                      # agent's yaw in degrees
# "objects_distance": [float, ],         # list of the objects' distances in meters between 0 and track_length in relation to the starting line.
# "objects_heading": [float, ],          # list of the objects' headings in degrees between -180 and 180.
# "objects_left_of_center": [Boolean, ], # list of Boolean flags indicating whether elements' objects are left of the center (True) or not (False).
# "objects_location": [(float, float),], # list of object locations [(x,y), ...].
# "objects_speed": [float, ],            # list of the objects' speeds in meters per second.
# "progress": float,                     # percentage of track completed
# "speed": float,                        # agent's speed in meters per second (m/s)
# "steering_angle": float,               # agent's steering angle in degrees
# "steps": int,                          # number steps completed
# "track_length": float,                 # track length in meters.
# "track_width": float,                  # width of the track
# "waypoints": [(float, float), ]        # list of (x,y) as milestones along the track center