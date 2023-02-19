import hunger_games as hg
from pettingzoo.test.api_test import api_test


def test_api():
    env = hg.env()
    api_test(env)
    env.close()


__name__ == '__main__' and test_api()