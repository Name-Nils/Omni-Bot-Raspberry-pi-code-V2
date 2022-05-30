from simple_websocket_server import WebSocketServer, WebSocket
from threading import Thread

send_queue = []
max_data_per_send = 2
receive_data = []

class Comm(WebSocket):
    def handle(self):
        global receive_data, send_queue

        if (self.data != " "):
            receive_data.append(self.data)
        
        for i in range(len(send_queue)):
            if i > max_data_per_send: break
            self.send_message(send_queue.pop())


def run():
    server = WebSocketServer("192.168.8.117", 8080, Comm)
    server.serve_forever()


ws_run = Thread(target=run)
ws_run.start()