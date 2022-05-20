# Agent
# Environment
# policy
# reward
# *render,  gym

import os
import random

"""
    0 1 2 3 4
    5 6 7 8 9
    ....
    .
"""

class Discrete:
    def __init__(self,num_actions: int):
        self.n = num_actions
    def sample(self):
        return random.randint(0, self.n-1)


class Environment:
    # X,Y plane: UP, DOWN, RIGHT, LEFT
    seeker, goal = (0,0), (4,4)
    info = {'seeker': seeker, 'goal': goal}
    def __init__(self, *args, **kwargs):
        self.action_space = Discrete(4)
        self.observation_space = Discrete(25)
    
    def reset(self):
        self.seeker = (0,0)        
        return self.get_observation()
    
    def get_observation(self):
        return 5*self.seeker[0]+self.seeker[1]
    
    def get_reward(self):
        return 1 if self.seeker == self.goal else 0
    
    def is_done(self):
        return self.seeker == self.goal
    
    def step(self, action):
        if action == 0:   # move down
            self.seeker = (min(self.seeker[0]+1,4), self.seeker[1])
        elif action == 1: # move left
            self.seeker = (self.seeker[0], max(self.seeker[1]-1,0))
        elif action == 2: # move up
            self.seeker = (max(self.seeker[0]-1,0), self.seeker[1])
        elif action == 3: # move right
            self.seeker = (self.seeker[0], min(self.seeker[1]+1,4))
        else:
            raise ValueError("Invalid action")
        return self.get_observation(), self.get_reward(), self.is_done(), self.info

    def render(self, *args, **kwargs):
        os.system('cls' if os.name == 'nt' else 'clear')
        grid = [['| ' for _ in range(5)] + ["|\n"] for _ in range(5)]
        grid[self.goal[0]][self.goal[1]] = '|G'
        grid[self.seeker[0]][self.seeker[1]] = '|S'
        print(''.join([''.join(grid_row) for grid_row in grid]))
        
import numpy as np
class Policy:
    def __init__(self, env):
        self.state_action_table = [[0 for _ in range(env.action_space.n)] for _ in range(env.observation_space.n)]
        self.action_space = env.action_space
        
    def get_action(self, state, explore=True, epsilon=0.1 ):
        if explore and random.uniform(0,1) < epsilon:
            return self.action_space.sample()
        return np.argmax(self.state_action_table[state])
        

import time 
env = Environment()
experiences = []
policy = Policy(env)
state = env.reset()
while not env.is_done():
    # random_action = env.action_space.sample()
    action = policy.get_action(state)
    next_state, reward, done, info = env.step(action)
    experiences.append([state, action, reward, next_state])    
    state = next_state
    time.sleep(0.1)
    env.render()
        

print(experiences)