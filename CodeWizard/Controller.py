import web


urls = (
    '/', 'home',
    '/', 'register'
)


render = web.template.render("Views/Templates", base="MainLayout")
app = web.application(urls, globals())


# Classes/Routes
# https://stackoverflow.com/questions/52439325/webpy-serving-static-files-staticapp-object-has-no-attribute-directory
class home:
    def GET(self):
        return render.Home()


class register:
    def GET(self):
        return render.Register()


if __name__ == '__main__':
    app.run()
