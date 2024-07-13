Run Instructions 

Initial Requirements:-
VS code (IDE that supports python,javascript,html,css)
MySQL Database
Node.js 

Setup:-
#1 MySQL
  1) Setup the MySQL local instance with localhost:3306
  2) username : root and password: Sa121243
  3) Open the Query file "Setup_Db" in MySQL workbench and run it
  4) Refresh Databases and check if the database "stcokmanagmentsystem" was created

#2 VS Code
  1) Once MySQL is setup create a folder and place all the files env, WebApp_React and WebApp_FastAPI in that folder.
  2) Open that folder in an IDE workspace (eg: VS code).
  3) Open a terminal in the workspace and activate venv using
     > source env/bin/activate
  4) Open new terminal in directory WebApp_FastAPI
     > pip install -r requirements.txt
     > uvicorn ims_Webmain:app --reload
     * Click on the generated localhost link (open in browser)
     * Keep terminal running
  5) Open new terminal in directory ims-webapp in WebApp_React folder
     * if first command doesnt work try using "npm init" beforehand.
     > npm install
     > npm install axios
     * Recommended STEP-5.2 instead of STEP-5.1
# Either run STEP 5.1 or 5.2
5.1) TO RUN APP test source
     * in same terminal as STEP-5
     > npm start
     * Click link for port 3000 and open in browser 
5.2) TO RUN BUILD
     * Same terminal as STEP-5
     > npm install -g serve
     > serve -s build
     * Click link for port 3000 and open in browser

CAUTION:
1) Make sure API is running (STEP4) while the React app is running (STEP 5.1/5.2)
   in seperate terminals.
2) Make sure SQL server is started and running
     


