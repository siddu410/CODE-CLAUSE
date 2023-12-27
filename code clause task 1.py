import pygame
import threading

def play_music(mp3_file):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()

def wait_for_input():
    input("Press Enter to stop the music...")
    pygame.mixer.music.stop()

# Create a playlist (list of song paths)
playlist = [
    "Carlos.mp3","Infraction.mp3","Enemy.mp3","Believer.mp3","Way-Down-We-Go.mp3","Under_The_Influence.mp3"
    # Add more songs as needed
]

while True:
    # Display the playlist
    print("\nPlaylist:")
    for index, song in enumerate(playlist, start=1):
        print(f"{index}. {song}")

    # Get user input for song selection or 'q' to quit
    user_input = input("Enter the number of the song to play (or 'q' to quit): ").lower()

    if user_input == 'q':
        break  # Exit the loop if the user enters 'q'

    try:
        selected_index = int(user_input) - 1
        selected_song = playlist[selected_index]

        # Create threads
        music_thread = threading.Thread(target=play_music, args=(selected_song,))
        input_thread = threading.Thread(target=wait_for_input)

        # Start threads
        music_thread.start()
        input_thread.start()

        print(f"Playing {selected_song}. Press Enter to stop.")
        
        # Wait for the input thread to finish before going to the next iteration
        input_thread.join()

    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number from the playlist.")
