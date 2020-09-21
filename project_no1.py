
next=True
while next==True:

    print('''
             1)Aquarious[Jan 20-Feb 18]
             2)Pisces[feb 19-march 20]
             3)Aries[march 21-april 19]
             4)Taurus [April 20 - May 20.]
             5)Gemini [May 21 - June 21]
             6)Cancer [June 22 - July 22]
             7)Leo [July 23 - Aug 22]
             8)Virgo [Aug. 23 - Sept 22]
             9)Libra [Sept. 23 - Oct 23]
             10)Scorpio [Oct. 24 - Nov 21]
             11)Sagittarius [Nov. 22 - Dec 21]
             12)Capricorn[dec 22-jan 19]''')

    ip=int(input('''enter num of your zodiac sign,if you do not know your sign you can see
    which column your birthdate lies  in:'''))
    if ip==1:
        print('''Aquarious:This might seem like a typical day early on, but as each hour goes by,
         you could start to see more and more mysterious actions and events cropping up. Who are
         the perpetrators? What are they up to!? If you look beneath the surface, you will start
         to see a pattern and an agenda. This is something exciting, and you should not ignore it.
         Try to get involved in their shenanigans and you will have a lot of fun. They could use a
          bright, witty person like you!''')
    elif ip==2:
        print('''Pisces: A relationship that you thought was broken beyond all repair still has some
         life in it. Figure out how you can put it on the road to recovery. There are two people
         involved in this messy situation, and each of you has your own apologies to make. Be a
         hero and be the first one to extend an olive branch. Call or e-mail them today. Let them
         know you're thinking about them and be honest about how you feel. Let down your guard and
         speak from the heart.''')
    elif ip==3:
        print('''Aries: Accidents are called accidents for a reason. They happen through no one
         person's concerted efforts. They just happen. If you are involved in a fender bender or
          any other type of collision (real or metaphorical), avoid taking it personally. Things
          happen, and every time you can let the stress roll off of your back, you grow and learn.
           Of course, if you are in a situation where you know someone is working against you, you
            should feel free to unsheath your claws.''')
    elif ip==4:
        print('''Taures:The art of flirtation takes a lot of time to learn, but you are becoming quite an
        expert.It's time to stop holding back and start using those killer skills you have learned! If
        you have someone in your sights, romantically speaking, today is the day to make that connection.
         Ask a pertinent question or two and help them see you in a new light. If you are currently in a
         relationship, get ready for things to go to a much hotter level''')
    elif ip==5:
        print('''Gemini:You need to know where to go for the information that will help you most in life.
         Instead of asking friends for advice on how to fatten up your rapidly thinning piggy bank, ask
         an expert. Friends are who you should talk to about your love life, work hassles, and other
         personal issues. But when it comes to credit, investments, and your savings account, you don't
          want to mix those two worlds. Sharing too much about how much money you make or have could also
          creat unnecessary friction.''')
    elif ip==6:
        print('''Cancer:Get out your finest fine-toothed comb because you'll need to go over some very fine
         print one more time. There are an awful lot of small details that could grow into big, embarrassing
          issues later on down the line if you don't nip them in the bud now. Probably the last thing you
          want to do is proofread or double-check your work one more time, but you should do it. It will
          save you a lot more of your time (and your pride) in the long run.''')
    elif ip==7:
        print('''Leo:Despite the fact that you're feeling better than you have in a while, right now is
         not the time to go out and celebrate. You are not overly impulsive as a rule, but today you
         should behave even more conservatively than usual. Bide your time and the right opportunity
         to have a blast will present itself soon enough. Skip any splurges and stay close to home.
         You can have just as celebratory a time cuddled up with a good book or your partner as you
          can at a big party.''')
    elif ip==8:
        print('''Virgo: Today is a great day to try a new food, hobby, sport, or adventure that you have
        always been just a little to scared to try before. Your fears are starting to vanish and your
         courage is growing, in part because your mind is hungry for new stimulation—even if that
          stimulation is based on fear! You will be totally fiery and full of energy, so put it to
           good use by pushing the envelope and pushing past one or two of the boundaries you've built
            for yourself.''')
    elif ip==9:
        print('''Libra: Today is a great day to try a new food, hobby, sport, or adventure that you have
         always been just a little to scared to try before. Your fears are starting to vanish and your
         courage is growing, in part because your mind is hungry for new stimulation—even if that
         stimulation is based on fear! You will be totally fiery and full of energy, so put it to good
          use by pushing the envelope and pushing past one or two of the boundaries you've built for
           yourself.''')
    elif ip==10:
        print('''Scorpio:Can you have too many friends? The answer, you may be beginning to fear,
        is yes! There are only so many free hours in your week, and it might be getting tough to
         prioritize who gets to share them with you. Friendships take as much work as anything else
          does, but the payoff is truly rewarding. See what you can do to show your friends how much
           you care.''')
    elif ip==11:
        print('''Sagittarius:Can you have too many friends? The answer, you may be beginning to
        fear, is yes! There are only so many free hours in your week, and it might be getting
        tough to prioritize who gets to share them with you. Friendships take as much work as
        anything else does, but the payoff is truly rewarding. See what you can do to show your
        friends how much you care.''')
    elif ip==12:
        print('''Capricorn: Today is a great day to try a new food, hobby, sport, or adventure that you
        have always been just a little to scared to try before. Your fears are starting to vanish and your
         courage is growing, in part because your mind is hungry for new stimulation—even if that stimulation
          is based on fear! You will be totally fiery and full of energy, so put it to good use by pushing
          the envelope and pushing past one or two of the boundaries you've built for yourself.''')
    else:
        print("are you sure about this?")

    ip3=input("do u want to try more?(y/n)")
    next=True if ip3=="y" else False
