Background:
GIThub is an online hosting service for Git-based version control. It is commonly employed for storing code revisions in a single repository.
GIThub provides additional features, one of which is Gists. 
Gists are primarily utilized for documentation purposes to share code fragments, notes, files, directories, and entire applications.
Go to https://gist.github.com/, login and click on New Gist to create a new gist. Gists can have different extensions such as .js, .md, .txt, etc.

Here is a test scenario that I made based on some of the test cases below:
   Case 1:  As a user, I want to create a public gist.
   Case 2:  As a user, I want to edit an existing gist.
   Case 3:  As a user, I want to delete an existing gist.

Test scenario

Test Case 1
  Case: User create a public gist with Github account
  Test description: Create a public gist with account registered on Github
  Type: Positive
  Pre-requisite: Github account
  
  Test step: 1. Navigate to https://gist.github.com/
             2. Navigate to your gist homepage
             3. Type an optional description and name for your gist
             4. Type the text of your gist into the gist text box
             5. Select "Create public gist" option then click "Create public gist"
             
  Data input: 1. Gist description = Create public gist
              2. Filename including extension = Publicgist1
              3. Gist text box = This is create public gist test case
              
  Expected result: 1. "Create public gist" button will active after user has entered all field
                   2. Redirects Directly to Gist Github discover
                   3. User can create Gists with different extensions such as .js, .md, .txt, etc
                   4. User successfully create public gist
                   4. Gist that have been created will appear in Gist Github discover
                   
  Actual result: 
  Status: (Passed, Failed)
  
  Case: User create a public gist with Github account
  Test description: Create a public gist with account registered on Github
  Type: Positive
  Pre-requisite: Github account
  
  Test step: 1. Navigate to https://gist.github.com/
             2. Navigate to your gist homepage
             3. Type an optional description and name for your gist
             4. Type the text of your gist into the gist text box
             5. Select "Create public gist" option then click "Create public gist"
             
  Data input: 1. Gist description = Create public gist
              2. Filename including extension = Publicgist1
              3. Gist text box = This is create public gist test case
              
  Expected result: 1. "Create public gist" button will active after user has entered all field
                   2. Redirects Directly to Gist Github discover
                   3. User can create Gists with different extensions such as .js, .md, .txt, etc
                   4. User successfully create public gist
                   4. Gist that have been created will appear in Gist Github discover
                   
  Actual result: 
  Status: (Passed, Failed)
  
  
  
  
 Case 2: User edit an existing gist
  Test description: Edit an existing gist
  Pre-requisites: Github account
  Test step: 1. Navigate to https://gist.github.com/
             2. View gist an existing
             3. Click Edit button
             4. Change gist's description, extenction, or type input
             5. Click "Update gist public" button
  Expected result: User successfully edit an existing gist
  Actual result: As expected
  Status: Pass
  
 Case 3: User delete an existing gist
  Test description: Delete an existing gist
  Pre-requisites: Github account
  Test step: 1. 


