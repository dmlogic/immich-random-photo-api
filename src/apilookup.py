import requests

class ApiLookup:

    def __init__(self, endpoint, width, height):
        self.endpoint = endpoint
        self.width = width
        self.height = height

    def get_random_image(self):
        url = f"{self.endpoint}/random-photo"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            data["url"] = f"{self.endpoint}/image/{self.width}x{self.height}/{data['path']}"
            return data
        else:
            raise Exception("Failed to fetch random photo")
