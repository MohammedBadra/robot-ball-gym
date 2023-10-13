import gymnasium as gym

env = gym.make("FetchReach-v2")
env.reset()
obs, reward, terminated, truncated, info = env.step(env.action_space.sample())

# The following always has to hold:
assert reward == env.unwrapped.compute_reward(obs["achieved_goal"], obs["desired_goal"], info)
assert truncated == env.unwrapped.compute_truncated(obs["achieved_goal"], obs["desired_goal"], info)
assert terminated == env.unwrapped.compute_terminated(obs["achieved_goal"], obs["desired_goal"], info)

# However goals can also be substituted:
substitute_goal = obs["achieved_goal"].copy()

substitute_reward = env.unwrapped.compute_reward(obs["achieved_goal"], substitute_goal, info)
substitute_terminated = env.unwrapped.compute_terminated(obs["achieved_goal"], substitute_goal, info)
substitute_truncated = env.unwrapped.compute_truncated(obs["achieved_goal"], substitute_goal, info)