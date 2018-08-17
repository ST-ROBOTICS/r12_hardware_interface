#r12_hardware_interface
ROS package providing a FollowJointTrajectoryAction interface to the ST Robotics r12 arm. Requires r12_moveit_config and my_r12_description packages. Based on Adam Heins' python shell for the r12.

## Use
joint_trajectory_action_server.py receives a follow_joint_trajectory action and moves the arm according to the given trajectory, while returning its position during the move on the action's feedback topic. Joint_state_remapper.py takes this feedback and remaps it to a JointState message, which is continuously published on the /joint_states topic. Both nodes must be running. The joint_trajectory_action_server.py is only able to follow a position based trajectory.
