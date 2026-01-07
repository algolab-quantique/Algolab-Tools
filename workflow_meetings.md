# Tricks shared during our Workflow Meeting(s)


## Github

## Terminal / Bash
- `ctrl`+`L` instead of `clear` will get a fresh screen by moving the screen down without clearing what's above the cursor

## Keynote
- right click toolbar and `edit toolbar` to find hidden features
  - Group / Ungroup
  - Remove background
  - Forward backward

## Mac OS
- Spacebar open folder while drag and dropping
- `shift`+`cmd`+`.` to show hidden files (brace yourself)
- `cmd`+`I` to open the "file inspector"
  - contains the "always open these files with" feature
  - see hidden filename extension
- `cmd`+`J` to open the "views options" let you set the default apearance for folders 
  - calculate all sizes option
  - open in list view
  - set default view
  - icon size
  - text size

## Hidden customization in Preferences
- Keyboard -> Keyboard Shortcuts -> Services -> New Terminal at Folder

## Customization requiring teminal commands
Faster cursor movement with keyboard:
```
  defaults write NSGlobalDomain KeyRepeat -int 1
  defaults write NSGlobalDomain InitialKeyRepeat -int  15
```

## Matplotlib
- default colors are available as `C0`, `C1`, ...
- Animation with the `gif` package
  ```
  #%%
  import numpy as np
  import matplotlib.pyplot as plt
  
  def plot(xx):
      plt.plot(xx, np.sin(xx))
      plt.xlim(0,10)
      plt.ylim(-1,1)
  
  xx = np.linspace(0,10,40)
  plot(xx)
  
  #%%
  import gif
  frames = [gif.frame(plot)(xx[:t]) for t in list(range(0,40,1))]
  gif.save(frames, "sine.gif", duration=50)
  
  #%%
  from IPython.display import Image
  Image("sine.gif")
  ```

## VS code

### Interactive mode and notebook
- Add interactive "notebook cells" in a `.py` script by adding `#%%`
- `Jupyter: Export current file as jupyter notebook` to transform a script with the above cells in a notebook
- `Jupyter: Export to python script` to export a jupyter notebook to a script

### Multi-cursor workflow
- `option`+`up`, `option`+`down' to move lines 
- `option`+`cmd`+`up`, `option`+`cmd`+`down` to add cursor above, below
- `cmd`+`d` to fin next appearance
- `cmd`+`u` to undo cursor
- `cmd`+`]`/`cmd`+`[` to indent/ unindent
- `ctrl`+`-` to go back to last cursor location
- `ctrl`+`shift`+`-` to go back to last cursor location
