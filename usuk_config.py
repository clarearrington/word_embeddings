#%%
from base_wv import main, make_config

def get_us_uk_targets(path, get_us=False, get_uk=False):
    targets = []
    ## Get dissimilar
    with open(f'{path}/dissimilar.txt') as fin:
        dis = fin.read().split()
        targets.extend(dis)

    ## Get similar
    with open(f'{path}/similar.txt') as fin:
        sim = fin.read().strip()
        for pair in sim.split('\n'):
            uk_word, us_word = pair.split()
            if get_us:
                targets.append(us_word)
            elif get_uk:
                targets.append(uk_word)

    return targets

dataset = "us_uk"
corpus_name = "coca"
run = "sense"
data_path = '/data/arrinj'

## TODO: can I do something about this?
## I should just filter it out myself for other words I think
## Min_word_count: 100 BNC, 300 COCA
min_count = 50
vector_size = 100
load_data = True
save_data = False

if corpus_name == 'bnc':
    targets = get_us_uk_targets(f'{data_path}/corpus_data/us_uk/truth', get_uk=True)
elif corpus_name == 'coca':
    targets = get_us_uk_targets(f'{data_path}/corpus_data/us_uk/truth', get_us=True)

config = config = make_config(
        dataset, corpus_name, run, min_count, 
        vector_size, targets, load_data, save_data, data_path)

main(config)

#%%