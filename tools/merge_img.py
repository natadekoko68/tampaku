from PIL import Image


def merge_img(input_path_pic1, input_path_pic2,output_name):
    output_path = "/Users/kotaro/PycharmProjects/tampaku/output/"

    im = Image.open(input_path_pic1)
    im2 = Image.open(input_path_pic2)


    dst = Image.new("RGB", (im.width + im2.width, im.height))
    dst.paste(im, (0, 0))
    dst.paste(im2, (im.width, 0))
    dst.save("/Users/kotaro/Desktop/"+output_name+".jpg")
    dst.save(output_path+output_name+".jpg")

if __name__ == "__main__":
    input_path_pic1 = "/Users/kotaro/Desktop/培養_数式_samplenum.jpg"
    input_path_pic2 = "/Users/kotaro/Desktop/培養_数式_oneplate.jpg"
    output_name = "graphs"
    merge_img(input_path_pic1, input_path_pic2, output_name)
