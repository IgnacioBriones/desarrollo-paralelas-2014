import tornado.httpserver, tornado.ioloop, tornado.web
from tornado.options import define, options
import subprocess

define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/upload", UploadHandler),
            (r"/runalgorithm", AlgorithmHandler)
        ]
        tornado.web.Application.__init__(self, handlers)
        
class AlgorithmHandler(tornado.web.RequestHandler):

    def get(self):
        pass
    def post(self):
        subprocess.call(["mpiexec", "-n 10", "--host hostfile", "python"])

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../static/main.html")

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        file1 = self.request.files['file1'][0]
        original_fname = file1['filename']
        output_file = open("../uploads/" + original_fname, 'w')
        output_file.write(file1['body'])
        self.finish("file" + original_fname + " is uploaded")

def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
