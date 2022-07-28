import socket as s

class IRC():
    def __init__(self, server, port) -> None:
        """
            regular socket connection made easy
        """
        self.socket = s.socket(s.AF_INET, s.SOCK_STREAM)
        self.socket.connect((server, port))
    
    def _is_nickname_taken(self) -> bool:
        raise  NotImplementedError
    
    def authenticate(self, nickname, username) -> bool:
        """
            following RFC1459 see 4.1.2 & 4.1.3 (4.1.1 being optional)
        """
        
        data = f"NICK ralsei"
        pass

    def join_channel(self) -> bool:
        pass

    def talk(self, username) -> bool:
        pass
    
    def _receive(self) -> str:
        pass
    

if __name__ == "__main__":
    server = "irc.root-me.org"
    port = 6667
    irc = IRC(server, port)