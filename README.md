# image2textSR
Copy text from image using screenshot tool in debian based(ubuntu)/arch based(manjaro) linux distro...

Make sure you have python3... If you don't have python3 and rather have python, then you have to change the firstOneTimeRun.sh and replace python3 with python one time...
```
git clone https://github.com/SR-Hossain/image2textSR
cd image2textSR
sudo chmod +x firstOneTimeRun.sh
```

if you are using Arch-based linux distro run this code
```
python3 arch_prerun.py
```
if you are not using arch, then DON'T RUN THE ABOVE CODE!!!

Now continue executing the commands shown below:
```
./firstOneTimeRun.sh
image2textSR
```
From now on, just type
<code>image2textSR</code>
on terminal and voila, see the magic!!!

Use cursor to select area to copy and then click on the tick mark to confirm the selection...

Tips: I would recommend that make a custom shortcut in your distro for terminal command... when giving command in custom shortcut give this command to work properly: 
```
image2textSR && echo hiii
```

<h1>I have used flameshot as screenshot tool here... Take a tour in <a href="https://github.com/flameshot-org/flameshot">the github page</a> of flameshot.....</h1>
