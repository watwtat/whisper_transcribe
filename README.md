# transcribe.py

## 概要

このスクリプトは、OpenAI Whisperモデルを使って音声・動画ファイル（例: .mkv, .mp4）から英語の音声を書き起こし、SRT字幕ファイルを生成します。

## 必要条件
- Python 3.x
- whisper パッケージ（`pip install openai-whisper`）
- CUDA対応GPU（推奨、CPUでも動作しますが遅くなります）

## 使い方

1. 必要なPythonパッケージをインストールします。
   ```
   pip install openai-whisper
   ```
2. コマンドラインから以下のように実行します。

   ```
   python transcribe.py --video-in 入力ファイル --output-dir 出力ディレクトリ
   ```

### オプション
- `--video-in`, `-v`: 入力音声/動画ファイルのパス（例: sample.mkv）
- `--output-dir`, `-o`: SRTファイルの出力先ディレクトリ（省略時はカレントディレクトリ）

### 実行例
```
python transcribe.py -v sample.mp4 -o ./output
```

## 注意
- デフォルトでWhisperの"medium"モデルをCUDA（GPU）で使用します。CPUで実行したい場合は、`device="cpu"`にコードを修正してください。
- 出力SRTファイルは指定したディレクトリに保存されます。

## ライセンス
このプロジェクトはMITライセンスです。
