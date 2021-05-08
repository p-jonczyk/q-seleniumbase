'''Contains test constants'''

# MESSAGE SELECTORS
toast_msg_success_selector = ".ui-toast-message-success"
toast_msg_error_selector = ".ui-toast-message-error"


# INPUT SELECTORS
authorization_user_selector = 'input[name="username"]'
authorization_password_selector = 'input[name="password"]'
authorization_barcode_selector = 'input[name="barcode"]'
authorization_confirm_btn = '.login-button button'
# BUTTON SELECTORS

# Authorization
barcode_authorization_button = 'image-button[icon="ic_mw_barcode"]'
username_authorization_button = 'image-button[icon="ic_mw_log_password"]'
# Main page
user_menu_btn_selector = 'mat-icon.ic_mw_terminal'
back_btn_selector = '.top-bar-buttons-container button:nth-child(1)'
hamburger_btn_selector = '.mat-accent .hamburger'
production_btn_selector = '.title-container h1:contains("Production")'

# Dialog windows buttons
dialog_accept_btn_selector = '.ic_mw_orderlist'
dialog_cancel_btn_selector = 'app-dialog-message-box .ic_mw_cancelbutton'

# Hamburger menu
hamburger_config_btn = '.dx-scrollview-content > div:last-of-type mat-icon'
application_config_btn = '.dx-scrollview-content span:first-of-type'
models_config_btn = '.dx-scrollview-content span:last-of-type'
hamburger_cmms_btn = '.ic_mw_callcraftsman'
hamburger_go_to_cmms_btn = '.dx-scrollview-content span:first-of-type'

# hamburher app configuration
app_config_items_btn = '.with-top-margin div:nth-child(3) div .clickable'
# hamburger models configuration

# ITEMS CONFIGURATION SELECTORS
items_config_add_btn = '.accept button'
items_config_edit_btn = '.edit button'
items_config_delete_btn = '.reject button'

# add window selectors

items_add_item_id_selector = 'input[placeholder="SKU"]'
items_add_item_name_selector = 'input[placeholder="Name"]'
items_add_item_group_selector = 'mat-select[formcontrolname="idGroup"]'
items_add_item_unit_selector = 'mat-select[formcontrolname="idUnit"]'
items_add_item_save_btn_selector = 'custom-buttons-list .ic_mw_savebutton'
items_add_item_cancel_btn_selector = 'custom-buttons-list .ic_mw_cancelbutton'

# PROCESS CONTROL CONFIGURATION SELECTORS
process_control_main_selector = '.container-wrapper div:nth-child(4)'
process_control_configuration_selector = '[icon="ic_mw_settings"] .container'
process_config_signal_control_selector = '.container-wrapper module-presenter:nth-child(1)'
process_config_multiple_items_selector = '.container-wrapper module-presenter:nth-child(2)'
process_config_parameters_selector = '.container-wrapper module-presenter:nth-child(3)'
process_config_control_actions_selector = '.container-wrapper module-presenter:nth-child(4)'
process_config_controls_selector = '.container-wrapper module-presenter:nth-child(5)'

# Parameters selectors

parameters_add_btn = '.ic_mw_addbutton'
parameters_edit_btn = '.ic_mw_edit'
parameters_delete_btn = '.ic_mw_cancelbutton'
parameters_duplicate_btn = '.ic_mw_duplicate'

parameters_param_name_selector = '[id="parameterName"] textarea'
parameters_param_save_btn = items_add_item_save_btn_selector
parameters_param_cancel_btn = '.button-content-container div:contains("Cancel")'
parameters_param_type_list_selector = '[id="parameterType"] mat-select'

# parameters types
parameters_param_type_yes_no = 'mat-option[id="mat-option-0"]'
parameters_param_type_text = 'mat-option[id="mat-option-1"]'
parameters_param_type_integer = 'mat-option[id="mat-option-2"]'
parameters_param_type_float = 'mat-option[id="mat-option-3"]'
parameters_param_type_list_type = 'mat-option[id="mat-option-4"]'

# parameters settings
parameters_param_required_slider = '[id="mat-slide-toggle-1"]'
parameters_comment_available_slider = '[id="mat-slide-toggle-2"]'
parameters_comment_required_slider = '[id="mat-slide-toggle-3"]'

# Control actions selectors

# control actions setting
control_actions_add_btn = parameters_add_btn

control_actions_name_selector = '[id="controlActionName"] textarea'
control_actions_add_save_btn = items_add_item_save_btn_selector
control_actions_add_param_btn = '.control-action-details-content-container-parameters .ic_mw_addbutton'
control_actions_add_param_name_selector = '.select-modal-content .dx-texteditor-input'
control_actions_param_list_confirm = 'app-select-modal .ic_mw_savebutton'

control_actions_toggle_shift_start = '#mat-slide-toggle-6'
control_actions_toogle_parameter = '[for="mat-slide-toggle-56-input"]'
# Controls selectors

controls_add_btn = parameters_add_btn

controls_name_selector = '[id="controlName"] textarea'
controls_add_control_action = '.control-details-content-container-parameters .ic_mw_addbutton'
controls_add_control_action_name_selector = control_actions_add_param_name_selector
controls_add_control_action_confirm_btn = control_actions_param_list_confirm
controls_add_save_btn = control_actions_add_save_btn

controls_add_control_action_toggle = '[for="mat-slide-toggle-76-input"]'
# Tasks list selectors

tasks_list_change_status_btn = '.mat-button-base:contains("Change status")'
tasks_list_edit_btn = parameters_edit_btn
tasks_list_details_btn = '.ic_mw_infoorder'

# edit task
tasks_list_edit_task_name_selector = 'input[formcontrolname="taskName"]'
tasks_list_edit_task_required_quantity_selector = 'input[formcontrolname="requiredQuantity"]'
tasks_list_edit_task_priority_selector = 'input[formcontrolname="priority"]'
tasks_list_edit_task_description_selector = 'textarea[formcontrolname="taskDescription"]'
tasks_list_edit_task_save_btn = items_add_item_save_btn_selector
tasks_list_edit_task_cancel_btn = items_add_item_cancel_btn_selector
tasks_list_edit_task_attributes_btn = '.mat-tab-label-content:contains("Attributes")'
tasks_list_edit_task_general_btn = '.mat-tab-label-content:contains("General")'

# edit task errors
tasks_list_edit_task_priority_error_value = '#mat-error-2'
tasks_list_edit_task_priority_error_empty = '#mat-error-3'
tastk_list_edit_task_required_quantity_error = '#mat-error-3'

# edit task attributes
tasks_lists_edit_task_attributes_txt = '.edit-attribute-value-modal-container input'


# change status
tasks_list_change_status_pause_btn = '.modal-content span:contains("Pause")'
tasks_list_change_status_run_btn = '.modal-content span:contains("Run")'
tasks_list_change_status_cancel_btn = '.modal-content span:contains("Cancel")'
tasks_list_change_status_set_as_new_btn = '.modal-content span:contains("Set as new")'
tasks_list_change_status_finish_btn = '.modal-content span:contains("Finish")'
tasks_list_change_status_restore_btn = '.modal-content span:contains("Restore")'
tasks_list_change_status_resume_btn = '.modal-content span:contains("Resume")'

# task details

tasks_list_details_task_descritpion_selector = '#cdk-accordion-child-1 .ui-g div:nth-child(9) .value'
tasks_list_details_task_attributes_btn = tasks_list_edit_task_attributes_btn


# DATA SELECTORS
logged_username = '.logged-user .name'
