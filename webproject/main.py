import web


urls = (
    '/(.*)', 'index'
)
app = web.application(urls, globals())


class index:
    def GET(self, name):
        print("Hello", name, ", How are you doing today?")
        return "<h1>Hello" + name + "</h1>, <b>How are you doing today?</b>"


if __name__ == '__main__':
    app.run()
