import os
import logging
import tempfile
import cv2 as cv
from PIL import Image
import streamlit as st
from ultralytics import YOLO


MODEL_DIR = r'C:\Users\Ap computers\Desktop\animal detection\Real-Time-Animal-Species-Detection\runs\detect\train\weights\best.pt'

logging.basicConfig(
    filename="./logs/log.log", 
    filemode='a', 
    level=logging.INFO, 
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s'
)


def main():
    # Load the YOLO model
    global model
    model = YOLO(MODEL_DIR)

    # Define animal classes
    class_names = ['Buffalo', 'Elephant', 'Rhino', 'Zebra', 'Cheetah', 'Fox', 'Jaguar', 'Tiger', 'Lion', 'Panda']

    # Streamlit sidebar for animal classes
    st.sidebar.header("**Animal Classes**")
    for animal in class_names:
        st.sidebar.markdown(f"- *{animal.capitalize()}*")

    st.title("Real-time Animal Species Detection")
    st.write("The aim of this project is to develop an efficient computer vision model capable of real-time wildlife detection.")

    # File uploader for images or videos
    uploaded_file = st.file_uploader("Upload an image or video", type=['jpg', 'jpeg', 'png', 'mp4'])

    if uploaded_file:
        if uploaded_file.type.startswith('image'):
            inference_images(uploaded_file)
        elif uploaded_file.type.startswith('video'):
            inference_video(uploaded_file)
        else:
            st.error("Unsupported file type. Please upload a valid image (JPEG, PNG, JPG) or video (MP4).")


def inference_images(uploaded_file):
    try:
        image = Image.open(uploaded_file)
        predict = model.predict(image)

        boxes = predict[0].boxes
        plotted = predict[0].plot()[:, :, ::-1]

        if len(boxes) == 0:
            st.markdown("**No Detection**")
        else:
            st.image(plotted, caption="Detected Image", width=600)
            logging.info("Detected Image")

    except Exception as e:
        st.error(f"Error processing image: {e}")


def inference_video(uploaded_file):
    try:
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(uploaded_file.read())
        temp_file.close()

        cap = cv.VideoCapture(temp_file.name)
        frame_count = 0

        if not cap.isOpened():
            st.error("Error opening video file.")

        frame_placeholder = st.empty()
        stop_placeholder = st.button("Stop")

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            frame_count += 1
            if frame_count % 2 == 0:
                predict = model.predict(frame, conf=0.75)
                plotted = predict[0].plot()
                frame_placeholder.image(plotted, channels="BGR", caption="Video Frame")

            if stop_placeholder:
                os.unlink(temp_file.name)
                break

        cap.release()

    except Exception as e:
        st.error(f"Error processing video: {e}")


if __name__ == '__main__':
    main()
