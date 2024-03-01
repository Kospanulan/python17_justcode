class User:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.posts = []

    def __repr__(self):
        return self.name

    def create_post(self,text):
        new_post = Post(text, self)
        self.posts.append(new_post)

    def registration(self, app):
        app.add_user(self)

    def change_name(self, new_name):
        self.name = new_name


class Post:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.comments = []
    def __repr__(self):
        return f"'{self.text}' @{self.author}."




class Comment:
    def __init__(self, text, author, post):
        self.text = text
        self.author = author
        self.post = post


class App:
    def __init__(self):
        self.users = []

    def add_user(self, new_user):
        self.users.append(new_user)

    def get_all_users(self):
        return self.users

    def get_all_posts(self):
        posts = []

        for user in self.users:
            posts.extend(user.posts)

        return posts

#
# instagram = App()
# baktiyar = User("Baktiyar", "Argyn")
# baktiyar.registration(instagram)
# baktiyar.create_post("Chtoto pishu")
# print(instagram.users)
# baktiyar.create_post("obratnno test")
# baktiyar.change_name("bakha")
# print(baktiyar.posts)
# print(instagram.users)
#

