from flask import Flask, jsonify, send_file, abort
from dotenv import load_dotenv
from src import lookup, transform
import io

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

# /image/800x600/upload/b97a4f5d-0316-4b82-b46f-5e10f1a57ceb/d6/b5/d6b57617-b15a-4987-9dd7-f399266c1fb0.jpg
@app.route('/image/<int:width>x<int:height>/<path:image_path>', methods=['GET'])
def serve_image(width, height, image_path):

    image_dir = os.getenv('IMMICH_PATH')
    full_path = os.path.join(image_dir, image_path)
    if not os.path.isfile(full_path):
        abort(404)

    transformer = transform.ImageTransformer(width, height)
    image = transformer.transform(full_path)

    return send_file(
        io.BytesIO(image),
        mimetype='image/jpeg',
        as_attachment=False
    )

if __name__ == '__main__':
    # '0.0.0.0' makes it accessible on your local network
    app.run(host='0.0.0.0', port=8000)
