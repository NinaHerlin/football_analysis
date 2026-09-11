from ultralytics import YOLO

model = YOLO('models/best.pt')  

result = model.predict('input_videos/08fd33_4.mp4', save=True)  
print(result[0])
print ('================================')
for box in result[0].boxes:
    print(box)