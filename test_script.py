import gitlab

print ("Введите ваш токен")
gitlab_token = input()
print("Введите URL")
gitlab_url = input()
  
gl = gitlab.gitlab(url = gitlab_url, private_token = gitlab_token)
users = gl.users.list(page = 1,per_page=1000)

for user in users:
    if (not(user.is_admin)):
        try:
            user.block()
            print('Пользователь ' + user.username + ' заблокирован')
            continue
        except:
            print('Не удалось заблокировать пользователя '+ user.username)
                
print('Все пользователи без права администрирования заблокированы')
