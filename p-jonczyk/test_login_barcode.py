'''This test suite contains 3 passing tests. '''

import pytest
from seleniumbase import BaseCase
import config
from basic_methods import BasicMethods as bm
import constants as const


class TestLoginBarcode(BaseCase):

    def test_LoginBarcode_RedMsgIncorrectCredentials_Appear(self):
        '''Checks if red inform message appears when incorrect credentials'''

        self.open(config.url)
        self.click(const.barcode_authorization_button)
        self.type(const.authorization_barcode_selector,
                  config.invalid_barcode+"\n")
        self.assert_element(const.toast_msg_error_selector)

    def test_LoginBarcode_CorrectCredentials_GreenMsgAppearRedirected(self):
        '''Checks if green inform message apperas and if user has been redirected'''

        self.open(config.url)
        self.click(const.barcode_authorization_button)
        self.type(const.authorization_barcode_selector,
                  config.valid_admin_barcode+"\n")
        self.assert_element(const.toast_msg_success_selector)
        self.assertNotEqual(self.get_current_url(),
                            config.url, "Did not redirect")

    def test_InputLongBarcode_RedMsgIncorrectCredentialsAppear(self):
        '''Checks if when user enters very long Barcode system 
        will toast message incorrect credentials'''

        self.open(config.url)
        self.click(const.barcode_authorization_button)
        bm.type_generated_string(
            self, config.test_string_len, const.authorization_barcode_selector)
        self.click('span:contains("Confirm")')
        self.assert_element(const.toast_msg_error_selector)
