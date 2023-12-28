# This program implements a window-based program that asks 
# a user to input California time, then converts to Japan time.

import tkinter

class TimeLagGUI:
    def __init__(self):
      self.mainWindow = tkinter.Tk()

      self.topFrame = tkinter.Frame(self.mainWindow)
      self.midFrame = tkinter.Frame(self.mainWindow)
      self.bottomFrame = tkinter.Frame(self.mainWindow)

      self.caLabel = tkinter.Label(self.topFrame,
                                   text = 'Enter the California time in 24-hour military time (hhmm):')
      self.caEntry = tkinter.Entry(self.topFrame, width = 10)

      # pack()で実際に作ったLabelやEntry、Button fieldを実体化。
      self.caLabel.pack(side = 'left')
      self.caEntry.pack(side = 'left')

      self.resultLabel = tkinter.Label(self.midFrame,
                                       text = 'Japan time: ')
      
      # Label内に入れられるString variableを作成。内容を変えるにはself.jpT.set(str)。
      self.jpT = tkinter.StringVar()
      self.jpTimeLabel = tkinter.Label(self.midFrame, 
                                       textvariable= self.jpT)

      self.resultLabel.pack(side = 'left')
      self.jpTimeLabel.pack(side = 'left')
      
      # Button classは、CommandでFunction call。()は不要で、FilterやMapなどのFunctionと似ている。
      self.jpTimeButton = tkinter.Button(self.bottomFrame,
                                         text = 'Convert to Japan time',
                                         command = self.convert)
      self.quitButton = tkinter.Button(self.bottomFrame,
                                       text = 'Quit',
                                       command = self.mainWindow.destroy)

      self.jpTimeButton.pack(side='left')
      self.quitButton.pack(side='left')
                
      # Frames have to be 実体化 too
      self.topFrame.pack()
      self.midFrame.pack()
      self.bottomFrame.pack()

      tkinter.mainloop()

    #　JpTime button calls this method.
    def convert(self):
      self.caTime = int(self.caEntry.get())
      self.jpTime = 1700 + self.caTime
      
      if self.jpTime >= 2400:
        self.jpTime -= 2400
        self.jpTimeStr = f"{str(self.jpTime)[:-2]}:{str(self.jpTime)[-2:]} in the following day"
      else:
        self.jpTimeStr = f"{str(self.jpTime)[:-2]}:{str(self.jpTime)[-2:]} in the same day"
      # Update StringVar() to be put inside the jpTimeLabel
      self.jpT.set(self.jpTimeStr)
        
timeCAJP = TimeLagGUI()


