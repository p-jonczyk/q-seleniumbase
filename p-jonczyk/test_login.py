''' This test suite contains 5 passing tests. '''

import pytest
from seleniumbase import BaseCase
from basic_methods import BasicMethods as bm
import config
import constants as const


class TestLogin(BaseCase):

    def test_Login_ConfirmButtonWhenOnlyUsername_Disabled(self):
        ''' Checks if "confirm" button is inactive when only username field is filled'''

        self.open(config.url)

        self.type(const.authorization_user_selector,
                  config.valid_username)
        self.assert_element('button[disabled="true"]')

    def test_Login_ConfirmButtonWhenOnlyPassword_Disabled(self):
        ''' Checks if "confirm" button is inactive when only password field is filled'''

        self.open(config.url)

        self.type(const.authorization_password_selector,
                  config.valid_password)
        self.assert_element('button[disabled="true"]')

    def test_Login_RedMsgWhenIncorectCredentials_Appear(self):
        '''Checks if red inform message appears when incorrect credentials'''

        self.open(config.url)
        bm.log_in(self, config.invalid_username, config.invalid_password)
        self.assert_element(const.toast_msg_error_selector)

    def test_Login_WhenCorrectCredentials_GreenMsgAppearRedirected(self):
        '''Checks if green inform message apperas and if user has been redirected'''

        self.open(config.url)
        bm.log_in(self, config.valid_username, config.valid_password)
        self.assert_element(const.toast_msg_success_selector)
        self.assertNotEqual(self.get_current_url(),
                            config.url, "Did not redirect")

    def test_InputLongStringCredentials_RedMsgIncorrectCredentialsAppear(self):
        '''Checks if when user enters very long Username and Password 
        system will show toast message incorrect credentials'''

        self.open(config.url)
        bm.type_generated_string(
            self, config.test_string_len, const.authorization_user_selector)
        bm.type_generated_string(
            self, config.test_string_len, const.authorization_password_selector)
        self.click('span:contains("Confirm")')
        self.assert_element(const.toast_msg_error_selector)
