from gymnasium.envs.registration import register


register(
    id='hunger-games-v0',
    entry_point='hunger_games.environment.env:env',
    # kwargs={'single_agent': True},
)
