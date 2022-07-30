## Data Engineering

Welcome to my data engineering project! 
My goal with this project is to apply and demonstrate my skills in Python.
I am specifically working with pandas and matplotlib.

The roadmap for this project includes plans to incorporate learning from
books such as the following:

- Automate the Boring Stuff with Python by Al Sweigart
- Clean Code by Robert C. Martin
- Grokking Algorithms by Aditya Y. Bhargava
- Beyond the Basic Stuff with Python by Al Sweigart
- Web Development with Django by Ben Shaw, Saurabh Badhwar, et. al
- Computer Science Distilled by Wladston Ferreira Filho
- Head First Design Patterns by Eric Freeman & Elisabeth Robson

as well as online resources such as:

- [Tim Buchalka's Udemy course, Python Programming Masterclass](https://www.udemy.com/course/python-the-complete-python-developer-course/)
- FreeCodeCamp's curriculum especially for HTML, CSS, & JavaScript
- W3school's SQL information
- Codecademy's Data Scientist:Machine Learning Specialist curriculum: https://www.codecademy.com/learn/paths/data-science

The app currently starts with humble origins featuring a command line interface to display different graphs to the user.
My goal is that over time, commit by commit, it will scale to a more dynamic project.
To run the program, clone this repository, download python 3.9 or later and check "add to path"
once python is in the environment path variable, open a terminal, cd into the repo and run 
"python -m pip install requirements.txt". 
Then run python plt_charts_and_graphs.py.

At the time of this writing there are 9 possible commands: 
  1. draw a line
  2. draw two points
  3. draw a line with more points
  4. draw 2 plots with title and super title
  5. draw 6 plots
  6. load the csv data
  7. draw a scatterplot
  8. draw a barchart using the LinkedIn search_data
  9. exit the program
  
Most of the graphs use harcoded data. Command 8 is different in that it uses data from a csv which I put together myself.
My goal was to search several keywords using LinkedIn's search feature and record the number of results for each one.
I searched over 80 terms that I have seen in job postings and recorded the number rounded to the nearest thousand
to determine which skills are most in demand in the technology job market. As the csv shows, the top 10 of the ones I searched
were:

1. cloud	533000
2. data analysis	372000
3. C	297000
4. SQL	260000
5. Python	257187
6. Java	224,000
7. AWS	222410
8. Javascript	165849
9. UX	158000
10. Linux	157000
