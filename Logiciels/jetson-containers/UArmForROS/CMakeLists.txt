cmake_minimum_required(VERSION 2.8.3)
project(uarm)

find_package(catkin REQUIRED COMPONENTS
  # roscpp
  rospy
  std_msgs
  sensor_msgs
  geometry_msgs
  message_generation
  # visualization_msgs
  # interactive_markers
)
# add_message_files(
#   FILES
# 	Angles.msg
# 	Coords.msg
# 	CoordsWithTime.msg
# 	CoordsWithTS4.msg
# )

add_service_files(
  FILES
  MoveTo.srv
  MoveToJoints.srv
  Pump.srv
  AttachDetach.srv
)


catkin_python_setup()

generate_messages(
  DEPENDENCIES
  std_msgs
  sensor_msgs
  geometry_msgs
)

catkin_package(
  CATKIN_DEPENDS rospy std_msgs geometry_msgs sensor_msgs
)


# include_directories(
#   ${catkin_INCLUDE_DIRS}
# )
#
# add_executable(uarm_status src/uarm_status.cpp)
# target_link_libraries(uarm_status ${catkin_LIBRARIES})
