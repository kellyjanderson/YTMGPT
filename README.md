# ChatGPT Playlist Assistant

Hello, music lovers and coders alike! 👋🎶

Are you tired of the endless copy-and-paste marathon just to curate your dream playlist? Worried about developing a "Repetitive Stress Injury" from all that clicking and typing? (Okay, that might be a stretch, but you get the point!) Well, you've come to the right place! This script was inspired by my own lazy... I mean, efficient... desires to build YouTube playlists using the wondrous powers of ChatGPT, minus the carpal tunnel.

This script is designed to streamline the creation of YouTube playlists with a little help from our friend, ChatGPT. Instead of manually copying and pasting song IDs like a 19th-century telegraph operator, why not let this handy tool do the heavy lifting?

### Features

- Update YouTube Playlists with minimal manual effort.
- Avoid unnecessary strain on your delicate, human hands.
- Impress your friends with your impeccable music taste (and your coding skills).

## Sample Prompts for ChatGPT

Here is a sample prompt that will cause ChatGPT to generate a list of songs and a comma-separated list 

> List ten songs about a sunny day as a numbered list. Then get me YouTube music IDs for those songs and print them as a comma-separated list in a code block so they can be easily copied.

Once ChatGPT provides the list, it will be in a code block format, making it easy for you to copy and paste directly into the script:

## Requirements

Before you dive in, make sure you've got:

- Python installed on your machine (preferably Python 3.8+).
- A virtual environment up and running (to keep things clean).
    ```shell
    python -m venv .venv
    source .venv/bin/activate
    ```
- The `ytmusicapi` library is installed within that environment.
    ```shell
    pip install ytmusicapi
    ```
- The download or clone the project.
    ```shell
    git clone https://github.com/kellyjanderson/YTMGPT.git
    ```    
- Make playlist,py executable
    ```shell
    chmod +x playlist.py
    ```    
- Update the shebang in playlsit.py to point at your python interpreter
    ```shell
    sed -i '' '1s|.*|#!'"$(pwd)"'/.venv/bin/python|' your_script.py
    ```
- Optionally add the project directory to your path
> bash:
    ```shell
    echo 'export PATH="./:$PATH"' >> ~/.bashrc
    ```
> zsh:
    ```shell
    echo 'export PATH="./:$PATH"' >> ~/.zshrc
    ```
- A love for music.
    ```bash
    🎶💞
    ```

## Usage
    ```shell
    playlist.py
    # when run without parameters it runs interactively which makes it easy to paste the list into the script.

    playlist.py <playlistID> <path>

    # Parameters:
    # <playlistID>: The YouTube Music playlist ID.
    # <path>: The path to a file containing a comma-separated list of YouTube Music video IDs.

    # Example:
    playlist.py PL12345abcdefg /path/to/video_ids.txt
    ```
## Contributing

In the spirit of music, which brings people together, we're committed to creating a welcoming and inclusive environment in this project. Here's our anthem:

- **Respect and Kindness**: We support and respect all individuals, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

- **No Bullying or Harassment**: Bullying, harassment, and other forms of aggression are not tolerated here. Let's build each other up, not tear each other down.

- **Be Excellent to Each Other**: Be thoughtful, be helpful, and be cool.

### Making Contributions

If you've got ideas on how to improve this script or add new features, we'd love to hear from you! Here's how you can contribute:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a new Pull Request.

Let's make the internet a better place, one playlist at a time. 🎉

