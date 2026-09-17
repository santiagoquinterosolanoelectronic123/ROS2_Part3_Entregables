import os
from os.path import join
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    pkg = get_package_share_directory('dif_bot_description')
    world_file = LaunchConfiguration('world',
        default=join(pkg, 'worlds', 'my_world.sdf'))
    gz_args = LaunchConfiguration('gz_args',
        default='--headless-rendering -r -s --render-engine ogre')

    robot_description = ParameterValue(
        Command(['xacro ', join(pkg, 'urdf', 'robot_gz.urdf.xacro')]),
        value_type=str
    )

    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'use_sim_time': True, 'robot_description': robot_description}]
    )

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': [gz_args, ' ', world_file]}.items()
    )

    spawn = Node(
        package='ros_gz_sim',
        executable='create',
        name='spawn_diff_bot',
        output='screen',
        arguments=['-topic', '/robot_description', '-name', 'diff_bot',
                   '-allow_renaming', 'true', '-z', '0.2']
    )

    spawn_after = TimerAction(period=5.0, actions=[spawn])

    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='ros_gz_bridge',
        parameters=[{'use_sim_time': True}],
        arguments=[
            '/joint_states@sensor_msgs/msg/JointState[gz.msgs.Model',
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
            '/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist',
            '/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry',
            '/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V',
            '/imu@sensor_msgs/msg/Imu[gz.msgs.IMU',
            '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan',
            '/camera/image_raw@sensor_msgs/msg/Image[gz.msgs.Image',
        ],
        output='screen'
    )

    return LaunchDescription([
        DeclareLaunchArgument('world', default_value=world_file),
        DeclareLaunchArgument('gz_args',
                              default_value='--headless-rendering -r -s --render-engine ogre'),
        gz_sim, rsp, spawn_after, bridge
    ])
