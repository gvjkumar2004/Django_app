from django.shortcuts import render
from django.http import HttpResponse

def docker_message(request):
    html_content = """
    <html>
    <head>
        <title>Dockerized Django App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f8ff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
                background-color: #4682B4;
                padding: 50px;
                border-radius: 10px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                color: white;
            }
            h1 {
                font-size: 48px;
                margin-bottom: 20px;
            }
            p {
                font-size: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎉 Containerized with Docker! 🎉</h1>
            <p>This Django application is now running in a Docker container.</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

