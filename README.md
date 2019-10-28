# Project Pizza
**P#0 by Team Fine Pizza**  

  **Roster:**  
  Benjamin Avrahami  -  Create all tables, facilitate adding new data to table, make sure data from tables are visible on website, other odds and ends  
  William Lin  -  Create python page to take in login information when account is created, enable users to log in, save session until browser window is closed  
  Tyler Huang  -  Make basic outline of project, connect to pages, ensure flexibility of connecting to new pages once created  
  David Wang  -  Create page for editing and creating new articles, display previous edit on page, make sure new story typed by user is saved and added to the appropriate table  


<br><br>
**HOW TO RUN THE PROJECT**
<br>Before you run: Download flask
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
git clone [insert HTTPS url of repo]
```
2. Run the main python program (app.py)
```
python3 app.py
```
3. Copy and paste the local url into your browser
      - The landing page should load with the options to log in or register
4. Register for an account
5. Log in with your newly made account!
      - The home page with the list of stories should load
      - There should be options to log out, add story, or edit any
        existing stories that you have no contributed to before
          - otherwise, click on any of the story names (which should be links) to read
6. To add:
      - Click "create new story" and you will be redirected to a page that
        prompts you to write a title and the body of the story
      - Click the submit button to finalize your story
   To edit:
      - On the home page, you will be presented with a list of stories that
        you can edit. Clicking on any of the stories will redirect you to a
        page that shows the latest edits and gives you the option to add to
        the story. Click submit to finalize your additions.
   To read:
      - Click on any story and you will be redirected to a page that displays
        the story text
   To log out:
      - You will be returned to the landing page
