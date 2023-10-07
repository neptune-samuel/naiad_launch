# This file is part of NAIAD launch scripts
# date : 2023-10-07
# revision lists:
# 
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='naiad_chassis',
            executable='naiad_chassis',
            parameters=[{'serial_port' : '/dev/ttyTHS2'}, 
                        {'serial_options' : '460800'},
                        {'debug_tcp_port' : 9600}
                    ]
        ),
        Node(
            package='naiad_chassis',
            executable='naiad_minirc',
            parameters=[{'tcp_port' : 9800}, 
                        {'continuous_mode' : False},
                        {'motion_control_period' : 50}
                    ]
        ),        
        Node(
            package='naiad_fog',
            executable='naiad_fog',
            parameters=[{'serial_port' : '/dev/ttyTHS1'}, 
                        {'serial_options' : '115200'},
                        {'state_publish_period' : 100},
                        {'vofa_service' : '9701:gx,gy,gz,ax,ay,az,er,ey,ep'}
                    ]
        ),
        Node(
            package='naiad_system',
            executable='naiad_system',
            parameters=[{'polling_interval' : 1000}, 
                        {'pairlink_server_port' : 9595},
                        {'monitor_processes' : 'plc_pairlink,_ros2_daemon,naiad_system:ros,naiad_chassis:ros,naiad_fog:ros,naiad_cyberbot:ros'}
                    ]
        )
    ])
