import re


attrs = re.compile(r'id="tid\.(.+?)" .+? type="tweet" std_tech="(.+?)" std_ling="(.+?)">')
type_re = re.compile(r'type="(.+?)"')
ner = None
UPOS_MAPPER = {'Xa': 'SYM', 'Xh': 'SYM', 'Xe': 'SYM', 'Xf': 'X', 'X': 'X', 'Xw': 'SYM'}

with open('reldi-normtagner-hr.conllu', 'w') as out:
    for line in open('reldi-normtagner-hr.vert'):
        if line.startswith('<text'):
            tweet_id, t, l = attrs.search(line).groups()
            out.write("# newdoc id = {}\n".format(tweet_id))
            out.write("# T = {}\n".format(t[-1]))
            out.write("# L = {}\n".format(l[-1]))
            sid = 0
        elif line.startswith('<s>'):
            sid += 1
            tid = 0
            out.write('# sent_id = {}.{}\n'.format(tweet_id, sid))
            sent = []
        elif line.startswith('<name '):
            ner = type_re.search(line).group(1)
            first = True
        elif line.startswith('</name>'):
            ner = None
        elif line.startswith('<g/>'):
            sent[-1][-1].append('SpaceAfter=No')
        elif line.startswith('</s>'):
            text = ''
            for token in sent:
                text += token[0]
                if 'SpaceAfter=No' not in token[-1]:
                    text += ' '
            out.write('# text = {}\n'.format(text.strip()))
            tid = 0
            for token in sent:
                tid += 1
                if ' ' in token[1]:
                    tokens = token[-1][0][11:].split(' ')
                    lemmas = token[1].split(' ')
                    lemmas[0] = lemmas[0][:-2]
                    upos = token[2].split(' ')
                    msd = token[3].split(' ')
                    upos_feats = token[4].split(' ')
                    token[-1] = token[-1][1:]
                    if len(token[-1]) > 0:
                        out.write(str(tid)+'-'+str(tid+len(tokens)-1)+'\t'+token[0]+'\t_'*7+'\t'+'|'.join(token[-1])+'\n')
                    else:
                        out.write(str(tid)+'-'+str(tid+len(tokens)-1)+'\t'+token[0]+'\t_'*8+'\n')
                    if upos[0] == '_':
                        upos[0] = UPOS_MAPPER[msd[0]]
                    if upos[1] == '_':
                        upos[1] = UPOS_MAPPER[msd[1]]
                    for t, l, p, m, f in zip(tokens, lemmas, upos, msd, upos_feats):
                        out.write(str(tid)+'\t'+t+'\t'+l+'\t'+p+'\t'+m+'\t'+f+'\t_\t_\t_\t_\n')
                        tid += 1
                    tid -= 1
                    continue
                if len(token[-1]) > 0:
                    out.write(str(tid)+'\t'+'\t'.join(token[:5])+'\t_\t_\t_\t'+'|'.join(token[-1])+'\n')
                else:
                    out.write(str(tid)+'\t'+'\t'.join(token[:5])+'\t_\t_\t_\t_\n')
            out.write('\n')
        elif '\t' in line:
            token, norm, lemma, msd, msd_feats, upos, upos_feats, normed = line.split('\t')
            if upos == '_':
                upos = UPOS_MAPPER[msd]
            sent.append([token, lemma[:-2], upos, msd, upos_feats, []])
            if norm != token:
                sent[-1][-1].append('Normalized='+norm)
            if ner is not None:
                if first:
                    sent[-1][-1].append('NER=B-'+ner)
                    first = False
                else:
                    sent[-1][-1].append('NER=I-'+ner)
