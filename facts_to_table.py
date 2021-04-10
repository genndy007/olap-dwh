import pickle

from db_fill import insert_facts


facts = None
with open('facts.pickle', 'rb') as f:
    facts = pickle.load(f)


insert_facts(facts)
