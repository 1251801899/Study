import web  

render = web.template.render(r'D:\\templates\\')
  
urls = (  
    '/', 'index'  
)  
  
class index:  
    def GET(self):
        i=web.input(name=None)
        return render.index(i.name)

       # name = '应江涛'
       # return render.index(name)
       # return "Hello, world!"  
  
if __name__ == "__main__":  
    app = web.application(urls, globals())  
    app.run()  
