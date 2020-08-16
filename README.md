# docker_python
Creating images in Docker using Python, Flask Web App, and Pandas

- You can try with source code

# Image creation steps

- PyCharm ile New Project

- Choose Flask application , Existing interpreter

<img src="images/create.png"  alt="drawing" width="600"/>



- CREATE


- Flask Project Folder

<img src="images/flask_app.png" alt="drawing" width="600"/>


- flaskProject/app  , create

- app/app.py  , create



``` Python
    #app/app.py

    from flask import Flask,render_template
    import pandas as pd
    import re


    # Python codes .......................
    # ....................................



    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return render_template('index.html',data = data)


    if __name__ == '__main__':
        app.run(host='0.0.0.0',port=5000)

```


- app/data.json , create

- app/templates/index.html ,create

- flaskProject/Dockerfile , create

<img src="images/docker_file.png" alt="drawing" width="600"/>

- flaskProject/requirements.txt ,create

<img src="images/require.png" alt="drawing" width="600"/>

``` text
    #requirements.txt

    click==7.1.2
    Flask==1.1.2
    Jinja2==2.11.2
    MarkupSafe==1.1.1
    pip==20.2.1
    Werkzeug==1.0.1
    pandas==1.1.0


```

Project folder

<img src="images/app_folder.png" alt="drawing" width="600"/>


- Acknowledging that Docker is preinstalled 


- We create a docker image named dene2

``` sh

    docker build -t dene2:latest .

```


- We create a docker image named flask

<img src="images/docker_images.png" alt="drawing" width="600"/>


``` sh

    docker run -p 5000:5000 dene2

```

<img src="images/docker_run.png" alt="drawing" width="600"/>



- With CMD + LEFT CLICK we can go to the web page


<img src="images/flask_web.png" alt="drawing" width="600"/>


- Now we can send our created flask application container to our storage area on the docker hub.

- We copy a new image with the same image ID using the 'docker image tag dene2 aydbirol164494/dene2' command.
  

``` sh

    docker image tag dene2 aydbirol164494/dene2

```

- Using the ' docker push aydbirol164494/dene2 ' command, we now send this image file we created to our storage area on the docker hub.

<img src="images/dockerhub.png" alt="drawing" width="600"/>

- With our control, we can see the 'aydbirol164494/dene2' image file on the docker hub at the same time.

- In order to test whether we can create a container by downloading the new image file from the hub, we first delete the 'aydbirol164494/dene2' image file using the docker image rm -f 447fafafb619 command.

``` sh

    docker image rm -f 447fafafb619 

```

<img src="images/image_del.png" alt="drawing" width="600"/>


- Again, we must run the command 'docker container run --rm --publish 5000: 5000 aydbirol164494/dene2' and download the image file from the docker hub and use this image to raise our container. We can examine this process from the picture below.

``` sh

    docker container run --rm --publish 5000:5000 aydbirol164494/dene2

```

<img src="images/download_image.png" alt="drawing" width="600"/>




<img src="images/image_up.png" alt="drawing" width="600"/>

- We have learned a brief information about how to create an image file, how to configure and run the Dockerfile file, how to set up containers over the image, and how to use the docker hub.