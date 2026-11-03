^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package elite_robots_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.1.0 (2026-11-03)
------------------
* Add CS63A and CS630 models, including kinematic and physical parameters, joint limits, and visual and collision meshes.
* Add CS63A and CS630 to the supported robot types in the Xacro descriptions and RViz launch file.
* Add maintainer contact information.
* Use the public GitHub clone URL in the English and Chinese READMEs.

1.0.0 (2026-07-28)
------------------
* Initial release for ROS 2 Humble.
* Added Xacro and URDF descriptions for the Elite Robots CS and LS series,
  including CS63, CS66, CS66A, CS68, CS612, CS616, CS618F, CS620, CS625,
  CS520H, and LS65.
* Added joint limits, kinematic, physical, and visual parameters for the
  supported robot models.
* Added visual and collision meshes, RViz2 configuration, and a launch file
  for inspecting robot descriptions.
* Added support for safety limits, TF prefixes, ros2_control integrations,
  simulated hardware, and configurable initial joint positions.
* Added tests for Xacro/URDF generation and the robot description launch file.
