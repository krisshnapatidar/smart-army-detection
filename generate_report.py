import os

# Path to the detections/report folder
folder_path = "C:/Users/kp167/yolov5/detections/report"  # Modify if your path is different

# Create a report file
report_file = os.path.join(folder_path, "detection_report.txt")

# Open the report file for writing
with open(report_file, 'w') as report:
    # Iterate through all label files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):  # Only process label files
            label_path = os.path.join(folder_path, filename)
            image_name = filename.replace('.txt', '.jpg')  # Assuming corresponding image file is a .jpg

            report.write(f"Detection Report for {image_name}\n")
            report.write(f"---------------------------------\n")
            with open(label_path, 'r') as label_file:
                for line in label_file:
                    data = line.strip().split()  # Split the line by spaces
                    class_id, x_center, y_center, width, height, conf_score = data
                    report.write(f"Class: {class_id}, Confidence: {conf_score}, "
                                 f"Coordinates: ({x_center}, {y_center}), Size: ({width}, {height})\n")
            report.write("\n\n")

print(f"Report generated at {report_file}")
