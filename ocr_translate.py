from textblob import TextBlob
import pytesseract
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
help="path to input image to be OCR'd")
ap.add_argument("-l", "--lang", type=str, default="es",
help="language to translate OCR'd text to (default is Spanish)")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# use Tesseract to OCR the image, then replace newline characters
# with a single space
text = pytesseract.image_to_string(rgb)
text = text.replace("\n", " ")
# show the original OCR'd text
print("ORIGINAL")
print("========")
print(text)
print("")

tb = TextBlob(text)
translated = tb.translate(to=args["lang"])
# show the translated text
print("TRANSLATED")
print("==========")
print(translated)