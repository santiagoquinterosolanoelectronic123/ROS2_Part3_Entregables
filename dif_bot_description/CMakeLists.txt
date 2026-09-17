cmake_minimum_required(VERSION 3.8)
project(dif_bot_description)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# ===== DEPENDENCIAS DE COMPILACIÓN =====
find_package(ament_cmake REQUIRED)

# NOTA: joint_state_publisher, joint_state_publisher_gui, robot_state_publisher,
# rviz2 y xacro son dependencias de EJECUCIÓN (exec_depend), no de compilación.
# Por eso NO se declaran aquí con find_package().

# ===== INSTALAR ARCHIVOS (URDF, LAUNCH, RVIZ, WORLDS) =====
install(DIRECTORY
  urdf
  launch
  rviz
  worlds
  config
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
