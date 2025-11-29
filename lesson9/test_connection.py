from sqlalchemy import create_engine, text

DB_URL = "postgresql://lesson9_user:lesson9_password@localhost:5433/lesson9_db"

try:
    engine = create_engine(DB_URL)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print("✅ Подключение успешно!")
        print(f"Версия PostgreSQL: {result.fetchone()[0]}")

        result = connection.execute(text("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
        """))
        tables = [row[0] for row in result]
        print(f"Таблицы в базе: {tables}")

except Exception as e:
    print(f"❌ Ошибка подключения: {e}")
