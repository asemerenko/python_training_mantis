from telnetlib import Telnet


class JamesHelper:

    def __init__(self, app):
        self.app = app

    def ensure_user_exists(self, username, password):
        pass


    class Session:

        def __init__(self, host, port, username, password):
           self.telnet = Telnet(host, port, 5)
           self.telnet.read_until("Login id:", 5)
           self.telnet.write(username + "\n")
           self.telnet.read_until("Password:", 5)
           self.telnet.write(password + "\n")
           self.telnet.read_until("Welcome root. HELP for a list of commands", 5)

        def is_user_registered(self, username):
            pass


