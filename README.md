# r12_hardware_interface
ROS package providing a FollowJointTrajectoryAction interface to the ST Robotics r12 arm. Requires r12_moveit_config and my_r12_description packages. Based on Adam Heins' python shell for the r12.

## Use
joint_trajectory_action_server.py receives a follow_joint_trajectory action and moves the arm according to the given trajectory, while returning its position during the move on the action's feedback topic. Joint_state_remapper.py takes this feedback and remaps it to a JointState message, which is continuously published on the /joint_states topic. Both nodes must be running. The action server is only able to follow a position based trajectory.

## Setup
NOTE: These ROS packages require the robot to be running a Forth overlay, adding the $RUN and $JL words. This can be checked with the ' $JL and ' $RUN commands; if the words are present, the robot should return OK. If this is not the case, please contact ST Robotics (ukoffice@strobotics.com)

Before any communication via ROS, the r12 arm must be set up using ROBOFORTH commands, externally from the ROS packages. The r12 python shell provided on github (https://github.com/ST-ROBOTICS/r12_python_shell) is suitable for this purpose. To set up the arm, press the RESET button on the controller, and then use the START command in the ROBOFORTH shell. If the robot was not in the HOME (vertical) position, it is also necessary to move it to roughly this position (DE-ENERGISE command, move robot by hand, ENERGISE command) and then send the CALIBRATE command.

After the robot has been set up, the joint_state_remapper.py node should be started (rosrun r12_hardware_interface joint_state_remapper.py) followed by the joint_trajectory_action_server.py node (rosrun r12_hardware_interface joint_trajectory_action_server.py). Starting the nodes in the opposite order or at the same time may cause unexpected errors.

## Emergency stop
Preempting the FollowJointTrajectory action should cause the arm to enter an emergency stop state and halt. However, if this fails it may be necessary to stop the robot by pressing the RESET button on the controller. After stopping the robot using the RESET button it will be necessary to perform the setup again before further use. 

Please exercise care when working with the robot arm, and stay out of the arm's envelope while in use.
