def list_videos(videos):
    pass
def add_videos(videos):
    pass
def update_videos(videos):
    pass
def delete_videos(videos):
    pass
def main():
    videos=[]
    while True:
        print("1. List all videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit")
        choice=input("Enter your choice : ")

        match choice:
            case "1":
                list_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_videos(videos)
            case "4":
                delete_videos(videos)
            case "5":
                break
            case _:
                print("Please enter a valid option")

if __name__=="__main__":
    main()