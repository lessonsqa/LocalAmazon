class VariablesClass:
    __username = "Lessons.qa@gmail.com"
    __password = "2357111317"
    defSearchText = "Roman old helmet"
    amazonSignInUrl = "https://www.amazon.com/gp/sign-in.html"

    @classmethod
    def get_username(cls):
        return cls.__username

    @classmethod
    def get_password(cls):
        return cls.__password
