import json
import argparse

from cookiespool.db import RedisClient
from cookiespool.scheduler import Scheduler


def set_robo_account(fp):
    conn = RedisClient('accounts', 'robo')
    with open(fp, 'r') as fp:
        robo_accounts = json.load(fp)

    for account in robo_accounts:
        result = conn.set(account['username'], account['password'])
        print('账号', account['username'], '录入成功' if result else '录入失败')


def main(fp):
    set_robo_account(fp)

    s = Scheduler()
    s.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('fp', help='path to your accounts json file')
    args = parser.parse_args()

    main(args.fp)
