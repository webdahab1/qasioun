"""Local dev server for the Qasioun site.

Same as `python -m http.server`, with one difference: the page itself is sent
with `Cache-Control: no-store`, so a normal refresh always shows index.html as
it is on disk. The stock server sends no cache header at all, which lets the
browser keep showing an old copy after an edit.

Videos and images keep normal caching so refreshes stay fast.

Usage:  python .claude/serve.py [port]      (default 8777)
"""
import http.server
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8777
NO_CACHE = ('.html', '.css', '.js')


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        path = self.path.split('?', 1)[0]
        if path.endswith('/') or path.endswith(NO_CACHE):
            self.send_header('Cache-Control', 'no-store')
        super().end_headers()


if __name__ == '__main__':
    with http.server.ThreadingHTTPServer(('', PORT), NoCacheHandler) as httpd:
        print(f'Qasioun dev server: http://localhost:{PORT}  (page is never cached)')
        httpd.serve_forever()
