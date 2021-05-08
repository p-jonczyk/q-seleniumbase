'''This test suite contains 4 passing tests. '''
import pytest
from seleniumbase import BaseCase
from basic_methods import BasicMethods as bm
import config
import constants as const
import time


class ChangeUser(BaseCase):

    def change_user_clicked(self):
        '''Open change user window, when logged'''

        self.click_chain([const.user_menu_btn_selector,
                          'span:contains("Change user")'])

    def test_ChangeUserClicked_LoginWindowAppears(self):
        '''Checks if when user clicks "Change user" in menu option
        then login window appear'''

        self.open(config.url)
        bm.log_in(self, config.valid_username, config.valid_password)
        self.change_user_clicked()
        self.assert_element('.authorization-modal')

    def test_ChangeUserClickedAndCancle_LoggedInSamePageAndData(self):
        '''Checks if when user clicks "Change user" menu option and then clicks Cancel
        then user should not be redirected or logged out,
        name and sumranme should remain the same,
        '''

        self.open(config.url)
        bm.log_in(self, config.valid_username, config.valid_password)
        self.change_user_clicked()
        current_url = self.get_current_url()
        stored_username = const.logged_username
        self.click('.ic_mw_cancelbutton')
        self.assertEqual(self.get_current_url(),
                         current_url, "Redirected")
        self.assertEqual(const.logged_username,
                         stored_username, "Username changed")
        self.assert_element_absent(const.toast_msg_success_selector)

    def test_ChangeUserValidBarcode_LoginNewUserMsgUsernameChanged(self):
        ''' Checks if when user clicks "Change user" menu option and provide
        valid credentials (barcode) then user logs out and new user logs in,
        toast success message appear and displayed username changed'''

        # self.change_user_with_barcode_authorization()
        self.open(config.url)
        bm.log_in(self, config.valid_username, config.valid_password)
        stored_username = const.logged_username
        bm.change_logged_user_with_barcode(self, config.valid_user_barcode)
        self.assert_element(const.toast_msg_success_selector)
        self.assertNotEqual(self.get_text(const.logged_username),
                            stored_username, "Username did not change")

    def test_ChangeUserValideBarcodeLoginNewPressBackBtn_NewUserRemainsLogged(self):
        ''' Checks if when user clicks "Change user" menu option and provide
        valid credentials (barcode), new user logs in and clicks "Back" button
        then user should remain logged in '''

        self.open(config.url)
        bm.log_in(self, config.valid_username, config.valid_password)
        bm.change_logged_user_with_barcode(self, config.valid_user_barcode)
        time.sleep(1)
        stored_username = self.get_text(const.logged_username)
        self.click(const.back_btn_selector)
        self.assertEqual(self.get_text(const.logged_username),
                         stored_username, "Username change hence logged out.")
