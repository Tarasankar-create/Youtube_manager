import json


def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
def save_data(videos):
    with open('youtube.txt','w') as file: 
        json.dump(videos,file)

def list_videos(videos):
    print("==========================================")
    print("   Name".ljust(13),'|'.ljust(10),"Link".ljust(15),'|'.ljust(5),'Duration(Hours)'.ljust(7))
    print("-"*70)
    for i,value in enumerate(videos):
        print(f"{i+1}. {value['name']:<15} {value['link'][:15]+'...' if len(value['link'])>15 else value['link']:<18} {value['time']:>15} ")
    print("==========================================")
    
def add_videos(videos):
    name=input("Enter video name : ")
    link=input("Enter video link : ")
    length=int(input("Enter video length : "))
    videos.append({'name': name, 'link': link, 'time': length})
    save_data(videos)
def update_videos(videos):
    list_videos(videos)
    choice=int(input("Enter the video number : "))
    if 1<=choice<=len(videos):
        print(" What do you want to update ? ")
        print("1. Video Name")
        print("2. Video Link")
        print("3. Video Duration")
        print("4. All")
        print("5. Exit")
        option=int(input("Enter your option : "))
        match option:
            case 1:
                updated_name=input("Enter video name : ")
                videos[choice-1]={'name': updated_name, 'link':videos[choice-1]['link'], 'time':videos[choice-1]['time']}
                save_data(videos)
                print("--------------------")
                print("|","Video updated".rjust(10).ljust(10),"|")
                print("--------------------")
            case 2:
                updated_link=input("Enter video link : ")
                videos[choice-1]={'name':videos[choice-1]['name'], 'link':updated_link, 'time':videos[choice-1]['time']}
                save_data(videos)
                print("--------------------")
                print("|","Video updated".rjust(10).ljust(10),"|")
                print("--------------------")
            case 3:
                updated_time=int(input("Enter video duration : "))
                videos[choice-1]={'name':videos[choice-1]['name'], 'link':videos[choice-1]['link'], 'time':updated_time}
                save_data(videos)
                print("--------------------")
                print("|","Video updated".rjust(10).ljust(10),"|")
                print("--------------------")
            case 4:
                updated_name=input("Enter video name : ")
                updated_link=input("Enter video link : ")
                updated_time=int(input("Enter video duration : "))
                videos[choice-1]={'name': updated_name, 'link':updated_link, 'time':updated_time}
                save_data(videos)
                print("--------------------")
                print("|","Video updated".rjust(10).ljust(10),"|")
                print("--------------------")
            case 5:
                return
            case _:
                print("--------------------")
                print("|","Invalid option!".rjust(10).ljust(10),"|")
                print("--------------------")
                return
    else:
        print("|","Please enter a valid number".rjust(10).ljust(10),"|")
def delete_videos(videos):
    list_videos(videos)
    index=int(input("Choose the number you want to delete : "))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data(videos)
        print("--------------------")
        print("|","Video deleted".rjust(10).ljust(10),"|")
        print("--------------------")
    else:
        print("--------------------")
        print("|","Invalid input!".rjust(10).ljust(10),"|")
        print("--------------------")
        return
def main():
    print("|>>>--- Welcome to Youtube manager ---<<<| ")
    videos=load_data()
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
                print("--------------------")
                print("|","Please enter a valid option".rjust(10).ljust(10),"|")
                print("--------------------")

if __name__=="__main__":
    main()