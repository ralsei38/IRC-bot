import socket as s
from time import sleep
from datetime import datetime

class IRC():
    def __init__(self, server, port) -> None:
        """
            regular socket connection made easy
        """
        self.socket = s.socket(s.AF_INET, s.SOCK_STREAM)
        self.socket.connect((server, port))
        print("socket receive:")
        print(self.recv())

    def _is_nickname_taken(self) -> bool:
        raise  NotImplementedError
    
    def authenticate(self, nickname) -> None:
        """
            following RFC1459 see 4.1.2 & 4.1.3 (4.1.1 being optional)
            actually using username as nickname & vice-versa
        """
        data = f"NICK {nickname} \r\n".encode("utf-8")
        self.socket.send(data)
        
        data = f"USER {nickname} 0 * :{nickname} \r\n".encode("utf-8")
        self.socket.send(data)
        print(self.recv())
        print(self.recv())
        print(self.recv())



    def list_users(self) -> None:
        print("LISTING USERS\n")
        data = f"NAMES \r\n".encode("utf-8")
        self.socket.send(data)
        print(self.recv())
        
    def join_channel(self, channel) -> None:
        if not channel.startswith('#'):
            channel = '#'+channel
        data = f"JOIN {channel} \r\n".encode("utf-8")
        self.socket.send(data)
        print(self.recv())
        print(self.recv())
        print(self.recv())

    def recv(self) -> str:
        answer = self.socket.recv(10**3)
        if not answer:
            raise Exception(f"No answer from {self.server}")
        else:
            return answer.decode("utf-8")

    def send_pm(self, receiver, msg) -> bool:
        """
            4.4.1 Private messages
        """
        data = f"PRIVMSG {receiver} :{msg} \r\n".encode("utf-8")
        self.socket.send(data)
        print(self.recv())
    
if __name__ == "__main__":
    server = "irc.root-me.org"
    port = 6667
    nickname= f"rals-{str(datetime.now()).split('.')[-1]}"[:9]
    channel=  "#root-me_challenge"

    print(nickname)
    print('*'*10)
    irc = IRC(server, port)
    print('*'*10)
    irc.authenticate(nickname)
    print('*'*10)
    irc.join_channel(channel)
    print('*'*10)
    irc.send_pm("nickname", "are you there ? thats a test btw")
    print('*'*10)
