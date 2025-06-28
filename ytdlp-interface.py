import os
import subprocess
import sys
# "C:\Users\devan\Documents\Desktop\shorts"
# "C:\Users\devan\Music\Playlist"

os.environ["PATH"] += os.pathsep + r"C:\Users\devan\Documents\Desktop\ffmpeg-7.1.1-essentials_build\bin"

def sanitize_filename(title):
    return "".join(c for c in title if c.isalnum() or c in " _-.").strip()


def run_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print("\n❌ Command failed:", command)
        sys.exit(1)


def download_single(link, download_type, output_path, resolution=None):
    base_command = f'yt-dlp -o "{output_path}/%(title).100s.%(ext)s" --embed-subs --write-subs --sub-langs en '

    if download_type == "audio":
        command = base_command + "--extract-audio --audio-format mp3 " + f'"{link}"'
    elif download_type == "video":
        command = base_command + f'-f "bestvideo[height={resolution}]+bestaudio/best" "{link}"'
    else:
        print("❌ Invalid download type")
        return

    run_command(command)


def download_playlist(link, download_type, output_path, max_videos=None, resolution=None):
    base_command = f'yt-dlp -o "{output_path}/%(playlist_index)s-%(title).100s.%(ext)s" --yes-playlist --embed-subs --write-subs --sub-langs en '

    if max_videos:
        base_command += f"--playlist-end {max_videos} "

    if download_type == "audio":
        command = base_command + "--extract-audio --audio-format mp3 " + f'"{link}"'
    elif download_type == "video":
        command = base_command + f'-f "bestvideo[height={resolution}]+bestaudio/best" "{link}"'
    else:
        print("❌ Invalid download type")
        return

    run_command(command)


def main():
    link = input("🔗 Enter YouTube URL: ").strip()
    output_path = input("📁 Enter output folder path: ").strip().replace('"', '')

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    download_type = input("🎵 Audio or 📹 Video? (a/v): ").strip().lower()
    if download_type not in ["a", "v", "audio", "video"]:
        print("❌ Invalid choice. ")
        return

    is_video = download_type in ["v", "video"]
    download_type = "audio" if download_type == "a" or download_type== "audio" else "video"

    resolution = None
    if is_video:
        resolution = input("📺 Enter resolution (e.g. 360, 480, 720): ").strip()
        if not resolution.isdigit():
            print("❌ Please enter a numeric resolution (e.g., 360, 480, 720).")
            return

    is_playlist = "list=" in link and "&index=" not in link

    if is_playlist:
        choice = input("📃 Detected a playlist. Download entire playlist? (Y/n): ").strip().lower()
        if choice == "y" or choice == "yes" or choice == "":
            max_videos = input("🔢 How many videos to download? (Enter for all): ").strip()
            max_videos = int(max_videos) if max_videos else None
            download_playlist(link, download_type, output_path, max_videos, resolution)
        else:
            download_single(link, download_type, output_path, resolution)
    else:
        download_single(link, download_type, output_path, resolution)

    print(f"\n✅ Done! Files saved to: {output_path}")



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Exiting...")
