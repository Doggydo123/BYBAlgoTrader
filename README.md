# BYBAlgoTrader
**GENERAL NOTES**
-Make pull requests to the develop branch not main.


**Prerequisites**:

Install Following:
Git, https://git-scm.com/downloads , this also comes with a UI and a command line interface,


Visual Studio Code https://code.visualstudio.com/Download ,
Python3 https://www.python.org/downloads/,
Then in VSCode go to the extensions and type in python, you'll want the top ones like "Python" and "Python Debugger".

Docker for containerising
https://docs.docker.com/desktop/install/windows-install/

**Step 1:**

    In a powershell terminal navigate to the directory you want this installed in (I usually create a folder called Git in my C: root folder).
    
    Then pull the repo which should be "git clone https://github.com/Doggydo123/BYBAlgoTrader.git" 
    
    There should be a new folder nowcalled BYBAlgoTrader, cd into it (cd BYBAlgoTrader)
    
    And in VSCODE, go File -> Open Folder, and open the BYBAlgoTrader

    You should now also have pip installed, this allows you to install programs from the command line, we will need flask for the server, so in your terminal try the following 
    pip install flask
    (you might need other imports like threading, e.g pip install threading)

    Remember to set your git username and email, maybe password too. 
    git config --global user.name "Your Username"
    git config --global user.email "your_email@example.com"
    git config --global user.password "password"
![image](https://github.com/Doggydo123/BYBAlgoTrader/assets/87892093/0279e3fc-efd6-4598-be3d-692ed2a22550)


**Step 2:**
    Try running the main.py file in VSC, this should start the automated jobs, and the webserver, which should look like this 
![image](https://github.com/Doggydo123/BYBAlgoTrader/assets/87892093/b68248bb-2023-41ef-ab7f-f9aa29af88bf)

For now editing will be simple, this is just the start, api calls are setup in App.py, and jobs are setup in Jobs.py
![image](https://github.com/Doggydo123/BYBAlgoTrader/assets/87892093/0559df29-0dcf-4c29-b058-bbf8ba9fd014)

