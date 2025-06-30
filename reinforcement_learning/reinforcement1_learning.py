#reinforcement learning (RL)

#key concepts
#1. agent
#2. environment
#3. state
#4. action
#5. reward 
#6. policy

import numpy as np
import random

#define evironment parameters
position = 5
actions = 2

#intialize the q-table
Q = np.zeros((10, actions))

#define episodes
episodes = 1000
learning_rate = 0.8
gamma = 0.9
epsilon = 0.3

#training the loop
for episode in range(episodes):
    state = random.randint(0, position - 1)
    
#action selection
    if random.uniform(0, 1) < epsilon:
        action = random.randint(0, actions - 1)
    else:
        action = np.argmax(Q[state, :])
        
#take action and observe reward
    if action == 0:  # move left
        next_state = max(0, state - 1)
    else:  # move right 
        next_state = min(position - 1, state + 1)

#reward
    if next_state == position - 1:
        reward = 10
    else:
        reward = -1
        
#update Q-value
    Q[state, action] = Q[state, action] + learning_rate * (reward + gamma * np.max(Q[next_state, :]) - Q[state, action])    
    
#transition to next state
    state = next_state
    
#display the Q-table
print("Q-table after training:")
print(Q)
#test the agent
state = 0
while state < position - 1:
    action = np.argmax(Q[state, :])
    if action == 0:  # move left
        next_state = max(0, state - 1)
    else:  # move right
        next_state = min(position - 1, state + 1)
    
    print(f"State: {state}, Action: {action}, Next State: {next_state}")
    state = next_state
#final state
print(f"Final State: {state}")
#display the final state
if state == position - 1:
    print("Reached the goal!")  
else:
    print("Did not reach the goal.")
#end of the code


#assignment:
#train RL agent to navigate to cross the road with action right, left, right