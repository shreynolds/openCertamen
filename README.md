# openCertamen
This program creates teams for Open Certamen at JCL conventions. The goal is for people from the same school to not be on the same team.

The program then assigns the teams to rooms for three rounds, if there is a template available for the number of teams.

# Instructions
1. Clone the current repository to your computer. Make sure you have [python3](https://www.python.org/downloads/) and [PANDAS](https://pandas.pydata.org/pandas-docs/version/0.24/install.html) downloaded
2. Create a Google Form that asks stuents for their full name, school (use multiple choice), and level (use multiple choice). Put the link to this form in your program so that students can fill it out to sign up for Open Certamen.
3. Once the sign up period has finished, prevent the form from accepting further responses. Then, download the data as a csv file. Rename the file responses.csv and rename the columns 'Name', 'Level', and 'School'.
4. Move the csv file to be in the same folder as the python file.
5. Open the python code and change the list 'totalrooms' to contain the room names you are using, if desired. If you want to specify rooms for beginner, intermediate, and advanced, do beginner rooms first, then intermediate, then advanced.
6. In terminal, go to the directory that the code is in, and run 
`python3 certamen.py` 
7. You will have html outputs for each of the levels.

# Notes
* If the code seems stuck or is not running, cancel and try again -- often that will help.
* While the output is in HTML, if you want to be able to edit it, you can convert it to a word doc either through copy and paste or through an online converter.
  * If you put it into a word doc, the spacing may be a bit off. Try changing font size, switching to landscape orientation, changing table layout, etc to be able to see it correctly
* If the number of teams does not have a specific template, you will not get rooms assigned.

# Notes for Magis
When it says 'go to the directory that the code is in', open terminal and type
cd Desktop (enter)
cd openCertamen (enter)
and then you are in the directory

If you want to update the code, go to the directory and type `git pull` and it will be updated if the code has been updated.
