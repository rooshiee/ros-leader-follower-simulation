# ROS Leader–Follower Turtle Simulation

## Overview

This project implements an autonomous leader–follower simulation using the Robot Operating System (ROS) and turtlesim. A leader turtle is controlled through movement commands while follower turtles automatically track the leader using ROS TF transformations.

The project demonstrates fundamental robotics concepts including ROS node communication, publishers, subscribers, custom messages, custom services, launch files, and autonomous multi-agent behaviour.

## Features

- Autonomous leader–follower behaviour
- ROS TF broadcaster and listener
- Random turtle spawning
- Multiple ROS nodes
- Launch file configuration
- Custom ROS messages
- Custom ROS services
- Python implementation

## Technologies

- Robot Operating System (ROS)
- Python
- Turtlesim
- ROS TF
- Ubuntu Linux

## Project Structure

```
com760cw1_B01009366/

├── launch/
├── scripts/
├── msg/
├── srv/
├── urdf/
├── package.xml
└── CMakeLists.txt
```

## Key Components

- Leader turtle movement control
- Autonomous follower turtles
- TF-based position tracking
- Random spawning system
- Environment setup
- Custom communication using ROS messages and services

## Running the Project

1. Build the ROS workspace.
2. Source the workspace.
3. Launch the simulation using the provided launch file.
4. Observe the autonomous leader–follower behaviour inside turtlesim.

## Future Improvements

- Gazebo implementation
- TurtleBot integration
- Obstacle avoidance
- Multi-robot coordination
- Reinforcement learning navigation

## Demonstration

The following video demonstrates the autonomous leader–follower behaviour implemented using ROS and turtlesim.




https://github.com/user-attachments/assets/1f3fdebb-bb13-4f0b-bad1-dfe7bb40163f









## Project Background

This project was completed as part of the Robotics & AI module during the MSc Artificial Intelligence programme at Ulster University.

The repository has been retained in its original submission structure while being presented as part of my technical portfolio.
