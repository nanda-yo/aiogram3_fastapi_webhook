# aiogram3 fastapi webhook #
 Deployment ready telegram bot template using FastAPI and aiogram3 via webhook for cyclic.sh.

There're some WIP API routes, and compiled vue/vite being served on "/", also WIP.
# To deploy on cyclic
- fork this repo
- go to variables section of your deployed app
- add these vars replacing with your own values
```bash
bot_token = your_bot_token  
webhook_url = https://your_host_url_or_server_ip  
webhook_path = /whatever/endpoint/you/want  
secret_tg_token = literally_anything_telegram_will_send_it_back
```

# To deploy somewhere else
- create .env in the same folder as app.py
- fill in with
```bash
debug=False  
bot_token= "your_bot_token"  
webhook_url="https://your_host_url_or_server_ip"  
webhook_path="/whatever/endpoint/you/want"  
secret_tg_token="literally_anything_telegram_will_send_it_back"
```
* Create and activate venv
```bash
python -m venv venv
source venv/bin/activate
```
* install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
* ... and run
```bash
python server.py
```
or run 
```bash
./bin install
```
to install  
and
```bash
./bin start
```
to run server





todo:  

add aws db integration
add 
