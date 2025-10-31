import requests

# The target url is http://117.72.52.127:16490/1.jpg

target_url = "http://117.72.52.127:16490/"

for i in range(1, 100) :
    with requests.get(target_url + str(i) + ".jpg", stream = True) as response :
        if response.status_code == 200 :
            with open(f"./{i}.jpg", "wb") as file :
                for chunk in response.iter_content(chunk_size = 8192) :
                    file.write(chunk)
            print(f"File {i}.jpg has been downloaded")

# File 10.png exsits and if you see the source code of website you will get
# flag
