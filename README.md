HOW IT WORKS:
Through a GUI, just changes the .dll you provide in the folder with the script to either SteamVR or OpenComposite to support OpenXR. It's a file switcher...

HOW TO USE:
*Drag the the x64 Steam version of the .dll for your game into a folder beside the python script. Rename it from "openvr_api.dll" to "SteamVR.dll". There is one already in there, just replace it with your games and rename.
The "OpenComposite.dll" will be the other.
In the script, line 7 change the target directory for your game wherever the "openvr_api.dll" is located. Ensure to use proper file path naming scheme.
Line 11 & 12 can stay the same, so long as those two .dll files are in the same folder as the Python script and named properly.
Line 32, you can change the name of the switcher if you like.
That's it. Here's a photo of the structure, thanks!
