from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine, exists, and_
from sqlalchemy.orm import relationship, sessionmaker

#  Connection
keys = {
    'DBMS': 'postgresql',
    'driver': 'pg8000',
    'user_name': 'postgres',
    'password': '123456',
    'ip': '192.168.2.112',
    'port': '5432',
    'db_name': 'TranslationView'
}

engine = create_engine(
    "{0}+{1}://{2}:{3}@{4}:{5}/{6}".format(
        keys['DBMS'], keys['driver'],
        keys['user_name'], keys['password'],
        keys['ip'], keys['port'], keys['db_name']
    ),
    client_encoding='utf8',
    echo=False
)

# Mapping
Base = declarative_base()

# class User(Base):
#     __tablename__ = 'user'
#
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     password = Column(String)
#
#
# class Vocabulary(Base):
#     __tablename__ = 'vocabulary'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     fullname = Column(String)
#     nickname = Column(String)
#     word1 = Column()
#     word2 = Column()


class Translation(Base):
    __tablename__ = 'translation'

    id = Column(Integer, primary_key=True)
    word1_id = Column(Integer, ForeignKey('word.id'))
    word2_id = Column(Integer, ForeignKey('word.id'))

    word1 = relationship("Word", foreign_keys="Translation.word1_id")
    word2 = relationship("Word", foreign_keys="Translation.word2_id")

    def __repr__(self):
        return "<Translation(word1='%s', word2='%s' lang1='%s' lang2='%s')>" % (
            self.word1.value, self.word2.value, self.word1.language.value, self.word2.language.value)


class Word(Base):
    __tablename__ = 'word'

    id = Column(Integer, primary_key=True)
    value = Column(String)

    language_id = Column(Integer, ForeignKey('language.id'))
    language = relationship("Language", back_populates="word")


class Language(Base):
    __tablename__ = 'language'

    id = Column(Integer, primary_key=True)
    value = Column(String)

    word = relationship("Word", back_populates="language")


Base.metadata.create_all(engine)


# if not exist
# def get_or_create(session, model, defaults=None, **kwargs):
#     instance = session.query(model).filter_by(**kwargs).first()
#     if instance:
#         return instance, False
#     else:
#         params = dict((k, v) for k, v in kwargs.iteritems() if not isinstance(v, ClauseElement))
#         params.update(defaults or {})
#         instance = model(**params)
#         session.add(instance)
#         return instance, True

# Session creation

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
session.query(Translation).all()
session.commit()


def add_lang():
    lang = input("Enter language = ")
    session.add(Language(value=lang))
    session.commit()
    return session.query(Language).filter(Language.value == lang).first()


def select_lang(all_result, curent):
    return session.query(Language).filter(Language.value == all_result[curent][0]).first()


def input_lang_in(diapson, msg):
    num = int(input(msg))
    if 0 <= num < diapson:
        return num
    else:
        return input_lang_in(diapson=diapson, msg=msg)


def show_languages():
    s = session.query(Language.value).all()
    if len(s):
        print("You can enable next languages:")
        for i in range(len(s)):
            print(i, s[i][0])
        msg1 = input("Do you want add new language? [Y]es [N]o\n")
        if msg1.upper() == "Y":
            print("Input Yes")
            add_lang()
            return show_languages()
        elif msg1.upper() == "N":
            print("Input No")
            print("Select two languages via number. This languages is your language and language who you want to learn")
            lang1 = select_lang(s, input_lang_in(diapson=len(s), msg="Your current: "))
            lang2 = select_lang(s, input_lang_in(diapson=len(s), msg="You learn: "))
            if lang1 == lang2:
                print("You can not learn current language")
                return show_languages()
            return [lang1, lang2]
        else:
            print("Bad input")
            return show_languages()
    else:
        print("No languages")
        add_lang()
        return show_languages()


def show_word_actions(cur_lang, lrn_lang):
    all_words = session.query(Word).filter(Word.language == current_lang).\
        all()
    if len(all_words):
        for word in all_words:
            print(word.value, word.language.value)
    else:
        print("No words")
    print("Your native is {0}\nYou learn {1}\n".format(cur_lang.value, lrn_lang.value))
    command = input("Input menu (input number):\n"
                    "1 - Add 1 word (word - translation)\n"
                    "2 - Add words with cascade (words - translations\n"
                    "3 - Delete word (experemental)\n"
                    "4 - Show all translation\n"
                    "0 - To close program\n")
    if command == '1':
        print(add_translation(cur_lang, lrn_lang))
    elif command == '0':
        return 0
    show_word_actions(cur_lang, lrn_lang)


def show_translations():
    pass


def add_translation(cur_lang, lrn_lang):
    word_current = add_word(cur_lang)
    word_learned = add_word(lrn_lang)
    created_translation = Translation(word1=word_current, word2=word_learned)
    translation = session.query(Translation).\
        filter(Translation.word1_id == word_current.id, Translation.word2_id == word_learned.id).\
        first()
    if not translation:
        session.add(created_translation)
        session.commit()
        translation = created_translation
    return translation


def add_word(language):
    value = input("Language {0} of next word is ".format(language.value))
    # this value in db?
    word_in_db = session.query(Word).filter(Word.value == value, Word.language == language).first()
    if word_in_db:
        word = word_in_db
    else:
        word = Word(value=value, language=language)
        session.add(word)
        print("Word '{0}' add".format(value))
    session.commit()
    return word


def add_words():
    pass


languages = show_languages()
current_lang = languages[0]
learn_lang = languages[1]
show_word_actions(cur_lang=current_lang, lrn_lang=learn_lang)


# word1 = Word(value="get", language=current_lang)
# word2 = Word(value="взять", language=learn_lang)
# my_translation = Translation(word1=word1, word2=word2)
# print(my_translation)
# s = session.query(Translation).all()
# for i in s:
#     print(s)
#session.add(my_translation)
# session.commit()
