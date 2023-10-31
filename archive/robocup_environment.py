import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
import gym_robotics

class RoboCupMSLEnv(gym.Env):
    """
    An extension to openAI' gym environment for Robocup Soccer Medium Size League
    """
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.action_space = spaces.Box(low=-1, high=1, shape=(2,))
        self.observation_space = spaces.Box(low=-1, high=1, shape=(4,))

        self.viewer = None
        self.state = None
        self.goal_position = np.array([0, 0])
        self.ball_position = None

        self.seed()
        self.reset()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        # Update the robot position based on the action
        robot_position = self.state[:2]
        robot_position += action * 0.1
        robot_position = np.clip(robot_position, -1, 1)
        self.state[:2] = robot_position

        # Update the ball position based on the robot-ball collision
        ball_position = self.state[2:]
        if np.linalg.norm(robot_position - ball_position) < 0.1:
            ball_position = robot_position + 0.1 * (ball_position - robot_position) / np.linalg.norm(ball_position - robot_position)
            self.state[2:] = ball_position

        # Calculate the reward based on the distance between the ball and the goal position
        distance = np.linalg.norm(ball_position - self.goal_position)
        reward = -distance

        # Terminate the episode if the ball reaches the goal
        done = (distance < 0.1)

        return self.state, reward, done, {}

    def reset(self):
        # Initialize the robot and ball positions randomly
        robot_position = self.np_random.uniform(low=-1, high=1, size=(2,))
        ball_position = self.np_random.uniform(low=-1, high=1, size=(2,))

        # Set the goal position to be on the opposite side of the arena
        goal_position = self.np_random.uniform(low=-1, high=1, size=(2,))
        goal_position *= np.array([1, -1])
        self.goal_position = goal_position

        # Set the state vector
        self.state = np.concatenate([robot_position, ball_position])

        return self.state

    def render(self, mode='human'):
        screen_width = 600
        screen_height = 600

        world_width = 2
        scale = screen_width / world_width
        robot_radius = 0.1 * scale
        ball_radius = 0.05 * scale
        goal_radius = 0.1 * scale

        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viewer(screen_width, screen_height)
            self.viewer.set_bounds(-world_width, world_width, -world_width, world_width)

            goal = rendering.make_circle(goal_radius)
            goal.set_color(0.5, 0.5, 0.5)
            self.viewer.add_geom(goal)

            robot = rendering.make_circle(robot_radius)
            robot.set_color(0.8, 0.3, 0.3)
            self.robot_trans = rendering.Transform()
            robot.add_attr(self.robot_trans)