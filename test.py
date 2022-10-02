import googletrans
from googletrans import Translator

nd = googletrans.LANGUAGES
text1 = "안녕하세요"
translator = Translator()

for i in nd:
    trans1 = translator.translate(text1, src='ko', dest=i)
    print(f"{nd[i]} 인사말", trans1.text)
