# This is a Element details using pubchempy
# we will be adding all the functions of pubchempy with UI inputs here

__________________
#run the start.sh:

```
sh start.sh
```

*** this has all the requirements and commands

___________________________________________________________________________________________________________
# Having issue with port already used Check which services are running on a specific port (e.g., port 5000)

```
sudo lsof -i :5000
```
___________________
# Kill the services 

```
kill -9 <service ID>
```
------------------------------------------------------------------------

# Do register and login 
	 Like if you find the code usefull
	 Provide suggestion 
 
------------------------------------------------------------------------------
# Doing code commit 
# Assuming you are in the root directory of your Git repository

```
git add .
git commit -m "Your commit message here"
git push
```

# having issue with virtual environment
#Creating a new virtual environment (venv) following the provided steps will not conflict with the existing one.
#The new virtual environment will be a separate and isolated environment with its own Python interpreter and installed packages.

Here are the steps:
________________________________________________________________
#Deactivate the current virtual environment (if it's activated):

```
deactivate
```
__________________________________________
#Remove the existing virtual environment:

```
rm -rf venv
```
___________________
#Upgrade virtualenv:
```
pip install --upgrade virtualenv
```

__________________________________________________
#Recreate and activate the new virtual environment:
```
virtualenv venv
source venv/bin/activate
```
	On Windows, use `venv\Scripts\activate`

_______________________
#then run the start.sh:

```
sh start.sh
```
*** this has all the requirements and commands 

# Having issue with port already used Check which services are running on a specific port (e.g., port 5000)

sudo lsof -i :5000

--------------------------------------------------------------------------
