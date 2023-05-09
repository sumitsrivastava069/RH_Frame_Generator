import os
import boto3

rekognition_client = boto3.client('rekognition')
folder_path = 'frame_new/'
confidence_threshold = 80

# Detect labels (objects) and text in the images
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg'):
        image_path = folder_path + filename
        
        response = rekognition_client.detect_labels(
            Image={
                'Bytes': open(image_path, 'rb').read(),
            },
            MinConfidence=confidence_threshold
        )

        # Extract the detected objects and their confidence scores from the response
        detected_objects = response['Labels']
        print(detected_objects)

        # # Process the detected objects
        for obj in detected_objects:
            if obj['Name'] == 'License Plate':
                response = rekognition_client.detect_text(Image={'Bytes': open(image_path, 'rb').read()})
                
                # Extract the detected text from the response
                license_plate_numbers = set()
                for text_detection in response['TextDetections']:
                    detected_text = text_detection['DetectedText']
                    if len(detected_text) >= 6:
                        digit_count = 0
                        char_count = 0
                        for char in detected_text:
                            if char.isdigit():
                                digit_count += 1
                            elif char.isalpha():
                                char_count += 1
                        if digit_count >= 4 and char_count >= 2:
                            license_plate_numbers.add(detected_text)
                
                for license_plate_number in license_plate_numbers:
                    print('Detected license plate number in ' + filename + ': ' + license_plate_number)
                    print()
