import json

def get_api_key():
    # Load credentials
    cred = json.loads(open("E:\live-project\moviegeeks\.prs").read())
    return cred['themoviedb_apikey']


if __name__ == '__main__':
    res = get_api_key()
    print(res)