# This file is part of NAIAD launch scripts
# date : 2023-10-07
# revision lists:
# 

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([           
        Node(
            package='naiad_cyberbot',
            executable='naiad_cyberbot'
        ),    
    ])
