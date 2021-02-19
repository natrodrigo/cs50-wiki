# CS50w Project 1: Wiki

This project is the "project1 - Wiki" from **CS50w**.
**CS50w** is a free course from Harvard University.

>"*Topics include database design, scalability, security, and user experience. Through hands-on projects, students learn to write and use APIs, create interactive UIs, and leverage cloud services like GitHub and Heroku. By semester’s end, students emerge with knowledge and experience in principles, languages, and tools that empower them to design and deploy applications on the Internet.*"
>Part of the course description on the home page;
>avaliable on: https://cs50.harvard.edu/web/2020/

All course specifications for this project  are avaliable on: <https://cs50.harvard.edu/web/2020/projects/1/wiki/>

#### Understanding

Wiki is a web application like Wikipedia, with entry pages that have some content. It have so many functions, but my objective here is not to explain how all functions works. The file called "**views.py**" contains all explanations about the program functions.
(This file is in wiki/encyclopedia directory).

This project uses **Django** framework with **Python** to create routes and render **HTML** content in a dinamic form.
Following Django documentation, after create a new project and a new app, CS50w teachers deleveries to us an app with a "husk" of the project, leaving us to implement the functions, create routes, HTML templates and etc.

#### Entry page

This project allows user to acess all pages of encyclopedia typing on navegation bar .../wiki/TITLE, where TITLE is the title of an encyclopedia entry. if this entry does not exists, user is invited to create this encyclopedia entry by cliking on "Create new page" on the left page's menu.

#### Index page

In homepage, the user can see a list with links for all avaliable entries.

#### Left menu
On the left menu, the user have a "search" bar that allows him to enter a term to search all titles which match the one entered.
Has also links to homepage, to create a new page, and to be redirected to a random page.

#### New and Edit page
By cliking in "create a new page", the user is presented to a page that contains two blank forms: to enter entry title and to enter text.
The text need to be written in markdown format. All pages are stored in the .md file format, which is converted to HTML via Python before being displayed on the screen.

A markdown guide is avaliable in Github Docs: <https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax>

All content pages can also be **edited** by clicking on the **link** indicated at the end of the content.

#### Demonstration Video

Finally, I leave here a video demonstration of the use of the application. Thank you for accessing and reading this content.

<https://youtu.be/0QJ9fmBvjnk>
