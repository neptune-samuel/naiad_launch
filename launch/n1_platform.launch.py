# This file is part of NAIAD launch scripts
# date : 2023-10-07
# revision lists:
# 
from launch import LaunchDescription
from launch_ros.actions import Node

#
# see README.md
#

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='naiad_chassis',
            executable='naiad_chassis',
            parameters=[{'serial_port' : '/dev/ttyTHS2'}, 
                        {'serial_options' : '460800'},
                        {'debug_tcp_port' : 9600},
                        {'sacp_dump_list': ['9601:0:609,610,611,614,615,616,617,619',
                              '9602:0:634,635,636,639,640,641,642,644',
                              '9605:0:410,413,414,415,416,417,418',
                              '9606:0:430,438,439,440,441,442,443',
                              '9609:0:310,313,314,315,316,317,318',
                              '9611:0:812,813,815,814,816',
                              '9612:0:862,863,865,864,866',
                              '9613:0:912,913,915,914,916',
                              '9614:0:962,963,965,964,966' 
                              '9620:0:1000,1001,1002,1003,1007,1008,1010,1011,1012',
                              '9621:0:1020,1021,1026,1027,1028',
                              '9622:0:1017,1018,1023,1024,1025'
                             ] 
                        }
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
                        {'monitor_processes' : ['plc_pairlink:default:9504', 
                                                'serial_logd:default:9503', 
                                                '_ros2_daemon:default:9502', 
                                                'naiad_system:ros:9505', 
                                                'naiad_chassis:ros:9506',
                                                'naiad_fog:ros:9507',
                                                'naiad_cyberbot:ros:9508'
                                            ]                  
                        },
                        {'data_dump_service' : 9501}
                    ]
        )
    ])
