import requests
import time

# Provide the paths directly in the code
image_path = "C:/Users/priya/Downloads/bottle.jpg"  # Replace with the path to your image file
output_file = "C:/Users/priya/OneDrive/Desktop/ocr/ocr_practice/output_text.txt"    # Replace with the desired output file name

subscription_key = "f589704f25234f469768230302e1759a"
endpoint = "https://computervisionmodel1.cognitiveservices.azure.com/"
ocr_url = endpoint + "vision/v3.2/read/analyze"

# Read the image into a byte array
with open(image_path, "rb") as image_file:
    image_data = image_file.read()

headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/octet-stream"
}

response = requests.post(ocr_url, headers=headers, data=image_data)

# Check if the request was successful
if response.status_code != 202:
    raise Exception("Failed to analyze image. Status code: {}".format(response.status_code))

# Get the URL where the API results will be available
operation_url = response.headers["Operation-Location"]

# Wait for the OCR operation to complete
print("Waiting for OCR results...")
time.sleep(10)

# Get the results from the operation URL
result_response = requests.get(operation_url, headers={"Ocp-Apim-Subscription-Key": subscription_key})

# Check if the result retrieval was successful
if result_response.status_code != 200:
    raise Exception("Failed to retrieve results. Status code: {}".format(result_response.status_code))

# Parse the JSON response
results = result_response.json()

# Check the status of the OCR operation
if results["status"] == "succeeded":
    # Open the output file in write mode with utf-8 encoding
    with open(output_file, "w", encoding="utf-8") as output_file_handle:
        # Save the recognized text to the file
        for read_result in results["analyzeResult"]["readResults"]:
            for line in read_result["lines"]:
                output_file_handle.write(line["text"] + "\n")
    print(f"OCR results successfully saved to {output_file}")
else:
    print("OCR operation did not succeed. Status: {}".format(results["status"]))
