plm='gpt-neo-1.3B'
dst='dialogsum'
setting='5shot'
mode='num_name_topic'

input_path='{}_{}_chain_{}_{}.txt'.format(plm, dst,setting,str(mode))
output_path='{}_chain_{}_{}.txt'.format(plm,setting,str(mode))

with open(input_path, 'r', encoding='utf8') as f, open(output_path, 'w', encoding='utf8') as of:
    datas=f.readlines()

    for idx,data in enumerate(datas):
        if 'Generated:' in datas[idx]:
            generated = datas[idx + 1].strip()
            try:
                if '[' in generated[0]:
                    generated=generated.split('[Dialogue]:')[1].strip()
                else:
                    generated = ''.join(generated.split('[Dialogue]:')[:1]).strip()
            except IndexError:
                generated=generated

            of.write(generated+'\n')
            of.flush()

