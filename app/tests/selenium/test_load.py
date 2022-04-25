import pytest
from selenium import webdriver


@pytest.mark.frontend
class TestTitle:
	def setup_method(self):
		self.driver = webdriver.Remote(
			command_executor='http://selenium-hub:4444/wd/hub',
			options=webdriver.ChromeOptions())
		self.vars = {}

	def teardown_method(self):
		self.driver.quit()

	def test_title(self):
		self.driver.get("https://recipe-remix.tech/")
		self.driver.set_window_size(788, 816)
		assert self.driver.title == "Recipe Remix"
