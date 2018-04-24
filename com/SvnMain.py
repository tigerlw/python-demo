#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

import pysvn



def get_login(realm, username, may_save):
    retcode = True
    username = 'liuwei'
    password = '001986lw'
    save = True
    return retcode, username, password, save


def ssl_server_trust_prompt( trust_dict ):
    return (True  # server is trusted
            , trust_dict["failures"]
            , True)

client = pysvn.Client()
client.callback_get_login = get_login
client.callback_ssl_server_trust_prompt = ssl_server_trust_prompt


#client.checkout('https://ASS-LIUWEI.ucloudlink.com:4455/svn/ocs-system/','D:/work/doc/pysvn/ocs-system')

client.update('D:/work/doc/pysvn/ocs-system')

entries_list = client.ls('https://ASS-LIUWEI.ucloudlink.com:4455/svn/ocs-system/')

for en in entries_list:
    print en.name


log_message = "reason for change"
def get_log_message():
    return True, log_message
client.callback_get_log_message = get_log_message

tag_name = 'features_20180404002'
#client.copy('https://ASS-LIUWEI.ucloudlink.com:4455/svn/ocs-system/baseline', 'https://ASS-LIUWEI.ucloudlink.com:4455/svn/ocs-system/features/%s' % tag_name )


#tag_name = 'release_20180404'
#client.copy('https://ASS-LIUWEI.ucloudlink.com:4455/svn/ocs-system/baseline', 'https://ASS-LIUWEI.ucloudlink.com:4455/svn/ocs-system/release/%s' % tag_name )
path1='https://ass-liuwei.ucloudlink.com:4455/svn/ocs-system/release/release_20180404'
path2 ='https://ass-liuwei.ucloudlink.com:4455/svn/ocs-system/features/features_20180404001'
path3 ='https://ass-liuwei.ucloudlink.com:4455/svn/ocs-system/features/features_20180404002'

entry = client.info2(path1)

pyinfo = entry[0][1]

print pyinfo['rev'].number


entry2 = client.info2(path2)

pyinfo2 = entry[0][1]

print pyinfo2['rev'].number

entry3 = client.info2(path3)

pyinfo3 = entry[0][1]

print pyinfo3['rev'].number


revision1 = pysvn.Revision(pysvn.opt_revision_kind.number, pyinfo['rev'].number)
revision2 = pysvn.Revision(pysvn.opt_revision_kind.number, pyinfo2['rev'].number)
revision3 = pysvn.Revision(pysvn.opt_revision_kind.number, pyinfo3['rev'].number)


revision = pysvn.Revision(pysvn.opt_revision_kind.number, 8)

wcpath = 'D:/work/doc/pysvn/ocs-system/release/release_20180404'

sourcepath = 'D:/work/doc/pysvn/ocs-system/features/features_20180404001'


#client.merge( path1, revision1, path2, revision2, wcpath )

client.merge( path2, revision, path2, revision2, wcpath )

#client.checkin([wcpath], 'Corrected spelling of python in foo.txt')
