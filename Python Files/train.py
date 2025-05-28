# Import YOLO class from ultralytics library
from ultralytics import YOLO
import os

def main():
    # Optional: Prevent memory fragmentation
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

    # Path to the data.yaml file
    data_yaml_path = r"D:\Projects\SLT\New Dataset\Split_Data\data.yaml"

    # Create a YOLO model object for YOLOv8 Nano
    model = YOLO('yolov8n.pt')  # Pretrained YOLOv8 Nano weights

    # Train the model
    model.train(
        data=data_yaml_path,  # Path to the data.yaml file
        epochs=120,           # Number of training epochs
        batch=8,              # Reduced batch size for 6GB GPU
        imgsz=416,            # Reduced image size for memory savings
        optimizer='Adam',     # Optimizer
        lr0=0.01,             # Initial learning rate
        patience=25,
        device='cuda'         # Optional: force use of GP
    )

    # Save the trained model
    model.export(format='torchscript')  # Export the model in TorchScript format

if __name__ == '__main__':
    main()
