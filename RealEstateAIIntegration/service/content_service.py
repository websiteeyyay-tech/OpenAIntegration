from openai import OpenAI

class ContentService:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def generate_description(self, property_data):
        prompt = (
            f"Write an attractive real estate listing for a {property_data['bedrooms']}-bedroom "
            f"home in {property_data['location']} priced at {property_data['price']}. "
            f"Highlight amenities and lifestyle benefits."
        )
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def create_staging_image(self, image_path, style="modern luxury"):
        response = self.client.images.generate(
            model="gpt-image-1",
            prompt=f"Virtually stage this property in {style} style.",
            size="1024x1024"
        )
        return response.data[0].url
