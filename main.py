"""
Terminal tool for downloading YouTube video

Required Library / Packages :
    pytubefix
    moviepy
"""

from download import Download

print("""
1.) Download YouTube Video from URL
2.) View Downloaded Video
3.) Change Download Destination
4.) Get Download Destination""")

youtube = Download()


while True:
    action = input("\nPerform action (1~4) : ").strip().lower()
    
    if action == "1":
        
        while True:
            url = input("URL <high_quality? Y/n> (press Enter to quit) : ").strip()
            
            if url in ["", "q", "quit", "exit"]:
                break
                
            high_quality = True
            
            if len(url.split(" ")) > 1:
                
                if url.split(" ")[-1].lower() == "n":
                    high_quality = False
                    
            youtube.url(url, high_quality)
    
    elif action == "2":
        youtube.view()
        
    elif action == "3":
        new_path = input("New download destination : ")
        youtube.path = new_path
        print(f"Download destination changed to {youtube.path}")
    
    elif action == "4":
        print(youtube.path)
        
    elif action in ["q", "quit", "exit"]:
        break
        
    else:
        print("Invalid input. Must be integer from 1 to 4")
        print("Enter q to terminate this program")
        
