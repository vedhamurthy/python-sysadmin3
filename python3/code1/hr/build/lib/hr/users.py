import pwd
import subprocess
import sys

from .helpers import user_names

def add(user_info):
    print("Adding user '%s'" % user_info['name'])
    try:
        subprocess.call([
            'useradd',
            '-p',
            user_info['password'],
            '-G',
            _groups_str(user_info),
            user_info['name'],
        ])
    except:
        print("Failed to add user '%s'" % user_info['name'])
        sys.exit(1)

def remove(user_info):
    print("Removing user '%s'" % user_info['name'])
    try:
        subprocess.call([
            'userdel',
            '-r',
            user_info['name']
        ])
    except:
        print("Failed to remove user '%s'" % user_info['name'])
        sys.exit(1)

def update(user_info):
    print("Updating user '%s'" % user_info['name'])
    try:
        subprocess.call([
            'usermod',
            '-p',
            user_info['password'],
            '-G',
            _groups_str(user_info),
            user_info['name'],
        ])
    except:
        print("Failed to update user '%s'" % user_info['name'])
        sys.exit(1)

def sync(users, existing_user_names=user_names()):
    user_names = [user['name'] for user in users]
    for user in users:
        if user['name'] not in existing_user_names:
            add(user)
        elif user['name'] in existing_user_names:
            update(user)
    for user_name in existing_user_names:
        if not user_name in user_names:
            remove({ 'name': user_name })

def _groups_str(user_info):
    return ','.join(user_info['groups'] or [])