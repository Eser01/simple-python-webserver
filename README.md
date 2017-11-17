# Simple Python WebServer
Simple code to serve statics files with python (without any external module)

## SetUp the server
1. All the configurations are in the file "config.py", you can change them there.
2. The server will serve all the file inside the "web" folder, so put your files there.
	- Note: you can change the folder "web" from another in the config file
3. Start the server:
```bash
./server.py # make sure the files has the right permissions
# OR
python server.py
```
4. (In case of SSL=True) To generate "server.pem" file, use the following command:
```bash
openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
```