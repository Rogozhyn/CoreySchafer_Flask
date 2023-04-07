from flaskblog import create_app

# possible arguments for create_app: 'default', 'development'
app = create_app()

if __name__ == '__main__':
    app.run()
