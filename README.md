# Project Pizza
**P#0 by Team Fine Pizza**  

  **Roster:**  
  Benjamin Avrahami  -  Create all tables, facilitate adding new data to table, make sure data from tables are visible on website, other odds and ends  
  William Lin  -  Create python page to take in login information when account is created, enable users to log in, save session until browser window is closed  
  Tyler Huang  -  Make basic outline of project, connect to pages, ensure flexibility of connecting to new pages once created  
  David Wang  -  Create page for editing and creating new articles, display previous edit on page, make sure new story typed by user is saved and added to the appropriate table  


<br><br>
**HOW TO RUN THE PROJECT**
Before you run: Download flask
- from home directory
```
$ python3 -m venv [insert hero]     #creates virtual environment
$ . hero/bin/activate               #activates virtual environment
(hero)$ pip3 install Flask          #installs flask
(hero)$ deactivate                  #deactivates the virtual environment (do after you finish testing)
```

Running the project:
1. Clone the repository
```
git clone [insert HTTPS url to repo]
```
2. Run the main python program (app.py)
```
python3 app.py
```
3. Copy and paste the local url into your browser
      - the landing page should load with the options to log in or register
4. Register for an account
5. Log in with your newly made account!
      - the home page with the list of stories should load
      - there should be options to log out, add story, or edit story
          - otherwise, click on any of the story names (which should be links) to read
6. To add:
      - You will be redirected to a page that prompts you to write a title and
        the body of the text
      - Click the add button to finalize your story
   To edit:
      - You will be prompted to choose which story to edit, which will then open
        a page with editable text that you can change
      - Click the change button to finalize your changes
   To read:
      - You will be redirected to a page that displays the story title and text
   To log out:
      - You will be returned to the landing page
