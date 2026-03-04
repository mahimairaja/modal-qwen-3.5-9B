# Deploy Qwen 3.5 9B to Modal Serverless GPUS

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="2300">

```

           #############        #############
          ####         ##      ####         ##
         ##  ##         ##    ##  ##         ##
        ##    ##         ##  ##    ##         ##
       ##      ##         ####      ##         ##
      ##        #############        ##         ##
     ##        ##         ####        ##         ##
    ##        ##         ##  ##        ##         ##
   ##        ##         ##    ##        ##         ##
  ##        ##         ##      ##        ##         ##
 ##        ##         ##        ##        ##         ##
##        ##         ##          ##        #############
 ##      ##         ##            ##      ##         ##
  ##    ##         ##              ##    ##         ##
   ##  ##         ##                ##  ##         ##
    ####         ##                  ####         ##
     #############                    #############
```

I was trying to if any api provider will publish the qwen 3.5 9B model as a llm api. But i couldn't find any. So i decided to deploy it myself using modal serverless. And sharing the code with you

## Authenticate with Modal

```bash
modal setup
```

## How to deploy

```bash
modal deploy main.py
```

## How to use

```bash
# Remember to modify the endpoint in client.py

python client.py
```

