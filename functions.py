from constant import one_d,one_d_summary,dialogsum_one_d_summary,dialogsum_one_d,two_d_summary,two_d,three_d,three_d_summary, \
    four_d,four_d_summary, five_d,five_d_summary

from constant import sam_two_d,sam_two_d_summary,sam_three_d_summary,sam_three_d,sam_four_d_summary,sam_five_d_summary,sam_five_d,sam_four_d

def speaker_names(names):
    str=''
    for i in range(len(names)-1):
        str+=names[i]+' and '
    str+=names[-1]

    return str

def prompting(args,setting,line,mode,topic=None):
    utters=line.split('\n')
    speakers=[utter.split(":")[0] for utter in utters][1:]
    names=list(set(speakers))
    nums=len(names)
    if topic is not None:
        topic=topic.strip()
    data_path=args.data_path

    if 'dialogsum' in data_path:
        _d=dialogsum_one_d
        _d_summary=dialogsum_one_d_summary
        _names='#Person1# and #Person2#'
        _names2='#Person1# and #Person2# and #Person3#'
        _names3='#Person1# and #Person2# and #Person3# and #Person4#'
        _names4='#Person1# and #Person2# and #Person3# and #Person4# and #Person5#'
        _names5='#Person1# and #Person2# and #Person3# and #Person4# and #Person5# and #Person6#'
        _nums=2
        _topic='get a check-up'
        _topic2='have a dinner'
        _topic3='pay the fare'
        _topic4="dimission"
        _topic5='shopping'
        num_name_pre1 = '{}[Content]: There are {} speakers, {}. To summarize: {}'.format(_d, _nums, _names, _d_summary)
        num_name_pre2 = '{}[Content]: There are {} speakers, {}. To summarize: {}'.format(two_d, '3', _names2, two_d_summary)
        num_name_pre3 = '{}[Content]: There are {} speakers, {}. To summarize: {}'.format(three_d, '2', _names3,
                                                                                    three_d_summary)
        num_name_pre4 = '{}[Content]: There are {} speakers, {}. To summarize: {}'.format(four_d, '2', _names4,
                                                                                    four_d_summary)
        num_name_pre5 = '{}[Content]: There are {} speakers, {}. To summarize: {}'.format(five_d, '2', _names5,
                                                                                    five_d_summary)

        topic_pre1 = '{}[Content]: There are {} speakers, {}. The topic is "{}". To summarize: {}' \
            .format(_d, _nums, _names, _topic, _d_summary)
        topic_pre2 = '{}[Content]: There are {} speakers, {}. The topic is "{}". To summarize: {}'. \
            format(two_d, '3', _names2, _topic2, two_d_summary)
        topic_pre3 = '{}[Content]: There are {} speakers, {}. The topic is "{}". To summarize: {}'. \
            format(three_d, '2', _names3, _topic3, three_d_summary)
        topic_pre4 = '{}[Content]: There are {} speakers, {}. The topic is "{}". To summarize: {}'. \
            format(three_d, '2', _names4, _topic4, four_d_summary)
        topic_pre5 = '{}[Content]: There are {} speakers, {}. The topic is "{}". To summarize: {}'. \
            format(three_d, '2', _names5, _topic5, five_d_summary)

        only_topic_pre1 = '{}[Content]: The topic is "{}". To summarize: {}' \
            .format(_d, _topic, _d_summary)
        only_topic_pre2 = '{}[Content]: The topic is "{}". To summarize: {}'. \
            format(two_d, _topic2, two_d_summary)
        only_topic_pre3 = '{}[Content]: The topic is "{}". To summarize: {}'. \
            format(three_d, _topic3, three_d_summary)
        only_topic_pre4 = '{}[Content]: The topic is "{}". To summarize: {}'. \
            format(four_d, _topic4, four_d_summary)
        only_topic_pre5 = '{}[Content]: The topic is "{}". To summarize: {}'. \
            format(five_d, _topic5, five_d_summary)

        None_pre1 = '{}[Content]: To summarize: {}'.format(_d, _d_summary)
        None_pre2 = '{}[Content]: To summarize: {}'.format(two_d, two_d_summary)
        None_pre3 = '{}[Content]: To summarize: {}'.format(three_d, three_d_summary)
        None_pre4 = '{}[Content]: To summarize: {}'.format(four_d, four_d_summary)
        None_pre5 = '{}[Content]: To summarize: {}'.format(five_d, five_d_summary)


    elif 'samsum' in data_path:
        _d = one_d
        _d_summary = one_d_summary
        _names='Tim and Kim'
        _names2='Anita and Jenny'
        _names3='Elisa and Sadie and Alice and Carol and Arthur and Liam and Kai and Tom and John'
        _names4='Isabella and Oscar'
        _names5='Maria and Andrew'
        _nums=2
        _topic='pomodoro technique'
        _topic2='Bologna station'
        _topic3 = 'drink at Mombasa'
        _topic4 = 'bad mood'
        _topic5 = 'food and drinks'
        num_name_pre1 = '{}[Content]: There are {} speakers, {}. To summarize: {}'.format(_d, _nums, _names, _d_summary)
        num_name_pre2 = '{}[Content]: There are {} speakers, {}. To summarize: {}'.format(sam_two_d, '2', _names2, sam_two_d_summary)
        num_name_pre3 = '{}[Content]: There are {} speakers, {}. To summarize: {}'.format(sam_three_d, '9', _names3,
                                                                                    sam_three_d_summary)
        num_name_pre4 = '{}[Content]: There are {} speakers, {}. To summarize: {}'.format(sam_four_d, '2', _names4,
                                                                                    sam_four_d_summary)
        num_name_pre5 = '{}[Content]: There are {} speakers, {}. To summarize: {}'.format(sam_five_d, '2', _names5,
                                                                                    sam_five_d_summary)
        None_pre1='{}[Content]: To summarize: {}'.format(_d, _d_summary)
        None_pre2 ='{}[Content]: To summarize: {}'.format(sam_two_d, sam_two_d_summary)
        None_pre3='{}[Content]: To summarize: {}'.format(sam_three_d, sam_three_d_summary)
        None_pre4 ='{}[Content]: To summarize: {}'.format(sam_four_d, sam_four_d_summary)
        None_pre5='{}[Content]: To summarize: {}'.format(sam_five_d, sam_five_d_summary)

        topic_pre1 = '{}[Content]: There are {} speakers, {}. The topic is "{}". To summarize: {}' \
            .format(_d, _nums, _names, _topic, _d_summary)
        topic_pre2 = '{}[Content]: There are {} speakers, {}. The topic is "{}". To summarize: {}'. \
            format(sam_two_d, '2', _names2, _topic2, sam_two_d_summary)
        topic_pre3 = '{}[Content]: There are {} speakers, {}. The topic is "{}". To summarize: {}'. \
            format(sam_three_d, '9', _names3, _topic3, sam_three_d_summary)
        topic_pre4 = '{}[Content]: There are {} speakers, {}. The topic is "{}". To summarize: {}'. \
            format(sam_four_d, '2', _names4, _topic4, sam_four_d_summary)
        topic_pre5 = '{}[Content]: There are {} speakers, {}. The topic is "{}". To summarize: {}'. \
            format(sam_five_d, '2', _names5, _topic5, sam_five_d_summary)



    post="[Content]: "
    if setting=='zero-shot':
        if mode=='None':
            prefix = 'Summarize the dialogue:'
            postfix = ""
        if mode=="name":
            prefix ='Speakers are {}. Summarize the dialogue into a statement:\n\n'.format(speaker_names(names))
            postfix=""
        elif mode=='num':
            prefix = 'There are {} speakers. Summarize the dialogue into a statement:\n\n'.format(nums)
            postfix = ""
        elif mode == 'num_name':
            prefix = 'There are {} speakers, {}. Summarize the dialogue into a statement:\n\n'.format(nums,speaker_names(names))
            postfix = ""
        elif mode =='topic':
            prefix = 'The topic of the dialogue is {}. Summarize the dialogue into a statement:\n\n'.\
                format(topic)
            postfix = ""
        elif mode =='name_topic':
            prefix = 'Speakers are {}. The topic of the dialogue is {}. Summarize the dialogue into a statement:\n\n'. \
                format(speaker_names(names),topic)
            postfix = ""
        elif mode =='num_topic':
            prefix = 'There are {} speakers. The topic of the dialogue is {}. Summarize the dialogue into a statement:\n\n'. \
                format(nums, topic)
            postfix = ""
        elif mode =='num_name_topic':
            prefix = 'There are {} speakers, {}. The topic of the dialogue is {}. Summarize the dialogue:\n\n'. \
                format(nums, speaker_names(names),topic)
            postfix = ""

    elif setting == '1shot':
        if mode == 'None':
            prefix = '{}[Content]: To summarize: {}'.format(_d,_d_summary)
            postfix = post+' To summarize: '

        if mode == 'num':
            prefix = '{}[Content]: There are {} speakers. To summarize: {}'.format(_d,_nums,_d_summary)
            postfix = post+'There are {} speakers. To summarize: '.format(nums)

        elif mode == 'name':
            prefix = '{}[Content]: Speakers are {}. To summarize: {}'.format(_d,_names,_d_summary)
            postfix =post+'Speakers are ' + speaker_names(names)+'. To summarize: '

        elif mode == 'num_name':
            prefix = '{}[Content]: There are {} speakers, {}. To summarize: {}'.format(_d,_nums,_names,_d_summary)
            postfix = post + 'There are {} speakers, {}. To summarize: '.format(nums,speaker_names(names))

        elif mode == 'topic':
            prefix = '{}[Content]: The topic is "{}". To summarize: {}'.format(_d,_topic,_d_summary)
            postfix =post + 'The topic is "{}". To summarize: '.format(topic)

        elif mode == 'num_topic':
            prefix = '{}[Content]: There are {} speakers, The topic is "{}". To summarize: {}' .format(_d,_nums,_topic,_d_summary)
            postfix =post + 'There are {} speakers, The topic is "{}". To summarize: '.format(nums, topic)

        elif mode == 'name_topic':
            prefix = '{}[Content]: Speakers are {}, The topic is "{}". To summarize: {}'.format(_d,_names,_topic,_d_summary)
            postfix= post+'Speakers are {}, The topic is "{}". To summarize: '.format(speaker_names(names),topic)

        elif mode == 'num_name_topic':
            prefix = '{}[Content]: There are {} speakers, {}. The topic is "{}". To summarize: {}' .format(_d,_nums,_names,_topic,_d_summary)
            postfix = post + 'There are {} speakers, {}. The topic is "{}". To summarize: '.\
                format(nums, speaker_names(names),topic)

    elif setting== '2shot':
        if mode == 'None':
            prefix = None_pre1 + None_pre2
            postfix ='To summarize: '
        if mode == 'num_name':
            prefix=num_name_pre1+num_name_pre2
            postfix = post + 'There are {} speakers, {}. To summarize: '.format(nums, speaker_names(names))
        elif mode == 'num_name_topic':
            prefix = topic_pre1+topic_pre2
            postfix = post + 'There are {} speakers, {}. The topic is "{}". To summarize: '.\
                format(nums, speaker_names(names),topic)

    elif setting== '3shot':
        if mode=='None':
            prefix = None_pre1 + None_pre2 + None_pre3
            postfix = 'To summarize: '
        if mode == 'num_name':
            prefix=num_name_pre1+num_name_pre2+num_name_pre3
            postfix = post + 'There are {} speakers, {}. To summarize: '.format(nums, speaker_names(names))
        elif mode == 'num_name_topic':

            prefix = topic_pre1+topic_pre2+topic_pre3
            postfix = post + 'There are {} speakers, {}. The topic is "{}". To summarize: '.\
                format(nums, speaker_names(names),topic)

    elif setting== '4shot':
        if mode == 'None':
            prefix = None_pre1 + None_pre2 + None_pre3+None_pre4
            postfix = post + ' To summarize: '
        if mode == 'num_name':
            prefix=num_name_pre1+num_name_pre2+num_name_pre3+num_name_pre4
            postfix = post + 'There are {} speakers, {}. To summarize: '.format(nums, speaker_names(names))
        elif mode == 'num_name_topic':
            prefix = topic_pre1+topic_pre2+topic_pre3+topic_pre4
            postfix = post + 'There are {} speakers, {}. The topic is "{}". To summarize: '.\
                format(nums, speaker_names(names),topic)

    elif setting== '5shot':
        if mode == 'None':
            prefix=None_pre1+None_pre2+None_pre3+None_pre4+None_pre5
            postfix = post + ' To summarize: '
        if mode == 'num_name':
            prefix=num_name_pre1+num_name_pre2+num_name_pre3+num_name_pre4+num_name_pre5
            postfix = post + 'There are {} speakers, {}. To summarize: '.format(nums, speaker_names(names))
        elif mode == 'num_name_topic':
            prefix = topic_pre1+topic_pre2+topic_pre3+topic_pre4+topic_pre5
            postfix = post + 'There are {} speakers, {}. The topic is "{}". To summarize: '.\
                format(nums, speaker_names(names),topic)
        elif mode =='topic':
            prefix = only_topic_pre1 + only_topic_pre2 + only_topic_pre3 + only_topic_pre4 + only_topic_pre5
            postfix = post + 'The topic is "{}". To summarize: '. \
                format(topic)

    return prefix, postfix