
## TEST SCENARIO CONTENT


### 1. Login user  

**Scope**: Test valid and invalid login attempts to the Authorization page.  
**Action**: User submits Login form.  
**Test Notes and Preconditions**: Open the login page.  
**Verification Steps**: Verify the user has been entered in to the admin page after given the correct details  

| #                   | Action           | Test case procedure | Expected result |
| ------------- | ------------- |  ------------- |  ------------- | 
| 1.1 | User enters only login  | 1. Enter login | *Confirm* button should be disabled. |
| 1.2 | User enters only password | 1. Enter password | *Confirm* button should be disabled. |
| 1.3 | User enters inproper values | 1. Enter login="asd"<br />  2. Enter password="asd"<br /> 3. Click *Confirm* | A red toast message should appear. |
| 1.4 | User enters proper values | 1. Enter login="admin"<br />  2. Enter password="Admin"<br /> 3. Click *Confirm* | A green toast message should appear and user should be logged in. Url should be on modules. |
| 1.5 | User clicks *Barcode* and *Confirm* after entering invalid credentials | 1. Press *Barcode* <br /> 2. Enter any invalid credentials <br /> 3. Press *Confirm* | User should remain on the authorization page not be logged in and toast message should appear. |
| 1.6 | User clicks *Barcode* and *Confirm* after entering valid credentials | 1. Press *Barcode* <br /> 2. Enter valid credentials: "AdminBC" <br /> 3. Press *Confirm* | User should be logged in and toast message should appear. |
| 1.7 | User clicks *Barcode* and *Confirm*  after entering very long hence invalid credentials | 1. Press *Barcode* <br /> 2. Enter very long *Barcode* <br /> 3. Click *Confirm* button | User should remain on the authorization page not be logged in and toast message should appear.|
| 1.8 | User clicks *Confirm* after entering very long hence invalid credentials | 1. Enter very long *Username* <br /> 2. Enter very long *Password* <br /> 3. Click *Confirm* button | User should remain on the authorization page, not be logged in and toast message should appear.|
| <img width=100/> | <img width=200/> |  <img width=500/> |  <img width=200/> |


### 2. Logout user  

**Scope**: Test logout user after successful login.  
**Action**: User logs out.  
**Test Notes and Preconditions**: Perform test after login.  
**Verification Steps**: Verify the user has been successfully logout after clicking on the action in menu.  

| #                   | Action           | Test case procedure | Expected result |
| ------------- | ------------- |  ------------- |  ------------- | 
| 2.1 | User clicks log out  | 1. Open user menu <br /> 2. Press *Logout* | User should be logged out, toast message should appear and user should be redirected to authorization page. |
| 2.2 | User clicks back after logout | 1. Open user menu <br /> 2. Press *Logout* <br /> 3. Press *Back* button | User should remain on the authorization page. |
| 2.3 | User logs in after logout | 1. Open user menu <br /> 2. Press *Logout* <br /> 3. Log in | User should be able to log in. |
| <img width=100/> | <img width=200/> |  <img width=500/> |  <img width=200/> |


### 3. Change user  

**Scope**: Change user after successful login.  
**Action**: Change user (logout the old one and log in a new one).  
**Test Notes and Preconditions**: Perform test after login.  
**Verification Steps**: Verify the user has been successfully changed after clicking on the action in menu.  

| #                   | Action           | Test case procedure   | Expected result |
| ------------- | ------------- |  ------------- |  ------------- | 
| 3.1 | User clicks *Change user*| 1. Open user menu  <br/> 2. Press *Change user*| A login window should appear. |
| 3.2 | User clicks *Change user*and *Cancel* | 1. Open user menu  <br /> 2. Press *Change user*  <br /> 3. Press *Cancel* | User should not be logged out, user should remain on the same page and name and surname should remain (top right corner). |
| 3.3 | User clicks *Change user*and *Confirm* after entering credentials | 1. Open user menu  <br /> 2. Press *Change user*  <br /> 3. Enter "operBC" barcode  <br /> 4. *Confirm* | User be logged out and the new user should be logged in, the toast message should appear and user name and surname should change. |
| 3.4 | User clicks *Change user*and *Confirm* after entering credentials | 1. Open user menu  <br /> 2. Press *Change user*  <br /> 3. Enter "operBC" barcode  <br /> 4. *Confirm*  <br /> 5. Press back button | The new user should remain logged in. |
| <img width=100/> | <img width=200/> |  <img width=500/> |  <img width=200/> |


### 4. Change language  

**Scope**: Change language in user menu.  
**Action**: Change language for user.  
**Test Notes and Preconditions**: Perform test after login.  
**Verification Steps**: Verify the language has been successfully changed after clicking on the action in menu.  

| #                   | Action           | Test case procedure | Expected result |
| ------------- | ------------- |  ------------- |  ------------- | 
| 4.1 | User clicks *Change application language* | 1. Open user menu <br /> 2. Press *Change application language* | The change language window should appear. |
| 4.2 | User clicks *Change application language* and *Cancel* | 1. Open user menu <br /> 2. Press *Change application language* <br /> 3. Press *Cancel* | Language should not be changed. |
| 4.3 | User clicks *Change application language* and *Confirm* after chosing the same one | 1. Open user menu <br /> 2. Press *Change application language* <br /> 3. Choose the same language <br /> 4. *Confirm* | Application language should not change. |
| 4.4 | User clicks *Change application language* and *Confirm* after chosing new language | 1. Open user menu <br /> 2. Press *Change application language* <br /> 3. Choose the an other language <br /> 4. *Confirm* | Application language should change. |
| 4.5 | After change of one user language a language of the other user should remain | 1. Check language of first user <br /> 2. *Change user* <br /> 3. *Change application language* <br /> 4. *Change user* back  | Language of the first user should remain unchanged. |
| <img width=100/> | <img width=200/> |  <img width=500/> |  <img width=200/> |

### 5. Items  

**Scope**: Items configuration.  
**Action**: CRUD of items in configuration.  
**Test Notes and Preconditions**: Perform test after login as admin.  
**Verification Steps**: Verify the CRUD operations on items.  

| #                   | Action           | Test case procedure | Expected result |
| ------------- | ------------- |  ------------- |  ------------- | 
| 5.1 | Items configuration view should appear | 1. Open application menu <br /> 2. Go to *Configuration* -> *Application configuration* -> *Items* | Items list on item configuration should appear. |
| 5.2 | Check default buttons state on items configuration | 1. Go to *Configuration* -> *Application configuration* -> *Items* | Add button should be enabled, delete and edit buttons should be disabled. |
| 5.3 | Check buttons state after selecting an item on items configuration | 1. Go to *Configuration* -> *Application configuration* -> *Items* <br /> 2. Select an item | Delete, Edit and Add buttons should be enabled. |
| 5.4 | Add item | 1. Go to *Configuration* -> *Application configuration*  -> *Items*  <br /> 2. Add item | Added item should appear on the list. |
| 5.5 | Edit item | 1. Add item <br /> 2. Edit it's name | Edited item should appear on the list. Check if the change is visible. |
| 5.6 | Remove item | 1. Add item <br /> 2. Remove it | Item should not be on the list |
| 5.7 | Try to Add item with not all required fields filled | 1. Open Add item window <br /> 2. Check if Save button is disabled <br /> 3. Try to fill data in several combinations and check if button behave correctly | Save button should behave correctly. |
| 5.8 | Check maximum allowed number of characters for ZFIN and Name fields | 1. Add item with long name and long ZFIN | Item should be on the list. |
| 5.9 | Check ZFIN and Name fields filled with over maximum allowed number of characters  | 1. Add item with longer name and ZFIN than maximum allowed number of characters | Save button should behave correctly. |
| 5.10 | User fills all required fields of *Add item* and clicks *Cancel* | 1. Fill all fields of *Add item* correctly <br /> 2. Click *Cancel* | Item should not appear on the list. |
| 5.11 | Abort *Delete item* | 1. Select item from list <br /> 2. Click *Delete* <br /> 3. Click *No* when dialog appear | Item should remain on the list. |
| <img width=100/> | <img width=200/> |  <img width=500/> |  <img width=200/> |



### 6. Process control configuration

**Scope**: Process control configuration.  
**Action**: CRUD of different components of Process control configuration.  
**Test Notes and Preconditions**: Perform test after login as admin.  
**Verification Steps**: Verify the CRUD operations on components of Process control configuration.   

| #                   | Action           | Test case procedure | Expected result |
| ------------- | ------------- |  ------------- |  ------------- | 
| 6.1 | Add parameter | 1. Open *Parameters* list <br /> 2. Press *Add* <br /> 3. Fill required *Parameter name* field <br /> 4. Click *Save* | Parameter should be on the list. |
| 6.2 | Delete parameter | 1. Open *Parameters* list <br /> 2. Select parameter from the list <br /> 3. Delete selected parameter  | Parameter should not be on the list. |
| 6.3 | Duplicate parameter | 1. Open *Parameters* list <br /> 2. Select parameter from the list <br /> 3. Duplicate selected parameter  | *Add parameter* window should appear with filled *Parameter name* |
| 6.4 | Check additional fields appearance for *Parameter type: List* selection | 1. Open *Parameters* list <br /> 2. Press *Add* <br /> 3. Select *Parameter type: List* | List view should appear |
| 6.5 | Check *List elemnts* assigment after adding *List element* | 1. Open *Parameters* list <br /> 2. Press *Add* <br /> 3. Select *Parameter type: List* <br /> 4. Click *Add* | Created element should be assigned to *List elements* |
| 6.6 | Check additional fields appearance for  *Parameter type: Integer value/Float value* selection | 1. Open *Parameters* list <br /> 2. Press *Add* <br /> 3. Select *Parameter type:  Integer value/Float value* | Additional fields should appear |
| 6.7 | Check additional fields appearance for both *Comment* options checked | 1. Open *Parameters* list <br /> 2. Press *Add* <br /> 3. Check both *Comment* options | Two additional fields should appear |
| 6.8 | Check *Parameter required* matching | 1. Open *Parameters* list <br /> 2. Press *Add* <br /> 3. Check *Parameter required* option | *Parameter required* on the list should show *Yes* |
| 6.9 | Check assigment of *Parameter* to *Controls Action* and *Controls Action* to *Controls* | 1. Add *Parameter* <br /> 2. Go to *Controls Action* <br /> 3. Add *Control Action* with *Parameter* assigned <br /> 4. Go to *Controls* <br /> 5. Add *Control* with *Control Action* assigned | Flawlessly perform all assignments and check added position appearance on lists |
| <img width=100/> | <img width=200/> |  <img width=500/> |  <img width=200/> |


### 7. Tasks list

**Scope**: Tasks list functionality.  
**Action**: CRUD of different tasks of Tasks list.  
**Test Notes and Preconditions**: Perform test after login as admin.  
**Verification Steps**: Verify the CRUD operations on tasks of Tasks list.   

| #                   | Action           | Test case procedure | Expected result |
| ------------- | ------------- |  ------------- |  ------------- | 
| 7.1 | Change status | 1. Open *Tasks list*<br /> 2. Check *Change status* button status<br /> 3. Select *Task* form list <br /> 4. Change its status <br /> 5. Check if status has changed <br /> | Status of the task changed
| 7.2 | Edit tasks *Task name* | 1. Select *task*  <br /> 2. Click *Edit* button <br /> 3.  Change *Task name* <br /> | Task should appear on the list with changed name |
| 7.3 | Edit tasks *Required quantity* | 1. Select *task* <br /> 2. Click *Edit* button <br /> 3.  Change tasks *Required quantity* | Task should appear on the list with changed *Required quantitiy* |
| 7.4 | Edit tasks *Priority*| 1. Select *task* <br /> 2. Click *Edit* button <br /> 3.  Change tasks *Priority* to invalide integer value | Error message should appear under *Priority* field and *Save* button should be disabled |
| 7.5 | Checks input of *Priority* and *Required quanitity* | 1. Select *task* <br /> 2. Click *Edit* button <br /> 3.  Change tasks *Priority* and *Required quantity* to string (letters) | Both fields should remain empty and *Save* button should be disabled |
| 7.6 | Edit tasks  *Task description*| 1. Select *task* <br /> 2. Click *Edit* button <br /> 3.  Type long string into *Task description* field <br /> 4. Click *Save* button <br /> 5. Open tasks *Details* | *Task description* should appear in tasks *Details* window |
| 7.7 | Edit tasks  *Attributes*| 1. Select *task* <br /> 2. Click *Edit* button <br /> 3. Click *Attributes* tab <br /> 4. Edit attribute <br /> 5. Click *Save* button <br /> 6. Open tasks *Details* <br /> 7. Open *Attributes* tab | *Attribiute value* should be changed |
| <img width=100/> | <img width=200/> |  <img width=500/> |  <img width=200/> |


## TOUR

**Scope**: User's tour for *Proccess control*
**Action**: Shows user step by step examplary *Proccess control* functionality

| #                   | Action           | 
| ------------- | ------------- | 
| 1 | User logs in |
| 2 | User adds new parameter in *parameters configuration* |
| 3 | User adds new control action in *control actions configuration* with created *parameter* assigned |
| 4 | User adds new control  in *controls configuration* with created *control action* assigned |
| <img width=100/> | <img width=500/> | 