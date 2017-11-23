# coding:utf-8

'''
    登录功能实现
'''
import time

from selenium.common import exceptions as EC

import common


class Login(object):
	'''
		登录页面
	'''
	
	def __init__(self, username='xn018170'):
		
		self.user_info = self.init_params()
		self.url = self.user_info['url']
		self.driver = common.browser()
		self.driver.maximize_window()
		self.open()
		# self.type_username(self.user_info['locate']["loc_name"], self.user_info['auth']["username"])
		self.type_username(self.user_info['locate']["loc_name"], username)
		self.type_password(self.user_info['locate']["loc_password"], self.user_info['auth']["password"])
		self.type_submit(self.user_info['locate']["loc_button"])
		self.driver.implicitly_wait(30)
		self.accept_next_alert = True
	
	def open(self):
		'''打开特定Url'''
		self.driver.get(self.url)
	
	def type_username(self, loc, name):
		'''输入用户名'''
		try:
			self.driver.find_element_by_name(loc).clear()
			self.driver.find_element_by_name(loc).send_keys(name)
			return True
		except EC.NoSuchElementException as e:
			print(e)
			return False
	
	def type_password(self, loc, password):
		'''输入密码'''
		self.driver.find_element_by_name(loc).clear()
		self.driver.find_element_by_name(loc).send_keys(password)
	
	def type_submit(self, loc):
		self.driver.find_element_by_css_selector(loc).click()
	
	def quit(self):
		self.driver.quit()
	
	def is_element_present(self, how, what):
		try:
			self.driver.find_element(by=how, value=what)
		except EC.NoSuchElementException as e:
			print e.msg
			return False
		return True
	
	def is_alert_present(self):
		try:
			self.driver.switch_to_alert()
		except EC.NoAlertPresentException as e:
			print e.msg
			return False
		return True
	
	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally:
			self.accept_next_alert = True
	
	# 登录参数
	def init_params(self):
		
		user_info = {
			'locate': {
				'loc_name': 'j_username',
				'loc_password': 'j_password',
				'loc_button': 'input.login-btn',
				},  # 元素位置
			'auth': {
				'username': None,
				'password': '111111',
				},  # 用户名/密码
			'url': "http://10.15.14.48:8098/houseLoan/login",  # 登录URL
			# 'url': "http://10.18.4.57:8080/houseLoan/login",  # 登录URL
			}
		return user_info
	
	def _click_control(self, driver, how="xpath", locate=None):
		try:
			if self.is_element_present(how, locate):
				driver.find_element(how, locate).click()
				time.sleep(1)
		except EC.NoSuchElementException as e:
			print e
			raise e
	
	def _send_data(self, driver, how, locate="xpath", value=None):
		try:
			if self.is_element_present(how, locate):
				element = driver.find_element(how, locate)
				element.clear()
				element.click()
				element.send_keys(value)
				time.sleep(1)
		except EC.NoSuchElementException as e:
			print e
			raise e


if __name__ == '__main__':
	Login()
