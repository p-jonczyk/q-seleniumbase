'''This test suite contains 3 passing tests. '''

import pytest
from seleniumbase import BaseCase
from basic_methods import BasicMethods as bm
import config
import constants as const
import time


class TestLogout(BaseCase):

    def test_LogoutClicked_MsgUserRedirected(self):
        ''' Checks if when user open user's menu and press log out
        will be redirected to autorization page and message appear'''

        self.open(config.url)
        bm.log_in(self, config.valid_username, config.valid_password)
        self.click_chain([const.user_menu_btn_selector,
                          'span:contains("Logout")'])
        self.assert_element(const.toast_msg_success_selector)
        self.assertNotEqual(config.url, config.url_authorization,
                            "Did not redirect")

    def test_LoggedoutClickBackButton_StayOnAuthorizationPage(self):
        ''' Checks if when user logs out and click back button
         will still stay on authorization page'''

        self.test_LogoutClicked_MsgUserRedirected()
        self.go_back()
        self.assertEqual(self.get_current_url(),
                         config.url_authorization, "Redirected")

    def test_LoggedinClickedLogout_ShouldBeAbleToLogInAgain(self):
        '''Checks if user is able to log in just after user logged out'''

        self.open(config.url)
        bm.log_in(self, config.valid_username, config.valid_password)
        bm.log_out(self)
        # need to hard-code login because bm.log_in opens config.url
        time.sleep(1)
        self.type(const.authorization_user_selector, config.valid_username)
        self.type(const.authorization_password_selector,
                  config.valid_password+"\n")
        self.wait_for_element_visible(const.user_menu_btn_selector)
        self.assertNotEqual(self.get_current_url(),
                            config.url_authorization, "Redirected")
