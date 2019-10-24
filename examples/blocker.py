if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        fp = path.dirname(path.dirname(path.abspath(__file__)))
        print(fp)
        sys.path.append(fp)
        from proxy2 import *
    else:
        from ..proxy2 import *


    class DomainBlocker(ProxyRequestHandler):
        def request_handler(self, req, req_body):
            blacklist = [
                'wikipedia.org'
            ]
            for b_domain in blacklist:
                if b_domain in req.path:
                    print("blocked by %s blacklist item" % b_domain)
                    self.block_request(req, req_body)
                    return True

        def block_request(self, req, req_body):
            print(req.path)
            data = "BLOCKED"
            self.wfile.write("%s %d %s\r\n" % (self.protocol_version, 200, 'OK'))
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', len(data))
            self.end_headers()
            self.wfile.write(data)
            self.wfile.flush()

        def save_handler(self, req, req_body, res, res_body):
            pass  # disable printing


    test(HandlerClass=DomainBlocker)
