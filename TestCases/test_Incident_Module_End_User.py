"""Incident Module end user test case"""

import unittest
from selenium import webdriver
from TestCase.BaseTestCase import TestBaseTestCase
from Pages.IncidentEndUser import IncidentEndUser
from TestCases.test_base import BaseTest
import time
from Config.login_cred import LoginCred

"""PASSED"""

class TestIncidentEndUser(BaseTest):

    # def setUp(self):
    #     # to call the setUp() method of base class or super class.
    #     super().setUp()

    def test_incident_page_end_user(self):
        print("inside")

        self.driver.get("https://supporttest.condenastint.com/sp")
        time.sleep(3)
        login_cred_obj = LoginCred(self.driver)
        login_cred_obj.login_cred()
        time.sleep(40)
        self.incident_end_use_obj = IncidentEndUser(self.driver)
        self.incident_end_use_obj.fill_incident_end_user_form()

        # self.test_obj = IncidentEndUser(self.driver)
        # self.test_obj.test_fun()

    # def tearDown(self):
    #     # To do the cleanup after test has executed.@
    #     super().tearDown()



