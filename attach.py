#!/usr/bin/env python3
import argparse
import subprocess
import shlex
import os

def mux_subtitles(video_in: str, subs_in: str, output_dir: str, force: bool = False):
    # 出力ディレクトリがなければ作成
    os.makedirs(output_dir, exist_ok=True)

    # 入力ファイル名から拡張子なしのベース名を取得
    base = os.path.splitext(os.path.basename(video_in))[0]
    # 出力ファイル名をディレクトリ内に自動生成（.mp4 拡張子）
    video_out = os.path.join(output_dir, f"{base}.mp4")

    cmd = [
        "ffmpeg",
        "-i", video_in,
        "-i", subs_in,
        "-c:v", "copy",
        "-c:a", "copy",
        "-c:s", "mov_text",
    ]
    if force:
        cmd.insert(0, "-y")  # 既存出力を上書き
    cmd.append(video_out)

    print("Running:", " ".join(shlex.quote(c) for c in cmd))
    subprocess.run(cmd, check=True)
    print(f"Done. Output file: {video_out}")

def main():
    parser = argparse.ArgumentParser(description="Embed SRT subtitles into an MP4 file using ffmpeg")
    parser.add_argument("--video-in", "-v", required=True,
                        help="Path to input video file (e.g. .mkv/.mp4)")
    parser.add_argument("--srt-in", "-s", required=True,
                        help="Path to input subtitles file (.srt)")
    parser.add_argument("--output-dir", "-o", required=True,
                        help="Directory to save the output .mp4 file")
    parser.add_argument("--force", "-f", action="store_true",
                        help="Overwrite output file if it already exists")
    args = parser.parse_args()

    mux_subtitles(args.video_in, args.srt_in, args.output_dir, args.force)

if __name__ == "__main__":
    main()

