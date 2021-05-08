'''This test suite contains 11 passing tests. '''
import pytest
from seleniumbase import BaseCase
from basic_methods import BasicMethods as bm
import config
import constants as const
import time


class TestItems(BaseCase):

    def set_items_test_starting_point(self):
        '''Sets starting point for items testing:
        Logs in and redirects to items list'''

        self.open(config.url)
        bm.log_in(self, config.valid_username, config.valid_password)
        self.wait_for_element(const.toast_msg_success_selector)
        self.go_to(config.url_items)

    def get_items_data_of_choice(self, item_id, column):
        '''Returns item data (str) from items table according to choice of column:
        1. ID | 2.Name | 3.Group | 4.Unit

        Parameters:

        item_id (str): ID of item

        column (int): Number of specific item's data column'''

        bm.choose_element_from_table(self, item_id)
        row = self.get_attribute('.dx-selection', 'aria-rowindex')
        data = self.get_text(
            f'tbody:last-of-type > tr[aria-rowindex="{row}"] > td[aria-colindex="{column}"]')
        return data

    def add_item_to_table(self, item_id, item_name, item_group, item_unit):
        '''Adds item into item's table

        Parameters:

        item_id (str): ID of item

        name (str): Name of item

        group (str): Name of group to be selected form available groups

        unit (str): Unit of item to be selected form available units'''

        self.click(const.items_config_add_btn)
        self.fill_add_item_field(item_id, item_name, item_group, item_unit)

    def fill_add_item_field(self, item_id=None, item_name=None, item_group=None, item_unit=None, save=True):

        if item_id is not None:
            self.type(const.items_add_item_id_selector, item_id)
        if item_name is not None:
            self.type(const.items_add_item_name_selector, item_name)
        if item_group is not None:
            self.click_chain([const.items_add_item_group_selector,
                              f'span:contains({item_group})'])
        if item_unit is not None:
            self.click_chain(
                [const.items_add_item_unit_selector, f'span:contains({item_unit})'])
        if save == True:
            self.click(const.items_add_item_save_btn_selector)

    def delete_item_from_table(self, item_id):
        '''Deletes item form item's table definde by its item_id

        Parameters:

        item_id (str): ID of item'''

        bm.choose_element_from_table(self, item_id)
        self.click_chain([const.items_config_delete_btn,
                          const.dialog_accept_btn_selector])
        time.sleep(1)

    def edit_item_from_table(self, current_item_id, new_item_id, new_item_name, new_item_group, new_item_unit):
        '''Edits item which already exist

        Parameters:

        current_item_id (str): Current ID of item to be edited

        new_item_id (str): ID of item

        new_item_name (str): Name of item

        new_item_group (str): Name of group to be selected form available groups

        new_item_unit (str): Unit of item to be selected form available units'''

        bm.choose_element_from_table(self, current_item_id)
        self.click(const.items_config_edit_btn)
        self.fill_add_item_field(
            new_item_id, new_item_name, new_item_group, new_item_unit)

    def reset_add_fields(self):
        '''Reset fields of Add item window'''
        self.click_chain(
            [const.items_add_item_cancel_btn_selector, const.items_config_add_btn])

    def test_OpenAppMenuNextCofigNextAppConfigNextItems_ItemsListAppears(self):
        '''Checks if when user opens Application menue, clicks Configuration,
        clicks Application Configuration and clicks Items then Items list should appear'''

        self.open(config.url)
        bm.log_in(self, config.valid_username, config.valid_password)
        self.click_chain([const.hamburger_btn_selector,
                          const.hamburger_config_btn,
                          const.application_config_btn,
                          const.app_config_items_btn])
        self.assert_element('q-panel:first-of-type')

    def test_OpenItemsConfigNoneItemSelected_DelEditBtnDisabledAddEnabled(self):
        '''Checks if when user opens Items configuration list and none item
        is selected then Delete and Edit button is disabeld
        while Add button is enabled.'''

        self.set_items_test_starting_point()
        self.assert_element('.reject button[disabled="true"]')
        self.assert_element('.edit button[disabled="true"]')
        # check if add button exist
        self.assert_element(const.items_config_add_btn)
        self.assert_element_absent('.accept button[disabled="false"]')

    def test_OpenItemsConfigSelectItem_DelEditAddBtnEnabled(self):
        '''Checks if when user opens Items configuration list and selects
        any item then all buttons Delete, Edit and Add are enabled'''

        self.set_items_test_starting_point()
        self.add_item_to_table(config.item_id, config.item_name,
                               config.item_group, config.item_unit)
        bm.choose_element_from_table(self, config.item_id)
        # check if buttons exist
        self.assert_element(const.items_config_delete_btn)
        self.assert_element(const.items_config_edit_btn)
        self.assert_element(const.items_config_add_btn)
        # check if are enabled
        self.assert_element_absent('.reject button[disabled="true"]')
        self.assert_element_absent('.edit button[disabled="true"]')
        self.assert_element_absent('.accept button[disabled="false"]')
        self.delete_item_from_table(config.item_id)

    def test_OpenItemsAddItem_ItemAppearsOnList(self):
        '''Checks if when user opens Items configuration, clicks Add,
        fills all input fields, clicks Save and clicks Confirm
        then toast message appears and added item appears on the list'''

        self.set_items_test_starting_point()
        self.add_item_to_table(config.item_id, config.item_name,
                               config.item_group, config.item_unit)
        self.assert_element(const.toast_msg_success_selector)
        bm.choose_element_from_table(self, config.item_id)
        self.assert_element(f'td:contains({config.item_id})')
        self.delete_item_from_table(config.item_id)

    def test_OpenItemsEditItem_ItemShowsChangedName(self):
        '''Checks if when user edit existing element name then item appears on the list
        which its name changed'''

        self.set_items_test_starting_point()
        self.add_item_to_table(config.item_id, config.item_name,
                               config.item_group, config.item_unit)
        self.edit_item_from_table(
            config.item_id, config.item_id, config.item_new_name, config.item_group, config.item_unit)
        self.assertNotEqual(config.item_name, self.get_items_data_of_choice(config.item_id, 2),
                            "Name of item has not changed")
        self.delete_item_from_table(config.item_id)

    def test_OpenItemsAddItemAndRemoveItem_ItemNotOnList(self):
        '''Checks if when user adds new item, clicks Delete and Confirm
        then toast message appears and item should not be on the list'''

        self.set_items_test_starting_point()
        self.add_item_to_table(config.item_id, config.item_name,
                               config.item_group, config.item_unit)
        self.delete_item_from_table(config.item_id)
        self.assert_element(const.toast_msg_success_selector)
        self.assert_element_not_present(f'td:contains({config.item_id})')

    def test_OpenItemsAddItemNotAllRequiredFieldFilled_SaveButtonDisabled(self):
        '''Checks if when user does not enter all required data while adding new item
        then Save button should be disabled'''

        elemen_to_to_be_asserted = '.custom-buttons-list-container button[disabled="true"]'
        self.set_items_test_starting_point()
        self.click(const.items_config_add_btn)
        # item id empty, rest filled
        self.fill_add_item_field(
            item_name=config.item_name, item_group=config.item_group, item_unit=config.item_unit)
        self.assert_element(elemen_to_to_be_asserted)
        # name of item empty, rest filled
        self.reset_add_fields()
        self.fill_add_item_field(
            item_id=config.item_id, item_group=config.item_group, item_unit=config.item_unit)
        self.assert_element(elemen_to_to_be_asserted)
        # group is not chosen, rest filled
        self.reset_add_fields()
        self.fill_add_item_field(
            item_id=config.item_id, item_name=config.item_name, item_unit=config.item_unit)
        self.assert_element(elemen_to_to_be_asserted)
        # unit is not chosen, rest filled
        self.reset_add_fields()
        self.fill_add_item_field(
            item_id=config.item_id, item_name=config.item_name, item_group=config.item_group)
        self.assert_element(elemen_to_to_be_asserted)
        # gropu and unit are not chosen, rest filled
        self.reset_add_fields()
        self.fill_add_item_field(
            item_id=config.item_id, item_name=config.item_name)
        self.assert_element(elemen_to_to_be_asserted)
        # id empty, group not chosen, rest filled
        self.fill_add_item_field(
            item_name=config.item_name, item_unit=config.item_unit)
        self.assert_element(elemen_to_to_be_asserted)

    def test_OpenItemsAddItemFillIdAndNameWithMaxString_ItemAppearsOnList(self):
        '''Checks if when user enters ID and Name of item with maximum allowed length (200 characters)
        then toast message pop-up and item appears on the list'''

        self.set_items_test_starting_point()
        generated_item_id = "a"*config.items_max_string_len
        generated_item_name = "b"*config.items_max_string_len
        self.add_item_to_table(
            generated_item_id, generated_item_name, config.item_group, config.item_unit)
        self.assert_element(const.toast_msg_success_selector)
        bm.choose_element_from_table(self, generated_item_id)
        self.assert_element(f'td:contains({generated_item_id})')
        self.delete_item_from_table(generated_item_id)

    def test_OpenItemsAddItemFillIdAndNameWithOverMaxString_SaveButtonDisabled(self):
        '''Checks if when user enters ID and Name of item with lenght over maximum allowed characters
        (over 200 characters) then Save button should be disabled'''

        self.set_items_test_starting_point()
        generated_item_id = "a"*config.items_over_max_string_len
        generated_item_name = "b"*config.items_over_max_string_len
        self.add_item_to_table(
            generated_item_id, generated_item_name, config.item_group, config.item_unit)
        self.assert_element(
            '.custom-buttons-list-container button[disabled="true"]')

    def test_OpenItemsAddItemFillFieldsClickCancel_ItemShouldNotAppearOnList(self):
        '''Checks if when user fills all required fields of Add item window correctly and clicks Cancel
        then Item should be added hence appear on the list'''

        self.set_items_test_starting_point()
        self.click(const.items_config_add_btn)
        self.fill_add_item_field(
            config.item_id, config.item_name, config.item_group, config.item_unit, save=False)
        self.click(const.items_add_item_cancel_btn_selector)
        self.assert_element_absent(const.toast_msg_success_selector)
        self.type(
            'td[aria-colindex="1"] input[aria-label="Filter cell"]', config.item_id)
        self.assert_element_not_present(f'td:contains({config.item_id})')

    def test_OpenItemsClickDeleteClickCancelClickNo_ItemShouldReaminOnList(self):
        '''Checks if when user select Item form list, clicks Delete button and clicks No
        then Item should remain on the list'''

        self.set_items_test_starting_point()
        self.add_item_to_table(config.item_id, config.item_name,
                               config.item_group, config.item_unit)
        bm.choose_element_from_table(self, config.item_id)
        self.click_chain([const.items_config_delete_btn,
                          const.dialog_cancel_btn_selector])
        self.assert_element(f'td:contains({config.item_id})')
        self.delete_item_from_table(config.item_id)
