from app import create_app

app = create_app(config_name="prod")


print(
    f"App initialized with config: "
    f"DB={app.config['SQLALCHEMY_DATABASE_URI']}, "
    f"SECRET_KEY=***"
)

if __name__ == "__main__":
    app.run()