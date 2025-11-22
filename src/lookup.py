import psycopg

class DatabaseLookup:

    def __init__(self, connection_string):
        self.connection = psycopg.connect(connection_string)

    def get_random_photo(self):
        query = """
        select a.id, album."albumName", a."originalPath", a."fileCreatedAt"
        from asset a
        join album_asset aa on aa."assetId" = a.id
        join album on album.id = aa."albumId"
        where a."type" = 'IMAGE'
            and album."albumName" not like '\\_%'
        order by random()
        limit 1
        """

        with self.connection.cursor() as cur:
            cur.execute(query)
            return cur.fetchone()
