from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Boolean
metadata = MetaData()
users = Table('users', metadata,
              Column('id_user', Integer, primary_key=True),
              Column('name', String),
              Column('password', String),
              )

vocabulary = Table('vocabulary', metadata,
                   Column('vocabulary_id', Integer, primary_key=True),
                   Column('user', None, ForeignKey('users.id_user')),
                   Column('translation', None, ForeignKey('translations.translation_id')),
                   Column('failed_inputs', Integer),
                   Column('inputs', Integer),
                   Column('is_learned', Boolean),
                   )

translations = Table('translations', metadata,
                     Column('translation_id', Integer, primary_key=True),
                     Column('word_lang1', None, ForeignKey('words.word_id')),
                     Column('word_lang2', None, ForeignKey('words.word_id')),
                     )

words = Table('words', metadata,
              Column('word_id', Integer, primary_key=True),
              Column('word', String),
              Column('language', None, ForeignKey('languages.language_id')),
              )

languages = Table('languages', metadata,
                  Column('language_id', Integer, primary_key=True),
                  Column('language_name', String),
                  )
# Column('counter_lang_1', Integer),
# Column('counter_lang_2', Integer),
# Column('name_lang_1', String, nullable=False),
# Column('name_lang_2', String, nullable=False),


def migrate(meta):
    from database.Core import engine
    meta.create_all(engine)


if __name__ == '__main__':
    migrate(metadata)
