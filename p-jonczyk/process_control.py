'''This test suite contains 9 passing tests. '''
import pytest
from seleniumbase import BaseCase
from basic_methods import BasicMethods as bm
import config
import constants as const
import time


class TestProcessContol(BaseCase):

    def set_process_control_starting_point(self, single_control=False, multiple_items=False, parameters=False, control_action=False, controls=False):
        '''Sets starting point for testing Process control configurations
            SET ONLY ONE VARIABLE TO True
        Parameters:

        signal_control (boolen): If True opens Signal Control list

        multiple_items (boolen): If True opens Multiple items controls assignent lsit

        parameters (boolen): If True opens Parameters list

        control_actions (boolen): If True opens Control actions list

        controls (boolen): If True opens Controls list

        '''
        self.open(config.url)
        bm.log_in(self, config.valid_username, config.valid_password)
        self.wait_for_element(const.toast_msg_success_selector)
        self.go_to(config.url_process_control)
        setting = [(single_control, const.process_config_signal_control_selector),
                   (multiple_items, const.process_config_multiple_items_selector),
                   (parameters, const.process_config_parameters_selector),
                   (control_action, const.process_config_control_actions_selector),
                   (controls, const.process_config_controls_selector)]

        for boolen, selector in setting:
            if boolen == True:
                self.click(selector)

    def add_parameter_to_table(self, parameter_name, parameter_type=None,  save=True):
        '''Opens Add parameter window and fill Parameter name

        Parameters:

        parameter_name (str): name of new parameter

        parameter_type (str): selector of parameter type from available list
                                if None - default parameter type

        save (boolen): If True - clicks Save button'''

        self.click(const.parameters_add_btn)
        self.type(const.parameters_param_name_selector, parameter_name)
        if parameter_type is not None:
            self.click_chain([const.parameters_param_type_list_selector,
                              parameter_type])
        if save == True:
            self.click(const.parameters_param_save_btn)

    def delete_element_from_table(self, element_name):
        ''' Delete selected element from table defined by its name

        Parameter:

        parameter_name (str): Name of parameter to be deleted'''

        bm.choose_element_from_table(self, element_name)
        self.click_chain([const.parameters_delete_btn,
                          const.dialog_accept_btn_selector])
        time.sleep(1)

    def add_control_action(self, control_action_name, parameter_name=None, save=True):
        ''' Adds new contorl action

        Parameters:

        control_action_name (str): Name of control action to be added

        parameter_name (str): Name of parameter to be added'''

        self.click(const.control_actions_add_btn)
        self.type(const.control_actions_name_selector, control_action_name)
        # additional option slider
        self.click('#mat-slide-toggle-5')
        if parameter_name is not None:
            self.click_chain([const.control_actions_add_param_btn,
                              const.control_actions_add_param_name_selector])
            self.type(const.control_actions_add_param_name_selector,
                      parameter_name)
            self.click_chain(
                ['#mat-slide-toggle-53', const.control_actions_param_list_confirm])

        if save == True:
            self.click(const.control_actions_add_save_btn)

    def add_control(self, control_name, control_action_name=None, save=True):
        ''' Adds new contorls in Control configuration

        Parameters:

        control_name (str): Name of control to be added

        control_action_name (str): Name of control action to be added'''

        self.click(const.controls_add_btn)
        self.type(const.controls_name_selector, config.control_name)
        if control_action_name is not None:
            self.click_chain([const.controls_add_control_action,
                              const.controls_add_control_action_name_selector])
            self.type(const.controls_add_control_action_name_selector,
                      control_action_name)
            self.click_chain(
                ['#mat-slide-toggle-20', const.controls_add_control_action_confirm_btn])

        if save == True:
            self.click(const.controls_add_save_btn)

    def test_OpenParametersAddParam_ParamAppearsOnList(self):
        '''Checks if when user opens Parameter list and adds new parameter
        then parameter apperas on the list'''

        self.set_process_control_starting_point(parameters=True)
        self.add_parameter_to_table(
            config.parameter_name, parameter_type=const.parameters_param_type_integer)
        self.assert_element(f'td:contains({config.parameter_name})')
        self.delete_element_from_table(config.parameter_name)

    def test_OpenParametersChooseAndDelParam_ParamShouldNotBeOnList(self):
        '''Checks if when user opens Parameter list, select parameter and delet it
        then parameter should not be on the list'''

        self.set_process_control_starting_point(parameters=True)
        self.add_parameter_to_table(config.parameter_name)
        self.delete_element_from_table(config.parameter_name)
        self.assert_element_absent(f'td:contains({config.parameter_name})')

    def test_OpenParametersChooseAndDuplicateParam_AddParamWidnowAppera(self):
        ''' Checks if when user select parameter and clicks duplicate then Add parameter
        window appears with filled Parameter name the same as choosen parameter to be duplicated'''

        self.set_process_control_starting_point(parameters=True)
        self.add_parameter_to_table(config.parameter_name)
        self.click(const.parameters_duplicate_btn)
        self.assert_element('span:contains("Add parameter")')
        self.assert_element('mat-error:contains("Name must be unique")')
        self.click(const.parameters_param_cancel_btn)
        self.delete_element_from_table(config.parameter_name)

    def test_AddParameterChooseParamTypeList_ListViewAppears(self):
        ''' Checks if when user choose parameter type List,
        then list view apperas'''

        self.set_process_control_starting_point(parameters=True)
        self.add_parameter_to_table(
            config.parameter_name, parameter_type=const.parameters_param_type_list_type, save=False)
        self.assert_element('.selection-list-details-container')
        self.assert_element('input[id="mat-input-1"]')

    def test_AddParameterChooseParamTypeList_ListViewAppears(self):
        ''' Checks if when user choose parameter type List and add list element,
        then added list element appears in proper field in Parameter configuration'''

        self.set_process_control_starting_point(parameters=True)
        self.add_parameter_to_table(
            config.parameter_name, parameter_type=const.parameters_param_type_list_type, save=False)
        self.click('.selection-list-details-container .ic_mw_addbutton')
        self.type('.edit-text-value-modal-container textarea',
                  config.parameter_config_list_elem)
        self.click('[id="mat-dialog-1"] .ic_mw_savebutton')
        self.assert_element('input[id="mat-input-1"]')

    def test_ParameterConfigChooseParamTypeInt_FieldsAppears(self):
        ''' Checks if when user choose parameter type Integer value
        then additional fileds appears'''

        self.set_process_control_starting_point(parameters=True)
        self.add_parameter_to_table(
            config.parameter_name, parameter_type=const.parameters_param_type_integer, save=False)
        self.assert_element('input[name="parameterMin"]')
        self.assert_element('input[name="parameterMax"]')

    def test_ParameterConfigChooseParamTypeFloat_FieldsAppers(self):
        ''' Checks if when user choose parameter type Float value
        then additional fileds appears'''

        self.set_process_control_starting_point(parameters=True)
        self.add_parameter_to_table(
            config.parameter_name, parameter_type=const.parameters_param_type_float, save=False)
        self.assert_element('input[name="parameterMin"]')
        self.assert_element('input[name="parameterMax"]')

    def test_ParameterConfigBothCommentSlidersOn_FieldsAppear(self):
        ''' Checks if when user check on bothe comment available and
        comment required sliders then additional fileds appears'''

        self.set_process_control_starting_point(parameters=True)
        self.add_parameter_to_table(config.parameter_name, save=False)
        self.click_chain([const.parameters_comment_available_slider,
                          const.parameters_comment_required_slider])
        self.assert_element('[name="optionalParameterCommentType"]')
        self.assert_element('[name="requiredParameterCommentForNOKType"]')

    def test_ParameterConfigParamRequiredOn_ShowsYesOnList(self):
        ''' Checks if when user check on slider of parameter required
        then it shows "Yes" in parameter required column in tabel'''

        self.set_process_control_starting_point(parameters=True)
        self.add_parameter_to_table(config.parameter_name, save=False)
        self.click(const.parameters_param_required_slider)
        self.click(const.parameters_param_save_btn)
        self.assertEqual(self.get_text(
            bm.choose_element_from_table(self, config.parameter_name, get_value=3)), "Yes",
            "Parameter required shows: No")
        self.delete_element_from_table(config.parameter_name)

    def test_AddParamAssingInControlActionsAssignInControls_ShouldBeVisibleInActionsAndThenInControls(self):
        ''' Checks if when user Adds new parameter, assigns it in Control Actions
        to new Control Action and assings that Control Action in Controls
        then all those steps should be done flawlessly and be visible
        in each mentioned configuration of process control.'''

        self.set_process_control_starting_point(parameters=True)
        self.add_parameter_to_table(config.parameter_name)
        self.go_to(config.url_process_control_control_actions)
        self.add_control_action(
            config.control_action_name, config.parameter_name)
        bm.choose_element_from_table(self, config.control_action_name)
        self.assert_element(f'td:contains({config.control_action_name})')
        self.go_to(config.url_process_control_controls)
        self.add_control(config.control_name, config.control_action_name)
        bm.choose_element_from_table(self, config.control_name)
        self.assert_element(f'td:contains({config.control_name})')
        self.delete_element_from_table(config.control_name)
        self.go_to(config.url_process_control_control_actions)
        self.delete_element_from_table(config.control_action_name)
        self.go_to(config.url_process_control_parameters)
        self.delete_element_from_table(config.parameter_name)
