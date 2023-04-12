import cv2
import argparse
from ultralytics import YOLO
import supervision as sv
import numpy as np
import speech_recognition as sr


name = 'siri'

ZONE_POLYGON = np.array([
    [0, 0],
    [1280, 0],
    [1250, 720],
    [0, 720]
    
])
def parse_arguments() -> argparse.Namespace:
    parser= argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument (
        "--webcam-resolution",
        default=[1280, 720],
        nargs=2,
        type=int
    )
    args= parser.parse_args()
    return args


def main():
    args= parse_arguments()
    frame_width, frame_height = args.webcam_resolution
    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
    
    model = YOLO("yolov8l.pt")
    box_annotador = sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,
        text_scale=1
    )
      
    zone = sv.PolygonZone(polygon=ZONE_POLYGON, frame_resolution_wh=tuple(args.webcam_resolution))
    zone_annotador = sv.PolygonZoneAnnotator(zone=zone, color=sv.Color.red())  
    while True:
        ret, frame = cap.read()
        
        result = model(frame)[0]
        detections = sv.Detections.from_yolov8(result)
        labels = [
            f"{model.model.names[class_id]}"
            for _, confidence, class_id,_ 
            in detections
        ]
        
        frame = box_annotador.annotate(
            scene=frame, 
            detections=detections, 
            labels=labels)
        
        zone.trigger(detections=detections)
        frame = zone_annotador.annotate(scene=frame)
        
        cv2.imshow("yolov8", frame)
        
        
        if(cv2.waitKey(30) == 27):
            break
        
    return labels

if __name__ == "__main__":
    main()

 