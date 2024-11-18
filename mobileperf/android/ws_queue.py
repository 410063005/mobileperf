import queue

from flask_socketio import SocketIO

socketio = SocketIO(message_queue="redis://")


class WsQueue(queue.Queue):
    def __init__(self, tag, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = tag

    def put(self, item, block=True, timeout=None):
        super().put(item, block, timeout)

        if self.tag in [
            "cpu_queue",
            "mem_queue",
            "power_queue",
            "traffic_queue",
            "fps_queue",
            "fd_queue",
            "thread_queue",
            "activity_queue",
            "simple_queue",
        ] and isinstance(item, list):
            socketio.emit(self.tag, {"data": item})


if __name__ == "__main__":
    q = WsQueue("simple_queue")
    # a simple test
    q.put([1, 2, 3])

    # 1. run `redis-server`, make sure local redis-server started
    # 2. run `redis-client` to login redis
    # 3. run `subscribe flask-socketio` to subscribe events from ME
    # 4. run `python ws_queue.py`
    # 5. you'll get event notification in redis (subscribed mode)
