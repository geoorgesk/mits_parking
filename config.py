class Config:
    # 🔹 Replace this with your actual Neon PostgreSQL connection string
    SQLALCHEMY_DATABASE_URI = "psql 'postgresql://neondb_owner:npg_9IQPBJ4eoUDO@ep-proud-shape-a1r11ec3.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'"

    # Disable modification tracking (improves performance)
    SQLALCHEMY_TRACK_MODIFICATIONS = False