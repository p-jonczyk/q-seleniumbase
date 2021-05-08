'''This test suite contains 7 passing tests. '''
import pytest
from seleniumbase import BaseCase
from basic_methods import BasicMethods as bm
import config
import constants as const
import time


class TestTasksList(BaseCase):

    def get_task_name(self, row=1, column=2):
        '''Returns value of element in row of choice from column of choice

        Parameters:

        row (int): Row number of element

        column (int): Column number of value'''
        time.sleep(1)
        if self.is_element_present(f'.dx-scrollable-simulated table tr[aria-rowindex="{row}"]'):
            task_name = (self.get_text(
                (f'.dx-scrollable-simulated table tr[aria-rowindex="{row}"] td[aria-colindex="{column}"]')))
            return task_name

    def set_tasks_list_starting_point(self):
        ''' Sets starting point for Tasks List testing '''

        self.open(config.url)
        bm.log_in(self, config.valid_username, config.valid_password)
        self.wait_for_element(const.toast_msg_success_selector)
        self.go_to(config.url_tasks_list)

    def change_status(self, task_name, choice):
        '''Changes status of task

        Parameter:

        task_name (str): Name of task which status will be changed

        change (str): choice of change - [pause, finish, run,
                        set as new, cancel, restore, resume]'''

        setting = [("pause", const.tasks_list_change_status_pause_btn),
                   ("finish", const.tasks_list_change_status_finish_btn),
                   ("run", const.tasks_list_change_status_run_btn),
                   ("set as new", const.tasks_list_change_status_set_as_new_btn),
                   ("restore", const.tasks_list_change_status_restore_btn),
                   ("cancel", const.tasks_list_change_status_cancel_btn),
                   ("resume", const.tasks_list_change_status_resume_btn)]

        self.click(const.tasks_list_change_status_btn)
        for change, button in setting:
            if choice.lower() == change:
                self.click(button)

    def edit_task(self, task_name, task_name_new=None, required_quantity=None, priority=None, task_description=None, task_attribute=None, save=True):
        ''' Edits selected task depending on choice of parameters

        Parameters:

        task_name (str): Name of task to be edited

        task_name_new (str): New name of task which is edited

        required_qantity (str): Required quantity to be set (valid: integer)

        priority (str): Priority to be set (valid 0 - 100)

        task_description (str): Description of the task

        task_attribute (tuple): (name of attribute (str:case sensitive) , input (str) )

        save (boolen): If True - saves changes'''

        bm.choose_element_from_table(self, task_name, column=2)
        self.click(const.tasks_list_edit_btn)
        if task_name_new is not None:
            self.click(const.tasks_list_edit_task_name_selector)
            self.type(const.tasks_list_edit_task_name_selector, task_name_new)
        if required_quantity is not None:
            self.click(const.tasks_list_edit_task_required_quantity_selector)
            self.type(
                const.tasks_list_edit_task_required_quantity_selector, required_quantity)
        if priority is not None:
            self.click(const.tasks_list_edit_task_priority_selector)
            self.type(
                const.tasks_list_edit_task_priority_selector, priority)
        if task_description is not None:
            self.click(const.tasks_list_edit_task_description_selector)
            self.type(const.tasks_list_edit_task_description_selector,
                      task_description)
        if task_attribute is not None:
            self.click_chain([const.tasks_list_edit_task_attributes_btn,
                              f'mat-label:contains({task_attribute[0]})'])
            self.type(const.tasks_lists_edit_task_attributes_txt,
                      task_attribute[1])
            self.click_chain([const.dialog_accept_btn_selector,
                              const.tasks_list_edit_task_general_btn])
            # had to close window but changes in attributes are saved regardless
            self.click(const.tasks_list_edit_task_cancel_btn)
        if save == True:
            self.click(const.tasks_list_edit_task_save_btn)

    def test_SelectTaskChangeStatus_StatusChanged(self):
        '''Checks if when user opens Tasks list, chooses task and change its status
        then status of the task changes'''

        self.set_tasks_list_starting_point()
        self.assert_element_absent(const.tasks_list_change_status_btn)
        sotred_task_status = self.get_text(bm.choose_element_from_table(
            self, self.get_task_name(), column=2, get_value=3))
        self.assert_element(const.tasks_list_change_status_btn)
        self.change_status(self.get_task_name(), "pause")
        self.assertNotEqual(self.get_text(bm.choose_element_from_table(self, self.get_task_name(), column=2, get_value=3)),
                            sotred_task_status, "Status did not change")
        self.change_status(self.get_task_name(), "resume")

    def test_SelectTaskEditName_NameChanged(self):
        '''Checks if when user opens Tasks list, selects task, clicks Edit
        and changes Task name, then tasks name on list is changed'''

        self.set_tasks_list_starting_point()
        stored_task_name = self.get_task_name()
        self.edit_task(self.get_task_name(),
                       task_name_new=config.task_name_new)
        self.assertNotEqual(self.get_task_name(),
                            self.get_text(
                                bm.choose_element_from_table(
                                    self, config.task_name_new, column=2, get_value=2)),
                            "Task did not change name")
        self.edit_task(config.task_name_new,
                       task_name_new=stored_task_name)

    def test_SelectTaskEditRequiredQuantity_QuantityChangedOnList(self):
        '''Checks if when user opens Task List, select task, click Edit
        and changes Required quantity of task then Required quantity changes on list.'''

        self.set_tasks_list_starting_point()
        stored_quantity = self.get_text(
            bm.choose_element_from_table(self, self.get_task_name(), column=2, get_value=8))
        self.edit_task(self.get_task_name(),
                       required_quantity=config.task_required_quantity)
        self.assertNotEqual(stored_quantity,
                            self.get_text(
                                bm.choose_element_from_table(
                                    self, self.get_task_name(), column=2, get_value=8)),
                            "Required quantity of task did not change")
        self.edit_task(self.get_task_name(), required_quantity=stored_quantity)

    def test_SelectTaskEditPriorityToInvalideValue_ErrorAppearsSaveBtnDisabled(self):
        '''Checks if when user opens Task List, select task, click Edit
        and changes Priority to incorrect value then error message under
        priority field appears and save button is disabled'''

        self.set_tasks_list_starting_point()
        self.edit_task(self.get_task_name(),
                       priority=config.task_priority_invalide)
        self.assert_elements(
            const.tasks_list_edit_task_priority_error_empty, 'button[disabled="true"]')

    def test_SelectTaskEditPriorityAndRequiredQuantityToInvalideValue_ErrorsAppearsSaveBtnDisabled(self):
        '''Checks if when user opens Task List, select task, click Edit
        and changes Priority and Required quantity to incorrect value
        then error messages under priority and required quantity fields appear
        and save button is disabled'''

        self.set_tasks_list_starting_point()
        self.edit_task(self.get_task_name(),
                       required_quantity=config.task_required_quantity_invalide,
                       priority=config.task_priority_invalide, save=False)
        self.assert_elements(
            const.tasks_list_edit_task_priority_error_empty,
            const.tastk_list_edit_task_required_quantity_error,
            'button[disabled="true"]')

    def test_SelectTaskEditDescriptionTypeLongStr_DescriptionAppearsInDetails(self):
        '''Checks if when user opens Task list, selects task, edits its description
        with long string, then description appears in details of task in corresponding field.'''

        self.set_tasks_list_starting_point()
        generated_task_description = bm.type_generated_string(
            self, config.test_string_len)
        self.edit_task(self.get_task_name(),
                       task_description=generated_task_description)
        bm.choose_element_from_table(self, self.get_task_name(), column=2)
        self.click(const.tasks_list_details_btn)
        self.assertEqual(generated_task_description,
                         self.get_text(
                             const.tasks_list_details_task_descritpion_selector),
                         "Task descriptions are different")
        self.edit_task(self.get_task_name(), task_description=" ")

    def test_SelectTaskEditAttributs_EditedAttributesAppearsInDetails(self):
        '''Checks if when user opens Task list, selects task, edits its attribute,
        then changed attribute appears in details of task in corresponding place'''

        attribute_holder = (config.task_attribute_name,
                            config.task_attribute_value)
        self.set_tasks_list_starting_point()
        self.edit_task(self.get_task_name(),
                       task_attribute=attribute_holder, save=False)
        bm.choose_element_from_table(self, self.get_task_name(), column=2)
        self.click_chain([const.tasks_list_details_btn,
                          const.tasks_list_details_task_attributes_btn])
        bm.choose_element_from_table(self, config.task_attribute_name)
        self.assertEqual(config.task_attribute_value,
                         self.get_text(
                             f'td:contains({config.task_attribute_value})'),
                         "Attribure values are different")
