import gymnasium as gym
import mujoco
import numpy as np

from gymnasium.envs.registration import register

register(
    id='A1SoccerEnv-v0',
    entry_point='a1_soccer_env:A1SoccerEnv')

class A1SoccerEnv(gym.Env):
    def __init__(self):
        super().__init__()

        # Load the MuJoCo model
        self.model = mujoco.load_model_from_path('a1/xml/a1.xml')
        self.sim = mujoco.MjSim(self.model)

        # Define action and observation spaces
        self.action_space = gym.spaces.Box(low=-1, high=1, shape=(12,), dtype=np.float32)
        self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(some_shape,), dtype=np.float32)

    def step(self, action):
        # Apply the action to the simulation
        self.sim.data.ctrl[:] = action
        self.sim.step()

        # Get the new observation, reward, and done flag
        observation = self._get_observation()
        reward = self._get_reward()
        done = self._get_done()

        return observation, reward, done, {}

    def reset(self):
        self.sim.reset()
        return self._get_observation()

    def render(self, mode='human'):
        mujoco.MjViewer(self.sim).render()

    def _get_observation(self):
        # Extract relevant information from the simulation for the observation
        robot_qpos = self.sim.data.qpos.flat.copy()
        ball_pos = self.sim.data.get_body_xpos('ball')
        return np.concatenate([robot_qpos, ball_pos])

    def _get_reward(self):
        # Compute reward based on the current state of the simulation
        ball_pos = self.sim.data.get_body_xpos('ball')
        reward = -np.linalg.norm(ball_pos - target_pos)  # Reward for moving ball closer to target
        return reward

    def _get_done(self):
        # Determine whether the episode is done
        ball_pos = self.sim.data.get_body_xpos('ball')
        done = np.linalg.norm(ball_pos - target_pos) < some_threshold  # Episode is done if ball is close to target
        return done

# Define target position for the ball
target_pos = np.array([10, 0, 0])