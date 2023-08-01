
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='naiad_chassis',
            executable='naiad_chassis',
            name='n1_chassis'
        ),
        Node(
            package='naiad_fog',
            executable='naiad_fog',
            namespace='fog_main',
            name='n1_fog',
            parameters=[{'serial_port' : '/dev/ttyTHS1'}, 
                        {'serial_options' : '115200'},
                        {'state_publish_period' : 100},
                        {'vofa_service' : '9701:0:gx,gy,gz,ax,ay,az,er,ey,ep'}]
        )
    ])

