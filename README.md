# Baseball-Player-Image-Microservice Communication Contract

* How to Request Data:
  * Write the full url of desired players baseball-reference statistics page(example: https://www.baseball-reference.com/players/a/abreual01.shtml) to player_url.txt.

* How to Receive Data:
  * In order to receive data for each image, read each line from player_images.txt into an array **After** sending the request. (If an error occured/photos did not exist: file will contain error messages "No Images Found" or "ERROR: Invalid URL"). Iterate through array and get page data using requests.get(image).content for access to each image.
  * Note: If using pySimpleGUI, images can only be displayed in png formatting. See convert_jpg() in exampleClient.py code for a solution to this file type conversion problem.

* UML Sequence Diagram:
<img src=microservice_uml.jpg style="width:400px;height:500px;">
