from PIL import Image, ImageDraw
import face_recognition

data = []
cnt = 1

for _, row in parent.iterrows():

    image = face_recognition.load_image_file(row['Image'])
    face_locations = face_recognition.face_locations(image)

    print('I found {} face(s) in this photograph.'.format(len(face_locations)))

    for face_location in face_locations:

        # Print the location of each face in this image
        top, right, bottom, left = face_location
        print('A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}'.format(top, left, bottom, right))

        # You can access the actual face itself like this:
        # face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(image)
        draw = ImageDraw.Draw(pil_image)
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0), width=3)

        file_name = 'D:\\Face_recognition\\Results\\FaceResult_{:02d}.jpg'.format(cnt)
        pil_image.save(file_name)
        cnt += 1

        del draw

        data.append({'Source image': row['Image'], 'Face found': file_name, 'Top': top, 'Left': left, 'Bottom': bottom, 'Right': right})

result = pandas.DataFrame.from_records(data)