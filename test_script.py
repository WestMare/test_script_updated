import Gitlab

access_token = 'Token'

print "Введите ваш токен")
gitlab_token = input()
print("Введите URL")
gitlab_url = input()


Gitlab(
        "https://{gitlab_url}/api/v4".format(gitlab_url=gitlab_url),
        private_token=github_token)
        

gl = gitlab.gitlab(url = gitlab_url, private_token = access_token)
users = gl.users.list(page = 1,per_page=1000)

for user in users:
    if (not(user.is_admin)
        try:
            block_user(user) continue 
print('Все пользователи без права администрирования заблокированы')
