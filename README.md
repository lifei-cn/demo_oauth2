# Demo for oath2 server/client by Django

## Register the client application on oauth2 server

    http://<oauth2-server>/o/applications/register/
        client type: Confidential
        grant type:
            Authorization code  (for web login)
            Resource owner password-based   (for subsystem api)
    
## Add oauth2 server on client

    http://<oauth2-client>/admin/socialaccount/socialapp/add
    

## How to access protected api

1.  Get access token from oath2 server


     curl --request POST \
          --url http://127.0.0.1:8000/o/token/ \
          --header 'Accept: */*' \
          --header 'Accept-Encoding: gzip, deflate' \
          --header 'Cache-Control: no-cache' \
          --header 'Connection: keep-alive' \
          --header 'Content-Length: 247' \
          --header 'Content-Type: application/x-www-form-urlencoded' \
          --header 'Cookie: sessionid=sfgqy7ej3fkuz8bunpft6jdl3akqga5l; csrftoken=t2ava3XRbP2WjtR6mvziTfj9nvF3MBCHZ6Shwx3lW8EYYVCpwBx2vN2bGFEeZ6C4; messages="9f6261956dfc60f13f5b806b41f9be22c0103068$[[\"__json_message\"\0540\05425\054\"Successfully signed in as test.\"]\054[\"__json_message\"\0540\05425\054\"Successfully signed in as test.\"]\054[\"__json_message\"\0540\05425\054\"Successfully signed in as test.\"]\054[\"__json_message\"\0540\05425\054\"Successfully signed in as test.\"]]"' \
          --header 'Host: 127.0.0.1:8000' \
          --header 'Postman-Token: 22f62bb4-4cea-4c46-92cb-dd6d63def194,6d14baed-54d7-45c6-b2c0-d0db7ae571a8' \
          --header 'User-Agent: PostmanRuntime/7.15.2' \
          --header 'cache-control: no-cache' \
          --data 'client_id=jOgVldzu59fttlBFb2P13sDa9nXpqwM6FJkabPCY&grant_type=password&username=test&password=Abc%2C123.&client_secret=H5xTkRxZ9sROEouviiwOx75nFHN0MZ9mqZLWlIl066A5J21c4rDM0WOe1cTXOB1cPVk3R7nQyc6lXxUCVx09fnhEHn8spHwfPfZlJkP2HVgCotNDGnYrAfD03D25cJWb'

    Response:
         {
            "access_token": "Bx8hMYBbHu3deg3a7iTshGouHxGumC",
            "expires_in": 36000,
            "token_type": "Bearer",
            "scope": "read write",
            "refresh_token": "LhCU13HohZMTxikpXqGUQUYlFExVm8"
         }

2.  Get token from oauth client

        curl --request POST \
             --url http://127.0.0.1:9000/rest-auth/custom/ \
             --header ': ' \
             --header 'Accept: */*' \
             --header 'Accept-Encoding: gzip, deflate' \
             --header 'Cache-Control: no-cache' \
             --header 'Connection: keep-alive' \
             --header 'Content-Length: 43' \
             --header 'Content-Type: application/x-www-form-urlencoded' \
             --header 'Cookie: sessionid=sfgqy7ej3fkuz8bunpft6jdl3akqga5l; csrftoken=dGkaEflbTSpUeBCvVT1ojSiN1CHgUbqDz4rLSAZdyxSJbj78vfyQ3PVtsROkRDRU; messages="4e91fd66d4c6278b0bf0053cce40d64e58f80b52$[[\"__json_message\"\0540\05425\054\"Successfully signed in as test.\"]\054[\"__json_message\"\0540\05425\054\"Successfully signed in as test.\"]\054[\"__json_message\"\0540\05425\054\"Successfully signed in as test.\"]]"' \
             --header 'Host: 127.0.0.1:9000' \
             --header 'Postman-Token: afe60633-b97f-471e-8eaa-e12442a2c5bf,3a1af119-f390-4c8d-9384-3fc3c0f3dc76' \
             --header 'User-Agent: PostmanRuntime/7.15.2' \
             --header 'cache-control: no-cache' \
             --data access_token=6x4K8jMWypTVwivYuebBZSsfTTQbRV
             
         Response:
            {
                "key": "1fb7b88e57bc94e6945ec71817c2abae167feb82"
            }

3.  access api by token

        curl --request GET \
             --url http://127.0.0.1:9000/api/test/ \
             --header 'Accept: */*' \
             --header 'Accept-Encoding: gzip, deflate' \
             --header 'Cache-Control: no-cache' \
             --header 'Connection: keep-alive' \
             --header 'Cookie: sessionid=sfgqy7ej3fkuz8bunpft6jdl3akqga5l; csrftoken=t2ava3XRbP2WjtR6mvziTfj9nvF3MBCHZ6Shwx3lW8EYYVCpwBx2vN2bGFEeZ6C4; messages="9f6261956dfc60f13f5b806b41f9be22c0103068$[[\"__json_message\"\0540\05425\054\"Successfully signed in as test.\"]\054[\"__json_message\"\0540\05425\054\"Successfully signed in as test.\"]\054[\"__json_message\"\0540\05425\054\"Successfully signed in as test.\"]\054[\"__json_message\"\0540\05425\054\"Successfully signed in as test.\"]]"' \
             --header 'Host: 127.0.0.1:9000' \
             --header 'Postman-Token: 17937ade-9e21-495b-bf2f-ad6ee2a6b21b,feca3558-8107-4dd5-9f4c-2a7ddd3c813c' \
             --header 'User-Agent: PostmanRuntime/7.15.2' \
             --header 'cache-control: no-cache'
        
        
        ** curl -X GET http://127.0.0.1:9000/api/test/ -H 'Authorization: Token 1fb7b88e57bc94e6945ec71817c2abae167feb82' **
        
        Response:
            {
                "msg": "Hello World"
            }
