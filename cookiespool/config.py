# Redis数据库地址
REDIS_HOST = 'localhost'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = None

# 产生器使用的浏览器
BROWSER_TYPE = 'Chrome'

# 产生器类，如扩展其他站点，请在此配置
GENERATOR_MAP = {
    'robo': 'RoboCookiesGenerator'
}

# 测试类，如扩展其他站点，请在此配置
TESTER_MAP = {
    'robo': 'RoboValidTester',
}

TEST_URL_MAP = {
    'robo': 'https://gw.datayes.com/rrp_adventure/web/kmap/company/info?ticker=000001',
}

# 产生器和验证器循环周期
CYCLE = 3600

# API地址和端口
API_HOST = '0.0.0.0'
API_PORT = 5000

# 生成器进程
GENERATOR_PROCESS = True
# 验证器进程
VALID_PROCESS = True
# API接口进程
API_PROCESS = True
