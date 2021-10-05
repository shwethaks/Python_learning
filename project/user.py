class User:
    def __init__(self, useremail, name, password, current_job_title):
        self.email = useremail
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password
    
    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print (f"User {self.name} currenlt workds as a {self.current_job_title}")


app_user_one = User("shwetha@gmail.com", "shwetha", "pwd", "Software engineer")
app_user_one.get_user_info()