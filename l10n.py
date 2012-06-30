# -*- coding: utf-8 -*-

import gettext

# Set up message catalog access
t = gettext.translation('myapplication', 'locale', fallback=True)
_ = t.ugettext

def greet_user(user):
    print _(u'Hello, %s.') % user


children = {'John': 1, 'Mary': 3}

def report_children(user):
    print t.ungettext(
        u'You have %s child',
        u'You have %s children',
        children[user]
    ) % children[user]


if __name__ == '__main__':
    for user in children.keys():
        greet_user(user)
        report_children(user)
