# train.py
import gymnasium as gym
import a1_soccer_env
import q_learning_agent

def main():
    env = gym.make('A1SoccerEnv-v0')
    agent = q_learning_agent.QLearningAgent(state_size=env.observation_space.n,
                                            action_size=env.action_space.n)

    episodes = 1000
    for e in range(episodes):
        state = env.reset()
        done = False
        while not done:
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            agent.learn(state, action, reward, next_state)
            state = next_state
        agent.update_exploration_rate(e)

        # Optional: Render the environment to visualize the training
        env.render()

if __name__ == "__main__":
    main()