import random
from collections import OrderedDict


def shuffle_vocabulary(d):
    keys = list(d.keys())
    random.shuffle(keys)
    return OrderedDict([(k, d[k]) for k in keys])


def translate_test(vocabulary):
    correct_words = 0
    incorrect_words = 0

    vocabulary = shuffle_vocabulary(vocabulary)

    for word in vocabulary:
        print("Translate word -", word)
        printed_word = input("> ")
        if printed_word == vocabulary[word]:
            print("Correct!")
            correct_words += 1
        else:
            print("Incorrect! The correct answer is -", vocabulary[word])
            incorrect_words += 1

    print("------------------------------------------")
    print("Number of Correct words:", correct_words)
    print("Number of Incorrect words:", incorrect_words)


print("Welcome to vocabulary!")
print("Let's start discovering words that you've been learned:")

english = \
    (
        "solicitously", "imprudently", "having heard",
        "keen to", "to commit", "to assert", "mare",
        "demand & supply", "block", "horse-dealer by trade",
        "went off", "vesper", "certain",
        "approval", "generally", "basically",
        "free-time activities", "follow-up questions",
        "self-affirmation", "rehearsal", "take a seat",
        "to stir", "necessarily", "urgently", "role model",
        "commercial", "fashion", "youth", "acceptance", "peer",
        "tedious", "scruffy", "sustainable", "blissful",
        "squint", "to squint", "conventional", "to aspire",
        "bleak", "to captivate", "to prevent", "terrible",
        "post office", "record shop", "to shook", "fortitude",
        "entrepreneur", "despair", "to despair", "desperate",
        "to languish", "preoccupation", "leisure"
    )
russian = \
    (
        "заботливо", "неосторожно", "услышав", "стремиться к",
        "фиксировать", "утвердить", "кобыла", "спрос и предложение",
        "квартал", "торговец лошадьми по профессии", "ушёл",
        "вечерняя звезда", "определённый", "одобрение", "в общем",
        "в основном", "занятия в свободное время", "вопросы вдогонку",
        "самоутверждение", "репетиция", "займи место",
        "жарить в раскалённом масле", "обязательно", "срочно",
        "образец для подражания", "реклама", "мода", "молодость",
        "принятие", "равный", "утомительный", "неопрятный",
        "устойчивый", "блаженный", "косоглазие", "щуриться",
        "обычный", "стремиться", "мрачный", "очаровывать",
        "предотвращать", "ужасный", "почтамт", "музыкальный магазин",
        "встряхнул", "сила духа", "предприниматель", "отчаяние",
        "отчаиваться", "отчаянный", "томиться", "озабоченность",
        "досуг"
    )

print("Choose [E]nglish / [R]ussian language mode:")
lang_mode = input("> ")

if lang_mode.upper() == "E" or lang_mode.upper() == "ENGLISH" or lang_mode.upper() == "ENG":
    print("English mode!")
    translate_test(dict(zip(english, russian)))
elif lang_mode.upper() == "R" or lang_mode.upper() == "RUSSIAN" or lang_mode.upper() == "RUS":
    print("Russian mode!")
    translate_test(dict(zip(russian, english)))
else:
    print("Incorrect input!")
    exit(1)


# ToDo: randomize words while loop --------- COMPLETED!
# ToDo: add possibility of choosing language mode (ENG -> RUS, RUS -> ENG) --------- COMPLETED!
# ToDo: add check of misspelling and predicting closest variants for possible correct answers
