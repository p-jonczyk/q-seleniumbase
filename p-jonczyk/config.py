# URL SETTINGS

# Different testing enviroments
# url = "http://192.168.1.157:8211"
url = "http://192.168.1.157:8311"
# main env
# url = "http://192.168.1.157:8711"
url_authorization = url+"/authorization"
url_models = url + "/models"
# Items
url_items = url+"/configuration/web-application-configuration/items/configure"
# Process control
url_process_control = url + "/configuration/modules-configuration/process-control"
url_process_control_parameters = url_process_control + "/parameters"
url_process_control_control_actions = url_process_control + "/control-actions"
url_process_control_controls = url_process_control + "/controls"
# Tasks list
url_tasks_list = url + "/production/tasks"

# USERS SETTINGS

valid_username = "admin"
valid_password = "Admin"
valid_user_barcode = "operBC"
valid_admin_barcode = "AdminBC"
invalid_username = "asdf"
invalid_password = "zxcv"
invalid_barcode = "invalideoperBC"

# FUNCTIONS SETTINGS

# Used when calling basic_methods: type_generated_string
test_string_len = 500

# Item settings
item_id = "Item_TESTQwer1234"
item_name = "Item_TEST ITEM NAME 12P 34/ 8R 123X RO_"
item_group = "Braki"
item_unit = "Gram"
item_new_name = "Item_new name 1233"
items_max_string_len = 200
items_over_max_string_len = items_max_string_len + 1

# Parameters
parameter_name = "Parameter_TEST2312dsad"
parameter_config_list_elem = "Parameter_Test list elem"

# Control actions
control_action_name = "ControlAction_ControTEST132"

# Controls
control_name = "Control_NameOfControls1234"

# Tasks lsit

task_name_new = "TasksList_NewTaskName3214"
task_required_quantity = "250"
task_required_quantity_invalide = "TasksListQuantityInvalide_dsawq"
task_priority_invalide = "TasksListPriorityInvalide_dsadas"
# already existing attribute
task_attribute_name = "Test"
task_attribute_value = "TasksListAttributeValu_TEST"
