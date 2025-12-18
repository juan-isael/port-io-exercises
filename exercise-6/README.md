# EXERCISE 6

I have completed the necessary implementation in my Port account (port+juanisael@savannahtech.io) to match the Port environment of the client.

I also wrote a Python script called `solution.py` that connects to the Port API to extract, process, and update the required data.

---
## Approach Followed: 
1.	Authenticated to the Port.io API using environment variables with my credentials.  
2.	Used the `requests` library for HTTP calls and `raise_for_status()` for error handling.  
3.	Processed JSON responses and counted EOL frameworks used by each service.  
4.	Updated service entities with the calculated number of EOL packages.  
5.	Applied type hints and logging for clarity and debugging.
---
## How to run
1.	Clone the repository:
```bash
git clone https://github.com/juan-isael/port-io-exercises.git
cd port-io-exercises
```
2.	Navigate to Exercise 6:
```bash
cd exercise-6
```
3.	Install dependencies
```bash
pip install -r requirements.txt
```
4.	Set temporary environment variables for your credentials
   
Windows
```powershell
$Env:PORT_CLIENT_ID= "YOUR_CLIENT_ID"
$Env:PORT_CLIENT_SECRET="YOUR_CLIENT_SECRET”
```
Linux/macOS
```bash
export PORT_CLIENT_ID="YOUR_CLIENT_ID"
export PORT_CLIENT_SECRET="YOUR_CLIENT_SECRET"
```
5.	Run the script
```bash
python solution.py
```

The script will print framework entities identifiers and their state; service entities identifiers with the number of EOL frameworks and finally the result of the updating process via API
