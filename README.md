# jaccuse
![Image](https://user-images.githubusercontent.com/15311579/214655423-8da5e44b-fbb2-4bb4-b9ef-6464e25b29cf.png)  
A simple python script to countdown the number since a thing happened  
It makes use of the [sense_hat](https://pythonhosted.org/sense-hat/api/) python library for controlling the LEDs  

Fun fact: You dont need a physical pi to develop this!  
You can run the main.py script in [Trinket.io](https://trinket.io/sense-hat) to emulate a raspberry pi with a sense hat :)  
If you do emulate, just skip to copying the main.py code into the emulator IDE and hitting run. Otherwise,  

## Physical Setup:

### 1. Clone the Repo into home directory (or wherever, im not your mom so do whatever you want)
```shell
cd $HOME
git clone https://github.com/444B/jaccuse.git
```

### 2. apt update and install sense-hat
```shell
sudo apt update && sudo apt install sense-hat -y
```
- note, you can make a pip venv for this but it was giving me numpy warnings (???) despite the fact that I wasnt using numpy or pillow so I opted to skip the venv

### 3. run file
```shell
python3 ~/jaccuse/main.py
```

### 4. (Optional) - add the python script to start up on physical pi startup
open /etc/rc.local  
```shell
sudo nano /etc/rc.local
```
add the following in, right before the bottom line that says "return 0"  

```shell
python3 $HOME/jaccuse/main.py &
```


# Documentation
### 1. Orientation.  
You should see a "?" displayed. Use the Sense pi button (or arrow keys if emulated on trinket) to face the question make the right way  
Press the button in (or Enter if emulated) to select this orientation.

### 2. Duration Selection
Next, the script needs to know how long you want to set the incremental timer  
The options are: Seconds, Minutes, Hours and Days.  
Cycle left and right to get the setting you want and then press the physical button IN (if emulated: press enter)  
The counter will now begin from zero and count up. Note that after 10, things get spooky so keep that in mind.  

### 3. ???

### 4. PROFIT

# How to contribute
- Check out the [Project Board](https://github.com/users/444B/projects/1/views/2?layout=board) for issues and things to fix / add
