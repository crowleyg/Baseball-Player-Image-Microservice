from bs4 import BeautifulSoup
import requests

while True:

    # check player_url.txt file for player url
    with open("player_url.txt", "r") as file:
        line = file.readline()

    if line != '':

        # clear previous response
        with open("player_images.txt", "w") as file:
            file.truncate(0)

        # get page from file generated URL
        URL = f"{line}"
        page = requests.get(URL)

        # check for invalid url
        if page.status_code != 200:
            with open("player_images.txt", "w") as file:
                file.write("ERROR: Invalid URL")

        # parse page content
        soup = BeautifulSoup(page.content, "html.parser")

        # hold all valid image addresses in array
        img_urls = []

        # find all image urls and store in array
        images = soup.findAll('img')
        for image in images:
            if "Photo of" in image['alt']:
                img_urls.append(image['src'])

        # check if array is empty
        if img_urls == []:
            with open("player_images.txt", "w") as file:
                file.write("No Images Found")

        # write img_urls to player_url file
        with open("player_images.txt", "w") as file:
            for url in img_urls:
                file.write(f"{url}\n")

        # clear request from player_url.txt
        with open("player_url.txt", "w") as file:
            file.truncate(0)

        # display contents of array (Debugging)
        # print(img_urls)