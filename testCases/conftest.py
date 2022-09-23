import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

@pytest.fixture()
def setup():
    serv = Service("C:\\Users\\vinothsc\\selenium driver\\geckodriver.exe")
    return webdriver.Firefox(service=serv)