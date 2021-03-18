from TikTokApi import TikTokApi
from flask import Flask






api = TikTokApi.get_instance()
app = Flask(__name__)

@app.route("/<handle>")
def get_user_info(handle):
    print(handle)

    return api.get_user_object(handle)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



# api = TikTokApi.get_instance()
# print(api.get_user_object("tejashullur"))
# print(api.userPosts(
#     "6852733616251192326",
#     "MS4wLjABAAAAjS7R9HXwjGDgu_N5-qcOLjtnUeM0FGKaT0ieje5cNyT1eMDpvduQzeTl_9Y5BZj8", 5 ))
