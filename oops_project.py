class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.logged_in=False
        self.menu()


    def menu(self):
        user_input=input('''Welcome to chatbook !!How would you like to proceed ?
                         1.Press 1 to signup,
                         2.press 2 to signin,
                         3.press 3 to write a post,
                         4.Press 4 to message a friend,
                         5.Press any other key to exit

        ''')
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit()
    def signup(self):
        email=input("Enter your email \n")
        password=input("Enter a password \n")
        self.username=email
        self.password=password
        print("You have signed up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username =="" and self.password=="":
            print("please signup first by pressing 1 in the main menu \n")
            self.menu()
        else:
            uname=input("please enter your username \n")
            pwd=input ("please enter your password \n")
            if uname==self.username and pwd==self.password:
                print("you have signed in successfully")
                print("\n")
                self.menu()
                self.logged_in=True
            print("incorrect username or password entered")
            self.menu()

chat=chatbook()
       