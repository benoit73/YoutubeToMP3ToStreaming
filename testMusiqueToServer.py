import ffmpeg
import configparser

def main():
    config = charger_configuration()
    input_audio_path = config['DEFAULT']['input_audio_path']
    rtmp_url = config['DEFAULT']['rtmp_url']
    print(rtmp_url)
    print(input_audio_path)
    stream_audio_to_rtmp(input_audio_path, rtmp_url)
def charger_configuration():
    config = configparser.ConfigParser()
    config.read('testconfig.ini')  # Assurez-vous que le chemin vers config.ini est correct
    return config

def stream_audio_to_rtmp(input_audio_path, rtmp_url):
    stream = (
        ffmpeg
        .input(input_audio_path)
        .output(rtmp_url, format='flv', acodec='aac', audio_bitrate='128k', ar='44100')
        .global_args('-loglevel', 'quiet')
        .run_async(pipe_stdin=True)
    )
    stream.wait()


if __name__ == "__main__":
    main()
