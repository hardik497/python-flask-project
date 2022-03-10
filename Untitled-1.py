
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.88.1">
    <title>Admin Panel</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.1/examples/sign-in/">

    

    <!-- Bootstrap core CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <!-- Favicons -->
<link rel="apple-touch-icon" href="/docs/5.1/assets/img/favicons/apple-touch-icon.png" sizes="180x180">
<link rel="icon" href="/docs/5.1/assets/img/favicons/favicon-32x32.png" sizes="32x32" type="image/png">
<link rel="icon" href="/docs/5.1/assets/img/favicons/favicon-16x16.png" sizes="16x16" type="image/png">
<link rel="manifest" href="/docs/5.1/assets/img/favicons/manifest.json">
<link rel="mask-icon" href="/docs/5.1/assets/img/favicons/safari-pinned-tab.svg" color="#7952b3">
<link rel="icon" href="/docs/5.1/assets/img/favicons/favicon.ico">
<meta name="theme-color" content="#7952b3">


    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>

    
    <!-- Custom styles for this template -->
    <link href="{{url_for('static',filename='css/signin.css')}}" rel="stylesheet">
  </head>
  <body class="text-center" style="background-image: url('        {{ url_for('static', filename='assets/img/backg.jpg') }}      ' )">
    
<main class="form-signin">
  <form  action="/dash" method="post">
    {% set fname = 'assets/img/' +  params['img']  %}
    <img class="mb-4" src="{{url_for('static',filename=fname)}}" alt="" width="72" height="57">
    <h1 class="h3 mb-3 fw-normal">Admin</h1>

    <div class="form-floating">
      <input type="email" name = "uname" class="form-control" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">Email address</label>
    </div>
    <div class="form-floating">
      <input type="password" name = "password" class="form-control" id="floatingPassword" placeholder="Password">
      <label for="floatingPassword">Password</label>
    </div>

    <div class="checkbox mb-3">
      <label>
        <input type="checkbox" value="remember-me"> Remember me
      </label>
    </div>
    <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
    <p class="mt-5 mb-3 text-muted">&copy;{{params['blog_name ']}} 2017–2022</p>
  </form>
</main>


    
  </body>
</html>




@app.route("/index")
def home():
    posts = Posts.query.filter_by().all()
    #[0:params['no_post']]
    last = math.ceil(len(posts)/int(params['no_post']))


    page  = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1

    page  = int(page)
    posts = posts[(page-1)*int(params['no_post']):(page-1)*int(params['no_post']) + (page-1)*int(params['no_post'])]
    if page == 1:
        prev = "#"
        next = "/?page="+ str(page+1)
    elif page == last:
        prev = "/?page="+ str(page-1)
        next = "#"
    else:
        prev = "/?page="+ str(page-1)
        next = "/?page="+ str(page+1)
    return render_template('index.html',params = params,posts=posts,prev=prev, next=next)