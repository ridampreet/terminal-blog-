
from menu import Menu
from database import Database
from models.blog import Blog
from models.posts import Post

Database.initialize()
menu=Menu()
menu.run_menu()
