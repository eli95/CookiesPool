from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RoboCookies(object):
    def __init__(self, username, password, browser):
        self.url = 'https://robo.datayes.com/'
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 5)
        self.username = username
        self.password = password

    def open(self):
        """
        打开网页输入用户名密码并点击
        :return: None
        """
        self.browser.delete_all_cookies()
        self.browser.get(self.url)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="dy-global-header"]/div/div/a[1]'))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dyc-login-register"]/div[2]/div[3]/img'))).click()
        self.browser.find_element_by_xpath('//*[@id="username"]').send_keys(self.username)
        self.browser.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        self.browser.find_element_by_xpath(
            '//*[@id="dyc-login-register"]/div[2]/div[2]/div[1]/div[3]/div[1]/form/div[3]/div/div/span/button').click()

    def password_error(self):
        """
        判断是否密码错误
        :return:
        """
        try:
            return self.wait.until(
                EC.text_to_be_present_in_element((By.XPATH, '//div[@class="ant-form-explain"]'), '账号密码不匹配'))
        except TimeoutException:
            return False

    def login_successfully(self):
        """
        判断是否登录成功
        :return:
        """
        try:
            return bool(
                self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="header-user"]/span/img'))))
        except TimeoutException:
            return False

    def get_cookies(self):
        """
        获取Cookies
        :return:
        """
        return self.browser.get_cookies()

    def main(self):
        """
        破解入口
        :return:
        """
        self.open()
        if self.password_error():
            return {
                'status': 2,
                'content': '账号密码不匹配',
            }

        if self.login_successfully():
            cookies = self.get_cookies()
            return {
                'status': 1,
                'content': cookies,
            }
