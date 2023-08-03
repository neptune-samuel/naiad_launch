
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='naiad_chassis',
            executable='naiad_chassis',
            name='n1_chassis',
            parameters=[{'serial_port' : '/dev/ttyTHS2'}, 
                        {'serial_options' : '460800'},
                        {'debug_tcp_port' : 9600}
                    ]
        ),
        Node(
            package='naiad_fog',
            executable='naiad_fog',
            name='n1_fog',
            parameters=[{'serial_port' : '/dev/ttyTHS1'}, 
                        {'serial_options' : '115200'},
                        {'state_publish_period' : 100},
                        {'vofa_service' : '9701:gx,gy,gz,ax,ay,az,er,ey,ep'}
                    ]
        )
    ])

