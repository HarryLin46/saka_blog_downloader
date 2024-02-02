import json
import requests

##load member's image
def load_member_image(data_list):
    for member in data_list["data"]:
        print(member["name"],member["img"],"\n")
        image_url = member["img"]

        # send HTTP GET request to image's URL
        response = requests.get(image_url)

        # check if request is success
        if response.status_code == 200:

            image_path = f"member/nogi/{member["name"]}.jpg"
            # write the data into the file
            with open(image_path, "wb") as file:
                file.write(response.content)

def prepare_member_list(data_list):
    with open('member/nogi/member_list.txt', 'w', encoding='utf-8') as file:
        for member in data_list["data"]:
            if member["graduation"]=="NO" and not member["name"]=="乃木坂46": #乃木坂46 is don't care
                file.write(member["name"]+"\n")

def update_nogi():
    #update member source
    url = "https://www.nogizaka46.com/s/n46/api/list/member?so=AB"

    #send request
    response = requests.get(url)
    # if response.status_code == 200:
    #     html = response.text
    #     with open('member/nogi/member_source_nogi.txt', 'w', encoding='utf-8') as file:
    #         file.write(html)
    #     # print(html)
    # else:
    #     print("get member source faild，error code：", response.status_code)

    # with open('member/nogi/member_source_nogi.txt', "r", encoding='utf-8') as f:
    #     text = f.read()
    html_txt = response.text
    raw_data = html_txt[html_txt.find('{'):html_txt.rfind('}')+1]
    data_list = json.loads(raw_data)
    load_member_image(data_list)
    prepare_member_list(data_list)

if __name__ == '__main__':
    update_nogi()

    



