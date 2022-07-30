import socket as s
from time import sleep
from datetime import datetime
import select


class IRC():
    def __init__(self, server, port) -> None:
        """
            regular socket connection made easy
        """
        self.socket = s.socket(s.AF_INET, s.SOCK_STREAM)
        self.socket.connect((server, port))

    def _is_nickname_taken(self) -> bool:
        raise  NotImplementedError
    
    def authenticate(self, nickname) -> str:
        """
            following RFC1459 see 4.1.2 & 4.1.3 (4.1.1 being optional)
            actually using username as nickname & vice-versa
        """
        print(f"authenticating as {nickname}")
        data = f"NICK {nickname} \r\n".encode("utf-8")
        self.socket.send(data)
        
        data = f"USER {nickname} 0 * :{nickname} \r\n".encode("utf-8")
        self.socket.send(data)
        return self.recv()

    def list_users(self) -> str:
        data = f"NAMES \r\n".encode("utf-8")
        self.socket.send(data)
        return self.recv()

    def join_channel(self, channel) -> str:
        print(f"joinning channel: {channel}")
        if not channel.startswith('#'):
            channel = '#'+channel
        data = f"JOIN {channel} \r\n".encode("utf-8")
        self.socket.send(data)
        return self.recv()

    def recv(self) -> str:
        full_answer = ""
        self.socket.settimeout(1.1)
        try:
            data = self.socket.recv(512).decode("utf-8")
            full_answer += data
            while True:
                data = self.socket.recv(100000).decode("utf-8")
                full_answer += data
        except:
            pass
        self.socket.settimeout(None)
        return full_answer

    def send_pm(self, receiver, msg) -> str:
        """
            4.4.1 Private messages
        """
        print(f"sending private message to {receiver}")
        data = f"PRIVMSG {receiver} :{msg} \r\n".encode("utf-8")
        self.socket.send(data)
        return self.recv()