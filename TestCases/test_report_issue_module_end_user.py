"""
Report Issue module end user test case
Author : Divya B
"""
from Pages.ReportIssueModuleEndUser import ReportIssueModuleEndUser
from TestCases.test_base import BaseTest
from Config.login_cred import LoginCred
import time


class TestReportIssueModuleEndUser(BaseTest):

    # def setUp(self):
    #     # to call the setUp() method of base class or super class.
    #     super().setUp()

    def test_report_issue_module_end_user(self):
        print("inside")
        self.driver.get("https://supporttest.condenastint.com/sp")
        time.sleep(3)
        login_cred_obj = LoginCred(self.driver)
        login_cred_obj.login_cred()
        time.sleep(40)
        self.report_issue_module_end_use_obj = ReportIssueModuleEndUser(self.driver)
        self.report_issue_module_end_use_obj.fill_report_issue_module_end_user()

"""PASSED"""