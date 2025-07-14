from pathlib import Path
import base64

video_path = Path("video/test2/test_video.mp4") # video paht

with open(video_path, "rb") as video_file:
    encoded_video = base64.b64encode(video_file.read()).decode("utf-8")

html_snippet = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Embedded Video</title>
</head>
<body>
    <h2>Embedded Video (Base64)</h2>
    <video controls width="640" height="360">
        <source src="data:video/mp4;base64,{encoded_video}" type="video/mp4">
        Browser is not support the video tag.
    </video>
</body>
</html>
"""

output_folder = Path("html")

base_filename = "embedded_video"
extension = ".html"

output_path = output_folder / f"{base_filename}{extension}"
counter = 1
while output_path.exists():
    output_path = output_folder / f"{base_filename}_{counter}{extension}"
    counter = counter + 1

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_snippet)

print(f"Saved to {output_path}")
