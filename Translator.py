from googletrans import Translator
text=eval(input("Enter your text here"))
translator=Translator()
dt=translator.detect(text)
print("The input language is: ",dt)
dest=eval(input("Enter the destination language code")) #ex: english-'en',japanese-'ja',korean-'ko',french='fr' etc..,
translated=translator.translate(text,dest=dest)
print(translated.text)
