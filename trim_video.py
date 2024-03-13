import sys
import ffmpeg
from ffmpeg import Error as FFmpegError

def trim_video(input_file, output_file, duration_minutes):
    try:
        duration_seconds = int(duration_minutes) * 60
        ffmpeg.input(input_file, ss=0).output(output_file, t=duration_seconds).run()
        print("Trimming complete!")
    except FFmpegError as e:
        print(f"An error occurred while trimming video: {e.stderr.decode()}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python trim_video.py <input_file.mp4> <duration_in_minutes>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    duration_minutes = sys.argv[3]

    trim_video(input_file, output_file, duration_minutes)
