# q_learning_agent.py
import numpy as np

class QLearningAgent:
    def __init__(self, state_size, action_size, learning_rate=0.1, discount_factor=0.99, exploration_rate=1.0):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.q_table = np.zeros((state_size, action_size))

    def act(self, state):
        if np.random.rand() < self.exploration_rate:
            return np.random.choice(self.action_size)
        return np.argmax(self.q_table[state, :])

    def learn(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state, :])
        td_target = reward + self.discount_factor * self.q_table[next_state, best_next_action]
        td_error = td_target - self.q_table[state, action]
        self.q_table[state, action] += self.learning_rate * td_error

    def update_exploration_rate(self, t):
        self.exploration_rate *= 0.995  # Example decay function
        self.exploration_rate = max(0.1, self.exploration_rate)  # Ensure exploration rate never reaches zero
