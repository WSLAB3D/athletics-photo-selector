import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose

def estimate_pose(img_path):
    img = cv2.imread(img_path)
    with mp_pose.Pose(static_image_mode=True) as pose:
        results = pose.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        if not results.pose_landmarks:
            return {"pose_score": 0}
        score = len(results.pose_landmarks.landmark)
        return {"pose_score": score}
