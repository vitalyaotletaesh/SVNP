import os


def svn_commit():
    os.system('svn add --force C:\\Users\\xxxam\\DjangoProjects\\media\\project_data\\SVNP')
    os.system('svn commit --message "changed files" C:\\Users\\xxxam\\DjangoProjects\\media\\project_data\\SVNP')
