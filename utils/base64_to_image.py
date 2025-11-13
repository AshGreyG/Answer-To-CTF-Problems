from typing import Optional
from utils.base64 import Base64

def base64_to_image(base64_encoded : str, path : Optional[str] = None) -> None :
    if "," in base64_encoded :
        base64_encoded = base64_encoded.split(",")[-1]

    try :
        image_bytes = Base64.decode(base64_encoded)

        if path :
            with open(path, "wb") as image :
                image.write(image_bytes)
                print(f"Image has been saved to {path}")

    except Exception as error :
        print(f"Failed to convert base64 to image: {error}")
        return None
