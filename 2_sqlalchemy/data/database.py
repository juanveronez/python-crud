from sqlalchemy import create_engine

# uri_format = 'dialect+driver://username:password@host:port/database'
uri_sqlite = 'sqlite:///data/my-database.db'
engine = create_engine(uri_sqlite, echo=True)

print('Conexão com SQLite estabelecida')