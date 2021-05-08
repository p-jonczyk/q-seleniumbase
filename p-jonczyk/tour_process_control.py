import pytest
from seleniumbase import BaseCase
from basic_methods import BasicMethods as bm
import config
import constants as const
import time


class ProcessControlTour(BaseCase):

    def cleaning_after_tour(self, element_name):
        bm.choose_element_from_table(self, element_name)
        self.click_chain([const.parameters_delete_btn,
                          const.dialog_accept_btn_selector])
        time.sleep(1)

    def test_process_control_tour(self):

        self.open(config.url)

        # LOG IN
        bm.basic_tour_step(self, msg="Welcome to Process control configuration tutorial !",
                           title="Q-name")
        bm.basic_tour_step(self, msg="1. Log in",
                           title="YOUR TASK", click=False)
        bm.basic_tour_step(self, msg="2. Add new parameter",
                           title="YOUR TASK", click=False)
        bm.basic_tour_step(self, msg="3. Add new control action with assigned parameter and invoke mode: 'on shift start' ",
                           title="YOUR TASK", click=False)
        bm.basic_tour_step(self, msg="4. Add new control with assigned control action",
                           title="YOUR TASK", click=False)
        bm.basic_tour_step(
            self, msg="There are two ways of log in...", title="Let's Log In !")
        bm.basic_tour_step(self, msg="Using Barcode",
                           selector=const.barcode_authorization_button)
        bm.basic_tour_step(self, msg="And using Password/PIN which will be used in this tutorial.",
                           selector=const.username_authorization_button)
        bm.basic_tour_step(self, msg="First enter the Username",
                           selector=const.authorization_user_selector,
                           filler=config.valid_username, click=False, fill=True)
        bm.basic_tour_step(self, msg="Next enter the Password/PIN",
                           selector=const.authorization_password_selector,
                           filler=config.valid_password, click=False, fill=True)
        bm.basic_tour_step(self, msg="And click 'Enter' or 'Confirm' button.",
                           selector=const.authorization_confirm_btn)
        bm.basic_tour_step(self, msg="You are logged in!", title="Congratulations!",
                           selector=const.logged_username)

        # GO TO PROCCESS CONTROL
        bm.basic_tour_step(
            self, msg="Let's go to Process control configuration.", click=False)
        bm.basic_tour_step(self, msg="In order to do that you have to click 'Process control' icon.",
                           selector=const.process_control_main_selector)
        bm.basic_tour_step(
            self, msg="Now you need to click 'Configuration'",
            selector=const.process_control_configuration_selector)
        bm.basic_tour_step(
            self, msg="You are in Process control configuration. Which you may see on the top panel.",
            title="Congratulation!", selector='ul li:nth-child(3)', click=False)
        bm.basic_tour_step(
            self, msg="Your next step is adding a parameter.", click=False)
        bm.basic_tour_step(
            self, msg="You may do that by clicking 'Parameters' configuration icon",
            selector=const.process_config_parameters_selector)

        # ADDING PARAMETER
        bm.basic_tour_step(
            self, msg="Now you see list of parameters which were already added. If parameter is selected you are able to:",
            title="List of Parameters")
        bm.basic_tour_step(
            self, msg="Duplicate",
            selector=const.parameters_duplicate_btn, click=False)
        bm.basic_tour_step(
            self, msg="Delete",
            selector=const.parameters_delete_btn, click=False)
        bm.basic_tour_step(
            self, msg="and Edit them.",
            selector=const.parameters_edit_btn, click=False)
        bm.basic_tour_step(
            self, msg="In this tutorial you are interested in adding new parameter, so let's click 'Add' button",
            selector=const.parameters_add_btn)
        bm.basic_tour_step(
            self, msg="There are few settings of parameter. For purpose of this tutorial you will leave parameter at defult settings.",
            title="Add parameter", click=False)
        bm.basic_tour_step(
            self, msg="As you see you have to enter 'Parameter name' which is required...",
            selector=const.parameters_param_name_selector,
            click=False, fill=True, filler=config.parameter_name)
        bm.basic_tour_step(self, msg="All what's left is to save new parameter by clicking 'Save' button",
                           selector=const.parameters_param_save_btn)
        bm.basic_tour_step(self, msg="You have added your first parameter !", title="Congratulations!",
                           click=False)
        bm.basic_tour_step(self, msg="Now you have to go back to Process control configurations. You can do that by clicking:",
                           click=False)
        bm.basic_tour_step(self, msg="Process control in the path of top panel...",
                           selector='ul li:nth-child(3)', click=False)
        bm.basic_tour_step(self, msg="or 'Back arrow' button also visible on the top panel. So let's click",
                           selector=const.back_btn_selector)

        # CONTROL ACTIONS
        bm.basic_tour_step(self, msg="Your next desitnation will be 'Control actions' configuration",
                           click=False)
        bm.basic_tour_step(self, msg="You may do that by clicking 'Control actions' configuration",
                           selector=const.process_config_control_actions_selector)
        bm.basic_tour_step(
            self, msg="Now you see list of added Control actions. Similar to parameters you may:",
            title="List of Control actions")
        bm.basic_tour_step(
            self, msg="Duplicate",
            selector=const.parameters_duplicate_btn, click=False)
        bm.basic_tour_step(
            self, msg="Delete",
            selector=const.parameters_delete_btn, click=False)
        bm.basic_tour_step(
            self, msg="and Edit them.",
            selector=const.parameters_edit_btn, click=False)
        bm.basic_tour_step(
            self, msg="Your goal is to add new control action, so let's click Add button.",
            selector=const.parameters_add_btn)
        bm.basic_tour_step(
            self, msg="First you need to fill 'Control action name' which is required.",
            selector=const.control_actions_name_selector, fill=True,
            filler=config.control_action_name, click=False)
        bm.basic_tour_step(
            self, msg="Add control action have various settings. As was mentioned at the beginning you are interested in:",
            title="Add control action", click=False)
        bm.basic_tour_step(self, msg="'On shift start' control action, so let's turn it on.",
                           selector=const.control_actions_toggle_shift_start)
        bm.basic_tour_step(self, "Now let's assign to this control action the parameter which you have added previously",
                           title="Assigne parameter to control action", click=False)
        bm.basic_tour_step(self, "You may do it by clicking Add button on the left side",
                           selector=const.control_actions_add_param_btn)
        bm.basic_tour_step(self, "Parameter list is visible. You may choose the parameter of interest.",
                           click=False, title="Parameter list")
        bm.basic_tour_step(self, "You may toggle more than one parameter to your control action!",
                           click=False, title="REMEMBER")
        bm.basic_tour_step(self, "Let's find your parameter on the list.",
                           selector=const.control_actions_add_param_name_selector,
                           fill=True, filler=config.parameter_name)
        bm.basic_tour_step(self, "Now we have to assign that parameter, so let's toggle it on.",
                           title="Great!", selector=const.control_actions_toogle_parameter)
        bm.basic_tour_step(self, "Confirm assigment",
                           selector=const.control_actions_param_list_confirm)
        bm.basic_tour_step(self, "Finally save your new control action.",
                           selector=const.control_actions_add_save_btn)
        bm.basic_tour_step(self, "Your first control action was created!",
                           title="Congratulations!", click=False)
        bm.basic_tour_step(self, "Let's go back to Process control configuration menu.",
                           selector='ul li:nth-child(3)')

        # CONTROLS
        bm.basic_tour_step(self, msg="Your last desitnation will be 'Controls' configuration",
                           click=False)
        bm.basic_tour_step(self, msg="As previously click 'Controls' configuration",
                           selector=const.process_config_controls_selector)
        bm.basic_tour_step(
            self, msg="List of Controls allow you the same actions as Parameter list and Control actions list:",
            title="List of Controls")
        bm.basic_tour_step(
            self, msg="Duplicate",
            selector=const.parameters_duplicate_btn, click=False)
        bm.basic_tour_step(
            self, msg="Delete",
            selector=const.parameters_delete_btn, click=False)
        bm.basic_tour_step(
            self, msg="and Edit them.",
            selector=const.parameters_edit_btn, click=False)
        bm.basic_tour_step(
            self, msg="Let's click Add button and create your own control.",
            selector=const.controls_add_btn)
        bm.basic_tour_step(
            self, msg="First you need to fill 'Control name' which is required.",
            selector=const.controls_name_selector, fill=True,
            filler=config.control_name, click=False)
        bm.basic_tour_step(
            self, msg="Add control also have various settings. For now you are interested in assigning your control action to new control.   ",
            title="Add control", click=False)
        bm.basic_tour_step(self, "Clicking Add button on the left side",
                           selector=const.controls_add_control_action)
        bm.basic_tour_step(self, "Control actions list is visible. It looks similar to the one from task.",
                           click=False, title="Assign control actions")
        bm.basic_tour_step(self, "You may toggle more than one parameter to your control action!",
                           click=False, title="REMEMBER")
        bm.basic_tour_step(self, "Let's find your control action on the list.",
                           selector=const.controls_add_control_action_name_selector,
                           fill=True, filler=config.control_action_name)
        bm.basic_tour_step(self, "Now we have to assign that parameter, so let's toggle it on.",
                           title="Great!", selector=const.controls_add_control_action_toggle)
        bm.basic_tour_step(self, "Confirm assigment",
                           selector=const.controls_add_control_action_confirm_btn)
        bm.basic_tour_step(self, "Finally save your new control.",
                           selector=const.controls_add_save_btn)
        bm.basic_tour_step(self, "Your first control was created!",
                           title="Congratulations!", click=False)

        # ENDING
        bm.basic_tour_step(self, "You can go to the main page which is 'Modules'",
                           title="Ending", click=False)
        bm.basic_tour_step(self, "Click 'hamburger menu' on the top panel",
                           title="Ending", selector=const.hamburger_btn_selector)
        bm.basic_tour_step(self, "Click 'CMMS' button",
                           title="Ending", selector=const.hamburger_cmms_btn)
        bm.basic_tour_step(self, "Finally click 'Go to CMMS' button",
                           title="Ending", selector=const.hamburger_go_to_cmms_btn)
        bm.basic_tour_step(self, "Good luck!",
                           title="THE END", click=False)

        # CLEANING
        self.go_to(config.url_process_control_controls)
        self.cleaning_after_tour(config.control_name)
        self.go_to(config.url_process_control_control_actions)
        self.cleaning_after_tour(config.control_action_name)
        self.go_to(config.url_process_control_parameters)
        self.cleaning_after_tour(config.parameter_name)
