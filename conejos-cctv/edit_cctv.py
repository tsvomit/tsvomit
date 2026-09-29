#!/usr/bin/env python3
"""Convierte un clip de Kling en un Reel estilo camara nocturna (9:16, timestamp vivo, grano, audio, loop).

Uso:
  pip install imageio-ffmpeg pillow numpy
  python edit_cctv.py clip.mp4 salida.mp4 --text "Cuenta los conejos" --loops 2
"""
import argparse, re, subprocess, sys
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def duration(path):
    out = subprocess.run([FFMPEG, "-i", path], capture_output=True, text=True).stderr
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", out)
    return int(m[1]) * 3600 + int(m[2]) * 60 + float(m[3])


def font(size):
    try:
        return ImageFont.truetype(MONO, size)
    except OSError:
        return ImageFont.load_default()


def overlay_frames(total, start, cam, text, text_from, text_to):
    h, m, s = (int(x) for x in start.split(":"))
    base = h * 3600 + m * 60 + s
    f_big, f_txt = font(46), font(64)
    for i in range(int(total * FPS)):
        t = i / FPS
        img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        sec = int(base + t) % 86400
        stamp = f"{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}"
        d.text((40, 60), f"{cam}  {stamp}", font=f_big, fill=(235, 255, 235, 235))
        if int(t * 2) % 2 == 0:
            d.ellipse((W - 150, 70, W - 120, 100), fill=(255, 40, 40, 235))
        d.text((W - 105, 62), "REC", font=f_big, fill=(235, 255, 235, 235))
        if text and text_from <= t <= text_to:
            w = d.textlength(text, font=f_txt)
            d.text(((W - w) / 2, H - 300), text, font=f_txt, fill=(235, 255, 235, 240),
                   stroke_width=4, stroke_fill=(0, 0, 0, 255))
        yield img.tobytes()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("src"); p.add_argument("dst")
    p.add_argument("--start", default="03:17:42", help="hora inicial del timestamp")
    p.add_argument("--cam", default="CAM 02")
    p.add_argument("--text", default="", help="texto minimo en pantalla")
    p.add_argument("--text-from", type=float, default=0.5)
    p.add_argument("--text-to", type=float, default=3.5)
    p.add_argument("--loops", type=int, default=2, help="veces que se repite el clip")
    p.add_argument("--audio", help="audio propio (grillos, golpes) para mezclar")
    a = p.parse_args()

    clip = duration(a.src)
    total = clip * a.loops
    grade = (f"fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
             "hue=s=0,eq=contrast=1.25:brightness=-0.03:gamma=1.15,"
             "colorchannelmixer=rr=0.55:gg=1.0:bb=0.55,"
             "noise=alls=22:allf=t+u,vignette=PI/4.5[v0];"
             "[v0][1:v]overlay=0:0:format=auto[v]")
    hiss = "anoisesrc=color=pink:amplitude=0.05:sample_rate=44100"
    crickets = ("aevalsrc='0.06*sin(2*PI*4300*t)*gt(mod(t,0.33),0.15)*(0.6+0.4*sin(2*PI*35*t))':"
                "s=44100")
    audio_in = ["-i", a.audio] if a.audio else []
    n = 2
    amix = "[2:a][3:a]amix=inputs=2:normalize=0" if not a.audio else "[2:a][3:a][4:a]amix=inputs=3:normalize=0"
    cmd = [FFMPEG, "-y", "-stream_loop", str(a.loops - 1), "-i", a.src,
           "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-f", "lavfi", "-t", f"{total}", "-i", hiss,
           "-f", "lavfi", "-t", f"{total}", "-i", crickets, *audio_in,
           "-filter_complex", f"[0:v]{grade};{amix}[a]",
           "-map", "[v]", "-map", "[a]", "-t", f"{total}",
           "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", a.dst]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    try:
        for fr in overlay_frames(total, a.start, a.cam, a.text, a.text_from, a.text_to):
            proc.stdin.write(fr)
    except BrokenPipeError:
        pass
    proc.stdin.close()
    sys.exit(proc.wait())


if __name__ == "__main__":
    main()
