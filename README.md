# Proyecto ROS2 Part 3 - Robot Diferencial

Proyecto final de la guia ROS 2 Part 3 (ROS 2 Jazzy). Implementa un robot diferencial completo con URDF/Xacro, sensores y simulacion en Gazebo Ignition.

## Paquetes incluidos

- **ros2_part3_launch**: Actividades 1 y 2 (launch files, argumentos y eventos).
- **dif_bot_description**: Actividades 4-9 (URDF/Xacro, sensores, RViz, Gazebo).

## Requisitos

- Ubuntu 22.04 o superior
- ROS 2 Jazzy Jalisco
- Gazebo Ignition (GZ Sim 8)
- Paquetes adicionales:

    sudo apt install ros-jazzy-ros-gz-sim ros-jazzy-ros-gz-bridge ros-jazzy-ros-gz-image ros-jazzy-xacro ros-jazzy-joint-state-publisher ros-jazzy-joint-state-publisher-gui ros-jazzy-teleop-twist-keyboard

## Instalacion

    cd ~/ros2_ws/src
    git clone https://github.com/santiagoquinterosolanoelectronic123/ros2_part3_proyecto.git
    cd ~/ros2_ws
    colcon build
    source install/setup.bash

## Uso

### Actividades 1 y 2 - Launch files

    ros2 launch ros2_part3_launch turtle_mimic.launch.py
    ros2 launch ros2_part3_launch main.launch.py

### Actividades 4-7 - Robot en RViz2

    ros2 launch dif_bot_description display_rviz.launch.py

### Actividad 8 - Simulacion en Gazebo (headless)

    ros2 launch dif_bot_description display_gz.launch.py

### Teleoperar el robot

    ros2 run teleop_twist_keyboard teleop_twist_keyboard

### Verificacion del sistema

    gz model --list
    ros2 topic hz /odom
    ros2 run tf2_tools view_frames
    rqt_graph

## Actividades cubiertas

| # | Actividad | Estado |
|---|-----------|--------|
| 1 | Launch files basicos (mimic) | Completo |
| 2 | Argumentos y lanzamiento jerarquico | Completo |
| 3 | Exploracion de TF2 | Completo |
| 4 | Construccion del robot en URDF/Xacro | Completo |
| 5 | Propiedades fisicas (colisiones e inercias) | Completo |
| 6 | Integracion de sensores (IMU, Lidar, Camara) | Completo |
| 7 | Visualizacion en RViz2 | Completo |
| 8 | Integracion con Gazebo Ignition | Completo |
| 9 | Mini-proyecto integrador | Completo |

## Estructura del proyecto

    ros2_part3_proyecto/
    ├── README.md
    ├── .gitignore
    ├── ros2_part3_launch/
    │   ├── launch/
    │   ├── CMakeLists.txt
    │   └── package.xml
    └── dif_bot_description/
        ├── urdf/
        ├── launch/
        ├── worlds/
        ├── rviz/
        ├── CMakeLists.txt
        └── package.xml

## Nota sobre WSL2

La GUI de Gazebo Ignition presenta un fallo de segmentacion en WSL2 debido a incompatibilidad con el backend grafico WSLg. La simulacion funciona correctamente en modo headless (sin GUI), y la verificacion se realiza a traves de topicos ROS 2. El codigo es completamente portable y funcionara con GUI en sistemas Linux nativos.

## Autor

Santiago Quintero Solano
