from tkinter import *
from tkvideo import tkvideo
from tkinter.messagebox import showinfo
from gtts import gTTS
import speech_recognition as sr
import os
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

root = Tk()
root.title("Avatar Model")
root.iconbitmap('Logos\white\icons8-sign-language-100.ico')

ask = Label(root, text="Enter any of the following only:\n\n1)A-Z letters\n"
                       "2) Basic Interaction- Please, Excuse Me, Bye, No, Yes, Sorry, Thank You, Welcome\n"
                       "3)Greetings- Good morning, Good afternoon, Good evening, Good morning, Good night, Hello\n")
ask.pack()

e = Entry(root, width=50, borderwidth=5)
e.pack()


# current=e.get()
# val=str.lower(current)

def value():
    current = e.get()
    val = str.lower(current)
    if val == "a":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/a.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "b":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/b.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "c":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/c.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "d":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/d.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "e":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/e.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "f":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/f.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "g":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/g.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "h":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/h.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "i":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/i.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "j":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/j.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "k":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/k.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "l":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/l.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "m":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/m.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "n":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/n.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "o":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/o.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "p":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/p.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "q":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/q.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "r":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/r.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "s":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/s.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "t":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/t.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "u":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/u.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "v":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/v.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "w":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/w.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "x":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/x.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "y":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/y.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "z":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Alphabets/z.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "bye":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Basic_Interaction/bye.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "excuse me":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Basic_Interaction/excuse me.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "no":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Basic_Interaction/no.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "please":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Basic_Interaction/please.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "sorry":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Basic_Interaction/sorry.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "thank you":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Basic_Interaction/thank you.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "welcome":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Basic_Interaction/welcome.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "yes":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Basic_Interaction/yes.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "good afternoon":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Greetings/good afternoon.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "good evening":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Greetings/good evening.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "good morning":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Greetings/good morning.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "good night":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Greetings/good night.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    if val == "hello":
        my_label = Label(root)
        my_label.pack()
        player = tkvideo("Animations\Greetings/hello.mp4", my_label, loop=1, size=(500, 300))
        player.play()
    my_label2 = Label(root, text="Please Press Exit Before Entering a New Input.")
    my_label2.pack()
    Exit = Button(root, text="Exit", command=quit, bg="red", fg="White")
    Exit.pack()


Enter = Button(root, text="Press to view the ISL sign", command=value,bg="green",fg="White")
Enter.pack()

def say(text1):
    language = 'en'
    speech = gTTS(text=text1, lang=language, slow=False)
    speech.save("text.mp3")
    os.system("start text.mp3")

def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:
                text = r.recognize_google(audio,language="en-IN")
            except:
                pass
            return text


def SpeechToText():
    speechtotextwindow = Toplevel(root)
    speechtotextwindow.title("Speech To Text Converter")
    speechtotextwindow.iconbitmap('Logos\white\icons8-sign-language-100.ico')
    text = Text(speechtotextwindow, font=12, height=3, width=30)
    text.pack()
    Head = Label(speechtotextwindow, text='Please Record your speech and paste it on the main input window')
    Head.pack()
    recordbutton = Button(speechtotextwindow, text='Record', bg='Pink',command=lambda: text.insert(END, recordvoice()))
    recordbutton.pack()

speechtotextbutton = Button(root, text='Speech To Text Converter', bg='Purple',fg="white", command=SpeechToText)
speechtotextbutton.pack()

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")


def preprocess(sentence):
    # Process the sentence with spaCy
    doc = nlp(sentence)

    # Remove stopwords, lemmatize, and convert to (subject-object-verb) structure
    processed_tokens = []
    for token in doc:
        # Remove stopwords and punctuation
        if token.text.lower() not in STOP_WORDS and not token.is_punct:
            # Lemmatize and convert to lower case
            processed_tokens.append(token.lemma_.lower())

    # Convert sentence to (subject-object-verb) structure
    svo_structure = []
    for token in doc:
        if token.dep_ in ["nsubj", "dobj", "pobj"]:  # Subject, object, and passive object
            svo_structure.append(token.lemma_.lower())
        elif token.dep_ == "ROOT":  # Verb
            svo_structure.append(token.lemma_.lower())

    # Return the processed sentence and its structure
    return " ".join(processed_tokens), " ".join(svo_structure)


def rearrange_sentence():
    input_sentence = entry.get()
    processed_sentence, svo_structure = preprocess(input_sentence)
    output_label.config(
        text=f"Processed Sentence: {processed_sentence}\nISL Sentence: {svo_structure}")


def rearrange():
    # Create a Tkinter window
    sentence_rearrange = Toplevel(root)
    sentence_rearrange.title("English to ISL sentence Converter")
    sentence_rearrange.iconbitmap('Logos\white\icons8-sign-language-100.ico')

    # Create input field
    global entry
    entry = Entry(sentence_rearrange, width=50)
    entry.pack(pady=10)

    # Create button to process input
    process_button = Button(sentence_rearrange, text="Process", bg="Yellow", command=rearrange_sentence)
    process_button.pack()

    # Create label to display output
    global output_label
    output_label= Label(sentence_rearrange, text="")
    output_label.pack(pady=10)

EnglishToSignSentence = Button(root, text='English to ISL Sentence Converter', bg='cyan',fg="black", command=rearrange)
EnglishToSignSentence.pack()


root.mainloop()