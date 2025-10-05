import requests
import time

class ApiLookup:

    def __init__(self, endpoint, width, height, max_retries=5, base_delay=10):
        self.endpoint = endpoint
        self.width = width
        self.height = height
        self.max_retries = max_retries
        self.base_delay = base_delay

    def get_random_image(self):
        url = f"{self.endpoint}/random-photo"
        attempt = 0
        while attempt < self.max_retries:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    data["url"] = f"{self.endpoint}/image/{self.width}x{self.height}/{data['path']}"
                    return data
                else:
                    raise Exception("Failed to fetch random photo")
            except Exception as e:
                attempt += 1
                if attempt >= self.max_retries:
                    raise Exception(f"Failed after {self.max_retries} attempts: {e}")
                delay = self.base_delay * (2 ** (attempt - 1))
                time.sleep(delay)