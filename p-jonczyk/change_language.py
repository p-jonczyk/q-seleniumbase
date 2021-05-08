'''This test suite contains 5 passing tests. '''
import pytest
from seleniumbase import BaseCase
from basic_methods import BasicMethods as bm
import config
import constants as const


class ChangeLanguage(BaseCase):

    language_reference = 'span:contains("Change application language")'
    change_language_btn_selector = '.menu-content-container button-menu-item:last-of-type'

    def login_and_click_change_app_language(self):
        '''Open config.url, login and open Change application language window'''

        self.open(config.url)
        bm.log_in(self, config.valid_username, config.valid_password)
        self.click_chain([const.user_menu_btn_selector,
                          self.change_language_btn_selector])

    def change_language(self, language):
        '''Changes application language to language of choice

        Parameters:

        language (str): language of choice '''

        if language.lower() == "polish":
            language_selector = '.language-wrapper-container button:first-of-type'
        elif language.lower() == "english":
            language_selector = '.language-wrapper-container button:last-of-type'

        self.click_chain([const.user_menu_btn_selector,
                          self.change_language_btn_selector,
                          language_selector, '.ic_mw_savebutton', const.dialog_accept_btn_selector])

    def check_language(self, language):
        '''Use to check what is current language of application.
        If False then ERROR

        Parameters:

        language (str): language of choice'''

        self.click(const.user_menu_btn_selector)
        if language.lower() == "polish":
            self.assert_element_not_present(self.language_reference)
        elif language.lower() == "english":
            self.assert_element_present(self.language_reference)
        self.click(const.user_menu_btn_selector)

    def test_ClickChangeAppLanguage_WindowAppear(self):
        '''Checks if when logged user opens User menu and click Change application language
        then change language window should appear'''

        self.login_and_click_change_app_language()
        self.assert_element('.modal-content')

    def test_ClickChangeAppLanguageCancle_LanguageNotChanged(self):
        '''Checks if when logged user open User menu, click Change application language
        and click Cancle then language remain unchanged'''

        self.login_and_click_change_app_language()
        self.click('.ic_mw_cancelbutton')
        self.check_language("english")

    def test_ClickChangeAppLanguageConfirmSame_LanguageNotChanged(self):
        '''Checks if when logged user open User menu, click Change application language,
        choose the same language, click Confirm and click Yes then language remain unchanged'''

        self.open(config.url)
        bm.log_in(self, config.valid_username, config.valid_password)
        self.change_language("English")
        self.check_language("English")

    def test_ClickChangeAppLanguageConfirmDifferent_LanguageChanged(self):
        '''Checks if when logged user open User menu, click Change application language,
        choose different language, click Confirm and click Yes then language should change'''

        self.open(config.url)
        bm.log_in(self, config.valid_username, config.valid_password)
        self.change_language("Polish")
        self.check_language("Polish")
        # return to English language for other future tests
        self.change_language("English")

    def test_ChangeOneUserLanguage_OtherUserLanguageUnchanged(self):
        '''Checks if when language is changed for one user then language of other user
        remain unchanged'''

        self.open(config.url)
        bm.log_in(self, config.valid_username, config.valid_password)
        self.check_language("English")
        bm.change_logged_user_with_barcode(self, config.valid_user_barcode)
        self.change_language("Polish")
        self.check_language("Polish")
        bm.change_logged_user_with_barcode(self, config.valid_admin_barcode)
        self.check_language("English")
        # return to English language for future tests
        bm.change_logged_user_with_barcode(self, config.valid_user_barcode)
        self.change_language("English")
