from flask import Flask, jsonify, send_from_directory
from dotenv import load_dotenv
from src import lookup
import os

load_dotenv()

connection_string = (
            f"dbname={os.getenv('PG_DATABASE')} "
            f"user={os.getenv('PG_USER')} "
            f"password={os.getenv('PG_PASSWORD')} "
            f"host={os.getenv('PG_HOST')} "
            f"port={os.getenv('PG_PORT')}"
        )
db_lookup = lookup.DatabaseLookup(connection_string)

app = Flask(__name__)

@app.route('/random-photo', methods=['GET'])
def random_photo():
    rawdata = db_lookup.get_random_photo()
    photo_data = {
        "id": rawdata[0],
        "album": rawdata[1],
        "path": rawdata[2].replace("/data/upload/", "", 1),
        "date": rawdata[3].strftime("%Y-%m-%d")
    }
    return jsonify(photo_data)

@app.route('/image/<path:image_path>', methods=['GET'])
def serve_image(image_path):
    image_dir = os.getenv('IMMICH_PATH')
    full_path = os.path.join(image_dir, image_path)
    if not os.path.isfile(full_path):
        abort(404)

    return send_from_directory(image_dir, image_path)

if __name__ == '__main__':
    # '0.0.0.0' makes it accessible on your local network
    app.run(host='0.0.0.0', port=8000)
