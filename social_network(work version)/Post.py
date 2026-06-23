class Post:

    def __init__(self, content, author):
        self.__post_id = 0
        self.__content = content
        self.__author = author
        self.__likes = []
        self.__coments = []

    @property
    def content(self):
        return self.__content

    @property
    def post_id(self):
        return self.__post_id

    @property
    def author(self):
        return self.__author

    @property
    def comments(self):
        return self.__coments

    @property
    def comments_author(self):
        return self.__comments_author

    @property
    def likes(self):
        return self.__likes

    @comments.setter
    def __comments(self, new_comment):
        self.__coments = new_comment

    @comments_author.setter
    def __comments_author(self, new_comment_author):
        self.__coments = new_comment_author

    @likes.setter
    def likes(self, new_like):
        self.__likes.append(new_like)

    @post_id.setter
    def post_id(self, increment_post_id):
        self.__post_id = increment_post_id

    def add_comment(self, user, text):
        new_user_comenting = Comment_User(user, text)
        self.comments.append(new_user_comenting)


class Comment_User:
    def __init__(self, uc, tu):
        self.user_commented = uc
        self.text_user = tu
