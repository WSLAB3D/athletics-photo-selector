from models import detect_objects, estimate_pose, analyze_faces, score_image, clip_score
import os, pandas as pd, shutil

image_dir = "images"
output = []

for img_file in os.listdir(image_dir):
    img_path = os.path.join(image_dir, img_file)
    tags = {"filename": img_file}
    tags.update(detect_objects.detect_objects(img_path))
    tags.update(estimate_pose.estimate_pose(img_path))
    tags.update(analyze_faces.analyze_faces(img_path))
    tags.update(clip_score.clip_score(img_path))
    tags["score"] = score_image.score_image(tags)
    output.append(tags)

df = pd.DataFrame(output)
top_images = df.sort_values("score", ascending=False).groupby(["gender", "ethnicity"]).head(10)
top_images.to_csv("../output/tagged_images.csv", index=False)

# Copy top images to web/static for gallery
for img in top_images["filename"]:
    shutil.copy(f"images/{img}", f"web/static/{img}")
