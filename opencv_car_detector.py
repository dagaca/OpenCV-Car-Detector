import cv2
import tkinter as tk
from tkinter import ttk

class CarDetectionApp:
    def __init__(self, root, video_path):
        """
        Initialize the CarDetectionApp.

        Parameters:
        - root: Tkinter root window
        - video_path: Path to the video file
        """
        self.root = root
        self.root.title("Car Detection App")

        # Open the video capture
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.car_classifier = cv2.CascadeClassifier('haarcascade_car.xml')
        self.cars_window_created = False

        # Variables to store adjustable parameters
        self.scale_factor_var = tk.DoubleVar(value=1.05)
        self.min_neighbors_var = tk.IntVar(value=3)
        self.min_size_var = tk.IntVar(value=30)

        # Create GUI widgets
        self.create_widgets()

    def create_widgets(self):
        """
        Create GUI widgets for the application.
        """
        # Video panel
        self.panel = tk.Label(self.root)
        self.panel.pack(padx=10, pady=10)

        # Scale Factor
        ttk.Label(self.root, text="Scale Factor:").pack()
        scale_factor_slider = ttk.Scale(self.root, from_=1.01, to=2.0, variable=self.scale_factor_var, orient="horizontal", length=200)
        scale_factor_slider.pack()

        # Min Neighbors
        ttk.Label(self.root, text="Min Neighbors:").pack()
        min_neighbors_entry = ttk.Entry(self.root, textvariable=self.min_neighbors_var)
        min_neighbors_entry.pack()

        # Min Size
        ttk.Label(self.root, text="Min Size:").pack()
        min_size_entry = ttk.Entry(self.root, textvariable=self.min_size_var)
        min_size_entry.pack()

        # Start Button
        start_button = ttk.Button(self.root, text="Start Detection", command=self.start_detection)
        start_button.pack()

        # Exit Button
        exit_button = ttk.Button(self.root, text="Exit", command=self.root.destroy)
        exit_button.pack()

    def start_detection(self):
        """
        Start the car detection process.
        """
        while True:
            ret, frame = self.cap.read()

            if not ret:
                # Reset video capture when it reaches the end
                self.cap.release()
                self.cap = cv2.VideoCapture(self.video_path)

            if frame is None:
                continue  # Skip the current iteration if frame is empty

            # Resize the frame
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

            # Convert to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect cars with dynamically adjusted parameters
            cars = self.car_classifier.detectMultiScale(
                gray,
                scaleFactor=self.scale_factor_var.get(),
                minNeighbors=self.min_neighbors_var.get(),
                minSize=(self.min_size_var.get(), self.min_size_var.get())
            )

            # Draw rectangles and display car type
            for (x, y, w, h) in cars:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                car_type = "Car"  # Replace this with your own car classification logic
                cv2.putText(frame, car_type, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Show the number of cars on each frame
            cv2.putText(frame, f'Number of Cars: {len(cars)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Show the frame
            cv2.imshow('Cars', frame)

            # Break the loop when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the video stream
        self.cap.release()

        # Close the Cars window if it's created
        if self.cars_window_created:
            cv2.destroyWindow('Cars')

        # Set the flag to False for the next Start Detection
        self.cars_window_created = False

if __name__ == "__main__":
    # Create Tkinter root window and start the application
    root = tk.Tk()
    app = CarDetectionApp(root, 'C:/Users/dagac/Desktop/People Flow Counter/videos/4K Road traffic video for object detection and tracking - free download now!.mp4')
    root.mainloop()