Rqtconsole , rqt_logger_level
http://wiki.ros.org/ROS/Tutorials/UsingRqtconsoleRoslaunch

services and paramaters:
http://wiki.ros.org/ROS/Tutorials/UnderstandingServicesParams

Publisher , subscriber :
http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29 

http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29

http://wiki.ros.org/ROS/Tutorials/ExaminingPublisherSubscriber

ROSbag:

http://wiki.ros.org/ROS/Tutorials/Recording%20and%20playing%20back%20data

Tf tutorial:
http://wiki.ros.org/navigation/Tutorials/RobotSetup/TF

rosserial and tf:

http://wiki.ros.org/rosserial_arduino/Tutorials/Time%20and%20TF

teleop:
http://wiki.ros.org/ROS/NetworkSetup

http://wiki.ros.org/ROS/Tutorials/MultipleMachines

http://wiki.ros.org/robotican/Tutorials/Remote%20monitoring%20and%20control

http://wiki.ros.org/robotican/Tutorials/Command%20you%20robot%20with%20simple%20motion%20commands



ROS RGBD tutorial:

http://wiki.ros.org/kinect

http://wiki.ros.org/openni_launch/Tutorials/QuickStart

http://wiki.ros.org/rtabmap_ros/Tutorials/HandHeldMapping 

http://sauravag.com/2016/10/how-to-setup-kinect-with-ros-and-rgbd-slam/

http://wiki.ros.org/openni_launch/Tutorials/BagRecordingPlayback

http://wiki.ros.org/depth_image_proc

with libfreenect2:

1.Install the libfreenect stack:bluetronics@hp-omen:~$ rostopic list
/rosout

sudo apt install ros-kinetic-freenect-stack

2.Connect the Kinect to your computer and test the Kinect stack by running the convenient launch file (depth registration refers to the pairing of
color data with depth points):
roslaunch freenect_launch freenect.launch depth_registration:=true

3.Open up rviz in a separate terminal window (press ctrl + shift + T to open a new terminal tab):
rosrun rviz rviz

4.In the rviz options panel on the left, change Global Options > Fixed Frame to camera_link

5.In rviz add a new PointCloud2. Set its topic to  /camera/depth_registered/points.

6.Wait a few seconds for the point cloud to show up. You may need to rotate the viewport around to see it.

7.Play around with some of the different topics being sent out by the Kinect.







