from re import A
import torch
import random
import numpy as np
from collections import deque
import level1

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:

    def __init__(self):
        self.n_games = 0
        self.epsilon = 0#randomness
        self.gamma = 0.9
        self.memory = deque(maxlen=MAX_MEMORY) # if full => popleft()
        #Todo model Trainer

    def get_state(self, level1):
        pass

    def remember(self, state, position, danger, ai_reward, done):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self, state, position, danger, ai_reward, done):
        pass

    def get_action(self, state):
        pass

def train():
    plot_scores = []
    plot_avg_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = level1.Level1()

    while True:

        #get old state
        state_old = agent.get_state(game)

        #get move
        final_move = agent.get_action(state_old)

        #perform move and get new_state
        ai_reward, done, score = game(final_move)
        state_new = agent.get_state(game)
        
        #train short memory
        agent.train_short_memory(state_old, final_move, ai_reward, state_new, done)

        #remember
        agent.remember(state_old, final_move, ai_reward, state_new, done)

        if done:
            # train long memory, plot result
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score
            #agent.model.save()

            print('Game', agent.n_games, 'Score', score, 'Record:', record)

            #TODO plot

if __name__ == '__main__':
    train()