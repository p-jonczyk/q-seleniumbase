'''Contains basic test methods'''
from seleniumbase import BaseCase
import random
import string
import config
import constants as const
import time


class BasicMethods(BaseCase):

    def log_in(self, username, password):
        '''Log In into the system

        Parameters:

        username (str): valid username

        password (str): valid password'''

        self.type(const.authorization_user_selector, username)
        self.type(const.authorization_password_selector, password+"\n")

    def log_out(self):
        '''Log out of the system'''

        self.click_chain([const.user_menu_btn_selector,
                          'span:contains("Logout")'])

    def type_generated_string(self, length, input_field=None):
        '''Fill given input field with given length string 
        or generates long string if input_field = ""

        Parameters:

        lenght (int): length of generated string

        input_field (selector=""): selector to input field for string '''

        char_set = string.ascii_letters + string.digits + string.punctuation + "ąęóźżńłć"
        random_string = ''.join(random.choice(char_set) for _ in range(length))
        if input_field is not None:
            self.type(input_field, random_string)
        else:
            return random_string

    def change_logged_user_with_barcode(self, valid_barcode):
        '''Change user when logged in with valid barcode'''

        self.click_chain([const.user_menu_btn_selector,
                          '.menu-content-container button-menu-item:nth-of-type(4)',
                          const.barcode_authorization_button])
        self.type(const.authorization_barcode_selector,
                  valid_barcode+"\n")

    def choose_element_from_table(self, element_name, column=1, get_value=None):
        ''' Returns selector of element from table based on choice of column
        or if get_value is not None then return selector of specyfic cell of table

        Parameters:

        element_name (str): Name of element

        column (int): number of column (from 1 - default)

        get_value (int): Number of column from which data will be obtained '''

        self.type(
            f'td[aria-colindex="{column}"] input[aria-label="Filter cell"]', element_name)
        time.sleep(1)
        row = 1
        while self.is_element_present(f'.dx-scrollable-simulated table tr[aria-rowindex="{row}"]'):
            self.click(
                f'.dx-scrollable-simulated table tr[aria-rowindex="{row}"]')
            stored_element = self.get_text(
                f'.dx-scrollable-simulated table tr[aria-rowindex="{row}"] td[aria-colindex="{column}"]')
            if stored_element == element_name:
                self.click(
                    f'.dx-scrollable-simulated table tr[aria-rowindex="{row}"]')
                if get_value is not None:
                    return (f'.dx-scrollable-simulated table tr[aria-rowindex="{row}"] td[aria-colindex="{get_value}"]')
                break
            else:
                row += 1

    def basic_tour_step(self, msg, selector='app-main', title=None, add_theme=None,
                        alignment=None, duration=None, filler=None, name=None,
                        main_theme="Shepherd", click=True, fill=False):
        ''' Creats tour step with action

        Parameters:

        msg (str): Description of step

        selector (str): Selector for tour and action - default left-top

        name (str): Name of following tour

        title (str): Title of tour step

        add_theme (str): Additional theme of step (square, arrow etc.)

        alignment (str): Alignment of msg/title

        duration (int): Time after step is continued automatically

        filler (str): Input if fill=True

        main_theme (str): Theme of whole tour

        click (boolen): If true - action - click selector

        fill (boolen): If true - action - type filler to selectro
        '''
        self.create_tour(theme=main_theme)
        self.add_tour_step(msg, selector, name, title,
                           add_theme, alignment, duration)
        self.play_tour()
        if click == True:
            self.click(selector)
        if fill == True:
            self.highlight_update_text(selector, filler)
