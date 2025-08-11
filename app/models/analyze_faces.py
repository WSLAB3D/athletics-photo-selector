from deepface import DeepFace

def analyze_faces(img_path):
    try:
        analysis = DeepFace.analyze(img_path, actions=['gender', 'age', 'race'], enforce_detection=False)
        return {
            "gender": analysis[0]["gender"],
            "age": analysis[0]["age"],
            "ethnicity": analysis[0]["dominant_race"]
        }
    except:
        return {"gender": "unknown", "age": "unknown", "ethnicity": "unknown"}
