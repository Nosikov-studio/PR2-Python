def image_info(d):
    i = d['image_id']
    t = d['image_title']
    try:
        s = f"Image {t} has id {i}"
    except:
        print("Error")
    else:
        return s


d1 = {'image_id': 108, 'image_title': 'my_cat'}
print(image_info(d1))
