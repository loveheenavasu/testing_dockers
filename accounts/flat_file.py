# import os
import jwt


def token(EMBED_ID, PRIVATE_KEY):
    try:
        data = {
            'token': jwt.encode({
                'embed': EMBED_ID,
                'user': {
                    'id': '31262',
                    'email': 'mukul@qricle.com',
                    'name': 'mukulqr',
                },
                'org': {
                    'id': '35617',
                    'name': 'Qricle'
                }},
                PRIVATE_KEY,
                algorithm='HS256'
            )
        }
        return data
    except Exception as e:
        return str(e)




