import os
from moviepy.editor import VideoFileClip

INPUT_DIR = "./videos"
OUTPUT_DIR = "./gifs"


def get_relative_file_paths(directory, allowed_extensions):
    """
    指定されたディレクトリ内の特定の拡張子のファイルの相対パスを取得します。

    Parameters:
        directory (str): ファイルパスを取得する対象のディレクトリのパス。
        allowed_extensions (list): 読み込みを許可する拡張子のリスト。

    Returns:
        list: ディレクトリ内の特定の拡張子のファイルの相対パスのリスト。
    """
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext.lower() in allowed_extensions:
                file_paths.append(os.path.relpath(os.path.join(INPUT_DIR, root, file), directory))
    return file_paths


def convert_video_to_gif(input_path, output_path):
    """
    動画ファイルをGIFアニメーションに変換します。

    Parameters:
        input_path (str): 入力動画ファイルのパス。
        output_path (str): 出力GIFアニメーションファイルのパス。
    """
    clip = VideoFileClip(input_path)
    clip = clip.resize(width=600)
    clip.write_gif(output_path, fps=6)
    clip.close()


if __name__ == "__main__":
    allowed_extensions = [".mp4"]
    input_paths = get_relative_file_paths(INPUT_DIR, allowed_extensions)
    output_paths = [OUTPUT_DIR + "/" + os.path.splitext(os.path.basename(path))[0] + ".gif" for path in input_paths]
    for input_path, output_path in zip(input_paths, output_paths):
        convert_video_to_gif(input_path, output_path)
