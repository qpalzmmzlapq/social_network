# хуесос
class User:
    """Пользователь социальной сети"""

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self._friends = (
            {}
        )  # {user: статус} статус: "друг", "заявка_отправлена", "заявка_получена"
        self._posts = []

    def send_friend_request(self, other_user):
        """Отправить заявку в друзья"""
        pass  # Проверки: нельзя добавить себя, повторно отправить

    def accept_friend_request(self, other_user):
        """Принять заявку"""
        pass  # Проверка: должна быть входящая заявка

    def unfriend(self, other_user):
        """Удалить из друзей"""
        pass

    @property
    def friends(self):
        """Список друзей"""
        pass

    @property
    def mutual_friends(self, other_user):
        """Общие друзья с другим пользователем"""
        pass

    def create_post(self, content):
        """Создать пост"""
        post = Post(self, content)
        self._posts.append(post)
        return post

    def like_post(self, post):
        """Лайкнуть пост"""
        pass

    def __str__(self):
        return f"@{self.username}"


class Post:
    """Пост пользователя"""

    _id_counter = 0

    def __init__(self, author, content):
        Post._id_counter += 1
        self.post_id = Post._id_counter
        self.author = author
        self.content = content
        self.likes = set()  # Кто лайкнул
        self.comments = []  # Список комментариев

    def add_comment(self, user, text):
        """Добавить комментарий"""
        pass

    def __str__(self):
        """Пост с лайками и комментариями"""
        pass


class SocialNetwork:
    """Сама социальная сеть"""

    def __init__(self, name):
        self.name = name
        self.users = {}  # {username: User}

    def register(self, username, email):
        """Зарегистрировать пользователя (username уникален)"""
        pass

    def find_user(self, username):
        """Найти пользователя по имени"""
        pass

    def suggest_friends(self, user):
        """
        Предложить друзей на основе:
        - Друзья друзей
        - Общие интересы (пока не реализовано)
        Возвращает список {user: количество_общих_друзей}, отсортированный по убыванию
        """
        pass

    def shortest_path(self, user1, user2):
        """
        Кратчайший путь между двумя пользователями через друзей
        (поиск в ширину)
        Возвращает список пользователей от user1 до user2
        """
        pass
