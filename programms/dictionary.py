#dictionary
nick_names={'ranjan':'stha',
            'abhay':'mundhe',
            'anurag':'nia',
            'atharva':'chiatra',
            'rahul':'hoge',
            'raaj':'chota doctor',}

def nicknames(name):
    name=name.lower()
    nick=''
    for friend in name:
        nick += nick_names[friend] +''
    return nick

nick_name_of_friend =input('enter the name of whose you want to know the nick name of ')
friend=nicknames(name)
print(friend)
