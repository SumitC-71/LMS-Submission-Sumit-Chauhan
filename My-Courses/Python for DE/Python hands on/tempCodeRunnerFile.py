like images
with open('photo.jpeg','rb') as rf:
    with open('binary_copy','wb') as wf:
        for line in rf:
            wf.write(