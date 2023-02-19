from stable_baselines3 import A2C

model = A2C("MlpPolicy", "CartPole-v1").learn(10000)