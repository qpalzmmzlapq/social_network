import Post
import os


class User:

    def __init__(self, username, email):
        self.__friends = []
        self.__posts = []
        self.__username = username
        self.__email = email

    @property
    def username(self):
        return self.__username

    @property
    def email(self):
        return self.__email

    @property
    def friends(self):
        return self.__friends

    @property
    def posts(self):
        return self.__posts

    def __posts_add(self, new_posts):
        self.__posts.append(new_posts)

    def __friends_add(self, new_friends):
        self.__friends.append(new_friends)

    def upload_post(self, content):
        post = Post.Post(content=content, author=self)
        self.__posts_add(post)
        post.post_id += len(self.posts)

    def like_post(self, like_another_people):
        print(
            "\n"
            + "-------------------------------------------------"
            + "\n"
            + "Ты: "
            + self.username
            + "\n"
            + "лайкаешь: "
            + like_another_people.username
            + "\n"
            + "Выбери один из постов "
            + like_another_people.username
        )
        if len(like_another_people.posts) != 0:
            print("-------------------------------------------------")
            for i in range(0, len(like_another_people.posts)):
                print(
                    str(like_another_people.posts[i].post_id)
                    + "."
                    + str(like_another_people.posts[i].content)
                )
            print("-------------------------------------------------")

            id_like = (
                int(input("Выбери пост который хочешь лайкнуть и укажи его номер: "))
                - 1
            )
            if id_like <= len(like_another_people.posts) - 1:
                like_another_people.posts[id_like].likes = self
                print(
                    "Ты поставил лайк на пост: "
                    + like_another_people.posts[id_like].content
                )
            else:
                print("Поста под таким номером нету")
        else:
            print("у пользователя " + like_another_people.username + " нету постов")

    def comment_post(self, comment_another_people):
        print(
            "\n"
            + "-------------------------------------------------"
            + "\n"
            + "Ты: "
            + self.username
            + "\n"
            + "оставляешь коментарий пользователю: "
            + comment_another_people.username
            + "\n"
            + "Выбери один из постов "
            + comment_another_people.username
        )
        if len(comment_another_people.posts) != 0:
            print("-------------------------------------------------")
            for i in range(0, len(comment_another_people.posts)):
                print(
                    str(comment_another_people.posts[i].post_id)
                    + "."
                    + str(comment_another_people.posts[i].content)
                )
            print("------------------------------------------------")
            id_like = (
                int(
                    input(
                        "Выбери пост который хочешь прокоментировать и укажи его номер: "
                    )
                )
                - 1
            )
            if id_like <= len(comment_another_people.posts) - 1:
                comment = input("Твой комментарий: ")
                comment_another_people.posts[id_like].add_comment(self, comment)
            else:
                print("Поста под таким номером нету")
        else:
            print("у пользователя " + comment_another_people.username + " нету постов")

    def SendFriendRequest(self, newFriend):
        frineds_added = False
        for i in range(0, len(self.friends)):
            if self.friends[i] == newFriend.username:
                print("Такой друг уже существует")
                frineds_added = True

        if frineds_added != True:
            response = newFriend.AcceptFriendFrom(self)
            if response == True:
                self.__friends_add(newFriend.username)
                newFriend.__friends_add(self.username)

    def AcceptFriendFrom(self, newFriendRequest):
        print("Ты: " + self.username + "\n")
        accept = input(
            "Принять запрос в друзья от: "
            + newFriendRequest.username
            + "\n"
            + "Да/Нет"
            + "\n"
        )
        response = False
        if accept.lower() == "Да".lower():
            response = True
        return response

    def DeleteFriends(self, deleted_friend):
        print("Ты: " + self.username + "\n")
        exist_friend = False
        for i in range(0, len(self.friends)):
            if self.friends[i] == deleted_friend.username:
                exist_friend = True
        if exist_friend == True:
            if (
                input(
                    "удалить из друзей:  "
                    + deleted_friend.username
                    + "?"
                    + "\n"
                    + "Да/Нет"
                    + "\n"
                ).lower()
                == "Да".lower()
            ):
                for i in range(0, len(self.friends)):
                    if self.friends[i] == deleted_friend.username:
                        self.friends.remove(self.friends[i])
            else:
                print("Пользователь: " + deleted_friend.username + "не был удалён")

    def GetInfo(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(
            "-------------------------------------------------" + "\n"
            "You:"
            + self.username
            + "\n"
            + "your email: "
            + self.email
            + "\n"
            + "AllYourFriend: "
            + str(self.friends)
            + "\n"
            + "-------------------------------------------------"
        )
        for i in range(0, len(self.posts)):
            print(
                "Your Posts: "
                + "\n"
                + str(self.posts[i].post_id)
                + "."
                + self.posts[i].content
                + "\n"
                + "likes count: "
                + str(len(self.posts[i].likes))
                + "\n"
                + "comment count:"
                + str(len(self.posts[i].comments))
                + "\n"
                + "-------------------------------------------------"
            )
        if len(self.posts) != 0:
            choise = input("Показать коментарии?" + "\n" + "Да/Нет" + "\n")
            id_post = 0
            if choise.lower() == "Да".lower():
                id_post = (
                    int(
                        input("выбери пост, под которым хочешь посмотреть коментарии: ")
                    )
                    - 1
                )
                if (
                    id_post - 1 <= len(self.posts)
                    and len(self.posts[id_post].comments) >= 0
                ):
                    for i in range(0, len(self.posts[id_post].comments)):
                        print(
                            "Пользователь: "
                            + self.posts[id_post].comments[i].user_commented.username
                            + "\n"
                            + "его\eё коментарий:"
                            + "\n"
                            + self.posts[id_post].comments[i].text_user
                        )
                else:
                    if id_post - 1 > len(self.posts) - 1:
                        print("поста под таким номером нет")
                    else:
                        print(
                            "Коментариев под постом: "
                            + self.posts[id_post].content
                            + " не найдено"
                        )
