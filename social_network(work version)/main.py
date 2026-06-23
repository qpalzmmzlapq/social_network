import User

maxiUser = User.User(username="maxim", email="myemail@gmail.com")

smbdUser = User.User(username="somebody", email="somebodyemail@gmail.com")

# выше пример создания пользователей

maxiUser.SendFriendRequest(smbdUser)

# выше запрос в друзья от maxiUser к smbdUser с одобрением или нет запроса от smbdUser

maxiUser.upload_post("Контент для загрузки в соц сеть")

# выше публикация поста от maxiUser

smbdUser.like_post(maxiUser)

# выше smbdUser ставит лайк одному из постов maxiUser(на выбор)

smbdUser.comment_post(maxiUser)

# выше smbdUser оставляет коментарий одному из постов maxiUser(на выбор)

maxiUser.GetInfo()

# выше получение всех данных о пользователе(имя, почта, друзья, посты и данные постов(лайки и коментарии))
