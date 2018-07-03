import h5py, csv, pickle, codecs


h5f = h5py.File('data/parsed_data.h5', 'r')
inp = h5f['inputs']     # input sentences (indexed)
out = h5f['outputs']    # output sentences (indexed)
in_parses = h5f['input_parses']
out_parses = h5f['output_parses']
in_lens = h5f['in_lengths']

vocab, rev_vocab = pickle.load(open('data/parse_vocab.pkl', 'rb'))

fn = ['idx', 'tokens', 'parse']
ofile = codecs.open('data/generated_input.tsv', 'w', 'utf-8')
outfile = csv.DictWriter(ofile, delimiter='\t', fieldnames=fn)
outfile.writerow(dict((x,x) for x in fn))

for idx in range(16935839, 23306069):
    inp_tokens = inp[idx][:(in_lens[idx]-1)]
    inp_tokens = [rev_vocab[r] for r in inp_tokens]
    inp_sent = ' '.join(inp_tokens)
    in_p = in_parses[idx]
    
    outfile.writerow({'idx': idx, 'tokens':inp_sent, 'parse':in_p})
    
    if idx % 1000000 == 0:
        print(idx)
    
    