import psycopg2

PGHOST = 'ep-damp-breeze-a2gsmwtk-pooler.eu-central-1.aws.neon.tech'
PGDATABASE = 'neondb'
PGUSER = 'neondb_owner'
PGPASSWORD = 'npg_tZP8q5mRAodc'
PORT = 5432

with psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT) as connection:
    with connection.cursor() as cursor:
        # query = """
        #     CREATE TABLE brand(
        #         id SERIAL PRIMARY KEY,
        #         name VARCHAR(50) UNIQUE NOT NULL
        #     )
        #     """
        # cursor.execute(query)
        query = """
            CREATE TABLE IF NOT EXISTS topic_inf(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) UNIQUE NOT NULL
                );

            CREATE TABLE IF NOT EXISTS user_inf(
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL
                );
            CREATE TABLE IF NOT EXISTS post(
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES user_inf(id),
                    topic_id INTEGER REFERENCES topic_inf(id),
                    post_text VARCHAR(150) UNIQUE NOT NULL
            );
        """
        cursor.execute(query)



with psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT) as connection:
        with connection.cursor() as cursor:
            query_insert = 'INSERT INTO topic_inf(name) VALUES(%s) RETURNING id, name'
            topics_ex = [('topic111',),('topic223',),('cars',),('planes',)]
            cursor.executemany(query_insert, topics_ex)

            query_insert = 'INSERT INTO user_inf(username, email) VALUES(%s,%s) RETURNING id,username'
            users_ex = [
                ('user12', 'user12@example.com'),
                ('user22', 'user22@example.com'),
            ]
            cursor.executemany(query_insert, users_ex)

            # query_insert = 'INSERT INTO post(user_id,topic_id,post_text) VALUES(%s,%s,%s)'
            # post_info = [
            # (5, 5, 'info_post_1'),
            # (6, 6, 'info_post_2'),
            # ]
            # cursor.executemany(query_insert, post_info)
