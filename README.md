# jaccuse
A simple python script to countdown the number since [event]

Fun fact: You dont need a physical pi to develop this!  
You can run the main.py script in [Trinket.io](https://trinket.io/sense-hat) to emulate a raspberry pi with a sense hat :)  

# Run the following to get setup:

## 1. Clone the Repo into home directory (or wherever, im not your mom so do whatever you want)
```shell
cd $HOME
git clone -b Second-Draft https://github.com/444B/jaccuse.git
```

## 2. apt update and install sense-hat
```shell
sudo apt update && sudo apt install sense-hat -y
```
- note, you can make a pip venv for this but it was giving me numpy warnings (???) despite the fact that I wasnt using numpy or pillow

## 3. run file
```shell
python3 ~/jaccuse/main.py
```

# Documentation
## 1. Orientation.  
You should see a "?" displayed. Use the Sense pi button (or arrow keys if emulated on trinket) to face the question make the right way  
Press the button in (or Enter if emulated) to select this orientation.

## 2. Duration Selection
Next, the script needs to know how long you want to set the incremental timer  
The options are: Seconds, Minutes, Hours and Days.  
Cycle left and right to get the setting you want and then press the physical button IN (if emulated: press enter)  
The counter will now begin from zero and count up. Note that after 10, things get spooky so keep that in mind.  

## 3. ???

## 4. PROFIT


# TODO
- Add a button that restarts the timer
- Bring value to stakeholders
- Add a way to logg the frequency of restarts
- Find a way to show double digits. Currently single digits work perfectly but double digits scroll past (owing to the difference in sense.show_letter() and sense.show_message(). Work in Progress
