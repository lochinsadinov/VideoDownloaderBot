import requests


# ================================== instagram =========================================


async def instagram(post_url: str):  # day = 300
    url = "https://instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com/get-info-rapidapi"

    querystring = {"url": post_url}

    headers = {
        "x-rapidapi-key": "129335ff72msh66a516b0190a3a9p14540cjsndee4f152486f",
        "x-rapidapi-host": "instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json().get('download_url')


# =============================================================================
# -------------------------------------tik tok---------------------------------

async def tiktok(post_url: str):
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/index"

    querystring = {"url": post_url}

    headers = {
        "x-rapidapi-key": "129335ff72msh66a516b0190a3a9p14540cjsndee4f152486f",
        "x-rapidapi-host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    response = response.json()
    return response.get('video')[0], response.get('music')[0]


# ======================================================================================


# ================================  facebook ===========================================
async def facebook(post_url: str):
    url = "https://full-downloader-social-media.p.rapidapi.com/"

    querystring = {"url": post_url}

    headers = {
        "x-rapidapi-key": "129335ff72msh66a516b0190a3a9p14540cjsndee4f152486f",
        "x-rapidapi-host": "full-downloader-social-media.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    response = response.json()
    # pprint(response)
    return response.get('download_url')


# asyncio.run(facebook('https://www.facebook.com/share/r/w35RJLRycr9uA8Uk/'))


# ==============================  snapchat  ====================================


async def snapchat(post_url: str):
    url = "https://download-snapchat-video-spotlight-online.p.rapidapi.com/download"

    querystring = {"url": post_url}

    headers = {
        "x-rapidapi-key": "129335ff72msh66a516b0190a3a9p14540cjsndee4f152486f",
        "x-rapidapi-host": "download-snapchat-video-spotlight-online.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    response = response.json()
    # pprint(response)
    return response.get('story').get('mediaUrl'), response.get('title')


"""
# ====================================
# async def facebook(post_url: str):
#     url = "https://facebook-reel-and-video-downloader.p.rapidapi.com/app/main.php"
#
#     querystring = {"url": post_url}
#
#     headers = {
#         "x-rapidapi-key": "129335ff72msh66a516b0190a3a9p14540cjsndee4f152486f",
#         "x-rapidapi-host": "facebook-reel-and-video-downloader.p.rapidapi.com"
#     }
#
#     response = requests.get(url, headers=headers, params=querystring)
#     response = response.json()
#     return response.get('media')[0].get('hd_url')
#     # pprint(response)
#
#
# # asyncio.run(facebook('https://www.facebook.com/share/r/w35RJLRycr9uA8Uk/'))


# async def facebook(post_url: str):
#     url = "https://full-downloader-social-media.p.rapidapi.com/"
#
#     querystring = {"url": post_url}
#
#     headers = {
#         "x-rapidapi-key": "129335ff72msh66a516b0190a3a9p14540cjsndee4f152486f",
#         "x-rapidapi-host": "full-downloader-social-media.p.rapidapi.com"
#     }
#
#     response = requests.get(url, headers=headers, params=querystring)
#     response = response.json()
#     return response.get('download_url')
#
#
# # asyncio.run(facebook('https://www.facebook.com/share/r/w35RJLRycr9uA8Uk/'))

"""
