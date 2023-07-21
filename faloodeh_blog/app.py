from Faloodeh import faloorun, Faloodeh
from models import Post, session
app = Faloodeh()


def home(request, response):
    posts = session.query(Post).all()
    context = {
        'posts':posts
    }
    response.body = app.template('blog/start_page.html', context=context).encode()


def about_page(request, response):
    response.body = app.template('blog/about_page.html', context={}).encode()

def create_post(request, response):
    if request.method == 'POST':
        form = request.POST
        title = form['title']
        slug =  form['slug']
        body = form['text']
        image = request.POST.get('image')
        image_root ='static/media/'+  str(image.filename)
        with open(image_root, 'wb') as img:
            img.write(image.file.read())

        post = Post(title=str(title), body=str(body), slug=str(slug), image=str(image_root))
        session.add(post)
        session.commit()

        # response.text = 'با موفقیط ثبت شد'
        response.headers = [('Location', '/')]       
        response.status_code = 301

    if request.method == 'GET':
        response.body = app.template('blog/create_post.html', context={}).encode()

@app.route("/articles/{slug}")
def post_details(request, response, slug):
    post = session.query(Post).filter(Post.slug == slug).first()
    
    context = {
        'post':post
    }
    response.body = app.template('blog/detail_page.html', context=context).encode()


app.add_route('/about', about_page)    
app.add_route('/', home)
app.add_route('/create', create_post)  

app.host = '127.0.0.1'
app.port = 5000
# faloorun(host=app.host, port=app.port, app=app)
if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(app, host=app.host, port=app.port)
