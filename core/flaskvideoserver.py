from flask import Flask, render_template, Response

class FlaskVideoServer:
    def __init__(self, liveVideoFrameQueue):
        self.app = Flask(__name__)
        @self.app.route('/')
        def index():
            """Video streaming home page."""
            return render_template('index.html')

        @self.app.route('/video_feed')
        def video_feed():
            """Video streaming route. Put this in the src attribute of an img tag."""
            return Response(self.gen(liveVideoFrameQueue), mimetype='multipart/x-mixed-replace; boundary=frame')

    def getFlaskApp(self):
        return self.app

    def gen(self, liveVideoFrameQueue):
        """Video streaming generator function."""
        while True:
            frame = liveVideoFrameQueue.get()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
