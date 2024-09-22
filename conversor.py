from moviepy.editor import VideoFileClip

caminho_original = 'teste.mov'

caminho_convertido = 'video_convertido.mp4'

clip = VideoFileClip(caminho_original)

clip.write_videofile(caminho_convertido, codec="libx264", audio_codec="aac")

clip.close()