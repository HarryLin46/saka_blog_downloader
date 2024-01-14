from PIL import Image
import io
import re
import sys
import tempfile

def resize_pictures(original_html): 
    # find all imgs
    img_tags = re.findall(r'<img src=[\'"](.*?)[\'"]', original_html)

    new_html = original_html
    for img_path in img_tags:
        # print(img_path)
        with Image.open(img_path) as img:
            # resize the img
            target_width = 896
            max_size = (target_width, target_width * 10)
            img.thumbnail(max_size, Image.Resampling.LANCZOS)

            # save the resized img as tempfile
            with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_img_file:
                img.save(temp_img_file, format='JPEG')
                temp_img_path = temp_img_file.name

                # change image pathsnin html
                new_html = new_html.replace(img_path, temp_img_path)

    return new_html

def modify_html_with_responsive_images(html_content): #unused
    max_width = "896px"
    # max_height = "200px"

    # 为每个 <img> 标签添加样式
    modified_html = re.sub(r'<img(.*?)src=[\'"](.*?)[\'"](.*?)>',
                           r'<img\1src="\2"\3 style="max-width: {}; max-height: {};">'.format(max_width, max_height),
                           html_content)
    return modified_html

def txt_to_html(file_path):
    html_content = ""

    with open(file_path, 'r', encoding='utf-8') as file:
        # max_width = "896px"
        for line in file:
            if line.strip().endswith(".jpg"):
                image_path = "blog_source/"+line.strip()
                # html_content += f"<img src='{image_path}' style=\"max-width: {max_width};\"><br>"
                html_content += f"<img src='{image_path}' /><br>"
            else:
                html_content += f"<p>{line.strip()}</p>"

    new_html_content = resize_pictures(html_content)
    return new_html_content




