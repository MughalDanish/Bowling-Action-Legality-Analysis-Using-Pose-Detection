import tkinter as tk
from tkinter import Tk, filedialog, Button, Scale, HORIZONTAL, Label, Frame, PhotoImage
import tkinter.messagebox as messagebox
import cv2
from functools import partial
import PoseModule as pm



class BowlingAnalysisApp:
    def __init__(self, root):
    
        self.root = root
        self.root.title("Fast Bowling Analysis")
        self.root.geometry("1920x1080")
        self.root.configure(bg="blue")
        self.pTime = 0
        self.detector = pm.poseDetector()
        

        # Top Navigation Bar
        self.nav_frame = tk.Frame(self.root, bg="red", width=1920, height=50)
        self.nav_frame.pack(side="top", fill="x")

        self.video_label = tk.Label(self.nav_frame, text="Fast Bowling Analysis", bg="red", fg="white", font=("Arial", 16))
        self.video_label.pack(side="left", padx=(20, 0), pady=10)

        self.help_button = tk.Button(self.nav_frame, text="Help", bg="orange", fg="white", command=self.open_help, relief=tk.GROOVE)
        self.help_button.pack(side="right", padx=(0, 20), pady=10)
      
        self.video_frame = Frame(self.root)
        self.video_frame.pack(side="left", padx=30, pady=30, fill="both")

        self.video_frame_label = Label(self.video_frame)
        self.video_frame_label.pack(fill="both", expand=True)
        
        #Left Side Control Button 

        self.left_control_frame = Frame(self.root, bg="blue")
        self.left_control_frame.pack(side="left", padx=100, pady=20, fill="y")

        self.before_release_button = self.create_left_side_button("Before Release ball", self.before_release_ball, "yellow")
        self.before_release_button.pack(pady=10)
        
        self.on_release_button = self.create_left_side_button("On Release ball", self.on_release_ball, "yellow")
        self.on_release_button.pack(pady=10)

        self.result_button = self.create_left_side_button("Tab to check result", self.result, "red")
        self.result_button.pack(pady=10)


        # Right Side Control Buttons
        self.control_frame = Frame(self.root, bg="blue")
        self.control_frame.pack(side="right", padx=20, pady=20, fill="y")
       
        
        
        self.browse_button = self.create_button("Browse Video", self.browse_video, "green")
        self.browse_button.pack(pady=10)

        self.speed_button = self.create_button("Playback Speed", None, "yellow")
        self.speed_button.pack(pady=10)

        self.speed_scale = Scale(self.control_frame, from_=0.1, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, length=200, bg="white", label="Speed", command=self.set_speed)
        self.speed_scale.set(1.0)
        self.speed_scale.pack(pady=10)

        self.restart_button = self.create_button("Restart", self.restart_video, "purple")
        self.restart_button.pack(pady=10)

        self.stop_button = self.create_button("Pause", self.stop_video, "red")
        self.stop_button.pack(pady=10)

        self.resume_button = self.create_button("Resume", self.resume_video, "blue")
        self.resume_button.pack(pady=10)

        self.backward_button = self.create_button("Backward", partial(self.seek_video, -10), "cyan")
        self.backward_button.pack(pady=10)

        self.forward_button = self.create_button("Forward", partial(self.seek_video, 10), "brown")
        self.forward_button.pack(pady=10)

        self.bw_var = tk.BooleanVar(value=False)
        self.bw_button = tk.Checkbutton(self.control_frame, text="Black & White", variable=self.bw_var, command=self.convert_to_bw, bg="white")
        self.bw_button.pack(pady=10)

        self.video_path = None
        self.cap = None
        self.playback_speed = 1.0
        self.paused = False
        self.on_release = False
        self.before_release = False
        self.on_ball_release_angle = None
        self.before_ball_release_angle = None

    def create_button(self, text, command, bg):
        return Button(self.control_frame, text=text, command=command, bg=bg, fg="black", width=15, relief=tk.GROOVE, borderwidth=3, font=("Arial", 12))
    
    def create_left_side_button(self, text, command, bg):
        return Button(self.left_control_frame, text=text, command=command, bg=bg, fg="black", width=15, relief=tk.GROOVE, borderwidth=3, font=("Arial", 12))


    def browse_video(self):
        self.video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])
        if self.video_path:
            self.cap = cv2.VideoCapture(self.video_path)
            self.cap.set(cv2.CAP_PROP_FPS, 15)
            self.play_video()

    def set_speed(self, speed):
        self.playback_speed = float(speed)

    def before_release_ball(self):
        self.before_release = True

    def on_release_ball(self):
        self.on_release = True

    def result(self):
        angle = self.before_ball_release_angle - self.on_ball_release_angle
        if angle <=15:
            messagebox.showinfo("Legal Action", f"Angle Difference: {angle} degrees")
        else:
            messagebox.showinfo("Illegal", f"Angle Difference: {angle} degrees")

        

    def stop_video(self):
        self.paused = True

    def resume_video(self):
        self.paused = False
        self.play_video()

    def restart_video(self):
        if self.cap:
            self.cap.release()  # Release the existing video capture object
        self.cap = cv2.VideoCapture(self.video_path)  # Create a new video capture object
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0) 
        self.cap.set(cv2.CAP_PROP_FPS, 15)
        self.paused = False
        self.play_video()

    def seek_video(self, sec):
        current_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
        total_frames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        new_frame = current_frame + (sec * 15)  # Assuming 15 frames per second
        if 0 <= new_frame <= total_frames:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, new_frame)


    def convert_to_bw(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (500, 580))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
            self.update_video_label(frame)

    def play_video(self):
        success, img = self.cap.read()
        #img = cv2.imread("data14.jpeg")
        if success:
            img = cv2.resize(img, (500, 580))
            img = self.detector.findPose(img)
            lmList = self.detector.findPosition(img, draw=False)
            angle = self.detector.findAngle(img, 12,14,16,draw=True)
            print(angle)
            if len(lmList) !=0:
                print(lmList[14])
                cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)
            self.update_video_label(img)

            
            if not self.paused:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.cap.get(cv2.CAP_PROP_POS_FRAMES) + self.playback_speed)

        if self.on_release:
                self.on_ball_release_angle =self.detector.findAngle(self.cap.get(cv2.CAP_PROP_POS_FRAMES),12,14,16,draw=False)
                self.on_release = False
                messagebox.showinfo("Angle on release ball", f"Angle : {self.on_ball_release_angle} degrees")

        if self.before_release:
            self.before_ball_release_angle =self.detector.findAngle(self.cap.get(cv2.CAP_PROP_POS_FRAMES),12,14,16,draw=False)
            self.before_release = False
            messagebox.showinfo("Angle before release ball", f"Angle : {self.before_ball_release_angle} degrees")
            

       
        if not self.paused:
            self.root.after(10, self.play_video)

    def update_video_label(self, frame):
        photo = self.convert_to_tkimage(frame)
        self.video_frame_label.configure(image=photo)
        self.video_frame_label.image = photo


    def convert_to_tkimage(self, frame):
        return PhotoImage(data=cv2.imencode('.png', frame)[1].tobytes())

    def open_help(self):
        # Placeholder function for opening help
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = BowlingAnalysisApp(root)
    root.mainloop()
