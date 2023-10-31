# Robocup Medium Size League Ball Manipulation using PPO

This project uses reinforcement learning with PPO algorithm to train a simulated robot in Robocup Medium Size League environment to manipulate a ball with high dexterity. The environment is created using Gymnasium-Robotics library, which provides a realistic simulation of the robot and ball.

## Prerequisites:

- Python 3.x
- Gymnasium-Robotics
- gym
- Stable Baselines3

## Installation

- Clone the repository: `git clone https://github.com/MohammedBadra/robot-ball-gym.git`
- Install the required packages: `pip install -r requirements.txt`

## Training and testing

The training and testing script is a rough draft. Meanwhile, when ready, you should be able to experiment with it as follows:

1. Define the environment by creating a `gym.Env` class.
2. Create a PPO policy using the `stable_baselines3.ppo.PPO` class.
3. Train the model using the `stable_baselines3.PPO` class and the `gymnasium-robotics` environment.

## Environment Configuration

The dimensions of the robot and ball can be changed in the `robocup_environment.py` file. The reward function and other environment parameters can be modified in the same file.

## Acknowledgments

- Gymnasium-Robotics library: https://github.com/Farama-Foundation/Gymnasium-Robotics
- Stable Baselines3: https://github.com/DLR-RM/stable-baselines3
