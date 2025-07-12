#!/usr/bin/env python3
import argparse
import whisper
from whisper.utils import get_writer

def main():
    parser = argparse.ArgumentParser(
        description="Transcribe audio/video to SRT using Whisper (simple args)"
    )
    parser.add_argument(
        "--video-in", "-v", required=True,
        help="Path to input audio/video file (e.g. .mkv, .mp4)"
    )
    parser.add_argument(
        "--output-dir", "-o", default=".",
        help="Directory to save the SRT file"
    )
    args = parser.parse_args()

    print(f"Loading Whisper model (default: medium) …")
    model = whisper.load_model("medium", device="cuda")

    print(f"Transcribing: {args.video_in}")
    result = model.transcribe(
        audio=args.video_in,
        language="en",
        task="transcribe"
    )

    print("Writing SRT file…")
    writer = get_writer("srt", output_dir=args.output_dir)
    writer(result, args.video_in)

    print(f"Done. SRT saved into: {args.output_dir}")

if __name__ == "__main__":
    main()
