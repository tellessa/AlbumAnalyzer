import apis.spotipy_util as spotipy_util


def get_object_methods(object_):
    """Gets all the methods for an object"""
    object_methods = [method_name for method_name in dir(object)
                      if callable(getattr(object, method_name))]
    return object_methods, len(object_methods)


if __name__ == "__main__":
    sp = spotipy_util._get_spotify_using_spotify_o_auth()
    methods, count = get_object_methods(sp)
    print(count)  # 22 methods on the Spotify object!
