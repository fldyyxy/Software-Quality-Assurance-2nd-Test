Background:
GIThub is an online hosting service for Git-based version control. It is commonly employed for storing code revisions in a single repository.
GIThub provides additional features, one of which is Gists. 
Gists are primarily utilized for documentation purposes to share code fragments, notes, files, directories, and entire applications.
Go to https://gist.github.com/, login and click on New Gist to create a new gist. Gists can have different extensions such as .js, .md, .txt, etc.

Here is a test scenario that I made based on some of the test cases below:
   Test case 1:  As a user, I want to create a public gist.
   Test case 2:  As a user, I want to edit an existing gist.
   Test case 3:  As a user, I want to delete an existing gist.
------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
Test Scenario 1: User create a public gist

Test case ID: CR01
Test description: Create a public gist with account registered on Github
Type: Positive
Pre-requisite: Github account 
Test step: 1. Navigate to https://gist.github.com/
           2. Sign in to Github
           3. Type an optional description and name for your gist
           4. Type text of your gist content into the gist text box
           5. Select "Create public gist" option then click "Create public gist"
             
Data input: 1. Gist description = Create public gist
            2. Filename including extension = Publicgist1
            3. Gist text box = This is create public gist test case
              
Expected result: 1. Redirect directly to Gist Github homepage
                 2. Redirect directly to login page
                 3. User can create Gists with different extensions such as .js, .md, .txt, etc
                 4. "Create public gist" button will active after user has entered all field
                 5. Gist that have been created will appear in Gist Github discover
Actual result: 
Test date: 
Tester:
Status:
------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
Test Scenario 1: User create a public gist

Test case ID: CR02
Test description: Create a public gist without account registered on Github
Type: Negative
Pre-requisite:  
Test step: 1. Navigate to https://gist.github.com/
             
Data input: -
              
Expected result: 1. Redirect directly to Gist Github homepage
                 2. Feature create gist not appear
                 3. User can not create a public gist
Actual result: 
Test date: 
Tester:
Status:
------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
Test Scenario 1: User create a public gist

Test case ID: CR03
Test description: Create a public gist without fill in content in the gist text box 
Type: Negative
Pre-requisite: Github account 
Test step: 1. Navigate to https://gist.github.com/
           2. Sign in to Github
           3. Type an optional description and name for your gist
           4. Let the gist text box empty
           5. Select "Create public gist" option then click "Create public gist"
             
Data input: 1. Gist description = Create public gist
            2. Filename including extension = Publicgist3
              
Expected result: 1. Redirect directly to Gist Github homepage
                 2. Redirect directly to login page
                 3. User can not create a gist public
                 4. Appear error message "Contents can't be empty"
Actual result: 
Test date: 
Tester:
Status:
------------------------------------------------------------------------------------------------------------------------------------------------------------------  
Test scenario 2: User edit an existing gist
 
Test case ID: ED01
Test description: Edit content of an existing gist
Type: Positive
Pre-requisites: 1. Github account
                2. Gist file
                
Test step: 1. Navigate to https://gist.github.com/
           2. Sign in to Github
           3. Navigate to "view your gist" and select gist named "Publicgist1" 
           4. Click "Edit" button
           5. Change values of gist content, description, or name
           6. Click "Update gist public" button

Data input: 1. Gist text box that will be change = This is edit public gist test case

Expected result: 1. Redirect directly to Gist Github homepage
                 2. Redirect directly to login page
                 3. Redirect directly to your gist that was edit
                 4. User can edit gists with different extensions such as .js, .md, .txt, etc
                 5. Gist existing file that was edit will appear on Gist Github Discover
                 6. Everyone who accesses https://gist.github.com/ can see your edited file
Actual result: 
Test date: 
Tester:
Status:
------------------------------------------------------------------------------------------------------------------------------------------------------------------  
Test scenario 2: User edit an existing gist

Test case ID: ED02
Test description: Cancel edit content of an existing gist
Type: Negative
Pre-requisites: 1. Github account
                2. Gist file
                
Test step: 1. Navigate to https://gist.github.com/
           2. Sign in to Github
           3. Navigate to "view your gist" and select gist named "Publicgist1" 
           4. Click "Edit" button
           5. Change values of gist content, description, or name
           6. Click "cancel" button

Data input: 1. Filename including extension that will change = Publicgist2

Expected result: 1. Redirect directly to Gist Github homepage
                 2. Redirect directly to login page
                 3. Redirect directly to your gist that was cancel edit
                 4. User can edit gists with different extensions such as .js, .md, .txt, etc
                 5. Gist existing file that was edit will not appear on Gist Github Discover
                 6. Everyone who accesses https://gist.github.com/ cannot see your edited file
Actual result: 
Test date: 
Tester:
Status:
------------------------------------------------------------------------------------------------------------------------------------------------------------------  
Test scenario 2: User edit an existing gist

Test case ID: ED03
Test description: Edit content of an existing gist but do not change existing values
Type: Negative
Pre-requisites: 1. Github account
                2. Gist file
                
Test step: 1. Navigate to https://gist.github.com/
           2. Sign in to Github
           3. Navigate to "view your gist" and select gist named "Publicgist1" 
           4. Click "Edit" button
           5. Change values of gist content, description, or name
           6. Click "Update public gist" button

Data input: -

Expected result: 1. Redirect directly to Gist Github homepage
                 2. Redirect directly to login page
                 3. Redirect Directly to your gist that was edit
                 4. User can edit gists with different extensions such as .js, .md, .txt, etc
                 5. Gist existing file that was edit will appear on Gist Github Discover and the values still same as before edited 
                 6. Everyone who accesses https://gist.github.com/ will not see any change of your gist
Actual result: 
Test date: 
Tester:
Status:
------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
Test scenario 3: User delete an existing gist
 
Test case ID: DE01
Test description: Delete an existing gist
Type: Positive
Pre-requisites: 1. Github account
                2. Gist file
                
Test step: 1. Navigate to https://gist.github.com/
           2. Sign in to Github
           3. Navigate to "view your gist" and select gist named "Publicgist1" 
           4. Click "Delete" button

Data input: -

Expected result: 1. Redirect directly to Gist Github homepage
                 2. Redirect directly to login page
                 3. Redirect directly to your gist list page
                 4. User can delete gists with different extensions such as .js, .md, .txt, etc
                 5. Appear notification "Gist deleted successfully"
                 6. Gist existing that was deleted does not appear on your gist list page
Actual result: 
Test date: 
Tester:
Status:
------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
Test scenario 3: User delete an existing gist
 
Test case ID: DE02
Test description: Cancel delete an existing gist
Type: Negative
Pre-requisites: 1. Github account
                2. Gist file
                
Test step: 1. Navigate to https://gist.github.com/
           2. Sign in to Github
           3. Navigate to "View your gist" and select gist named "Publicgist1" 
           4. Click "Delete" button
           5. Click the "Cancel" button on the gist.Github pop up notification

Data input: -

Expected result: 1. Redirect directly to Gist Github homepage
                 2. Redirect directly to login page   
                 3. Redirect directly to your gist list page
                 4. User can delete gists with different extensions such as .js, .md, .txt, etc
                 5. Appear notification "Gist deleted successfully"
                 6. Gist existing that was deleted does not appear on your gist list page
Actual result: 
Test date: 
Tester:
Status:
