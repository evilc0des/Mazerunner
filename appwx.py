#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Mazerunner GUI Program

AI Mini-Project

author: Dk Saha
created: January 2017
'''
import wx

class windowClass(wx.Frame):

	def __init__(self, parent, *args, **kwargs):
		super(windowClass, self).__init__(parent, *args, **kwargs)
		self.Centre()

	def DrawImg(self, w, h, path, position):
		bitmap = wx.Bitmap(path)
		bitmap = scale_bitmap(bitmap, 600, 200)
		control = wx.StaticBitmap(self, -1, bitmap)
		control.SetPosition(position)

	def InitMenu(self):
		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
		menubar.Append(fileMenu, '&File')
		self.SetMenuBar(menubar)
		self.Bind(wx.EVT_MENU, self.OnQuit, fitem)
		self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

	def OnQuit(self, e):
		self.Close()

	def OnCloseWindow(self, e):

		dial = wx.MessageDialog(None, 'Are you sure to quit?', 'Question', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = dial.ShowModal()
		if ret == wx.ID_YES:
			self.Destroy()
		else:
			e.Veto()

class splashWindow(windowClass):
	"""docstring for splashWindow"""
	def __init__(self, parent, path, title):
		super(splashWindow, self).__init__(None, title= title, size= (600,200), style= wx.STAY_ON_TOP)
		self.DrawImg(600, 200, path, (0,0))
		self.Show()
		
class mainWindow(windowClass):
	"""docstring for mainWindow"""
	def __init__(self, parent, title):
		super(mainWindow, self).__init__(None, title= title, size= (800,600))
		self.InitMenu()
		self.Show()

def scale_bitmap(bitmap, width, height):
	image = bitmap.ConvertToImage()
	image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
	result = wx.Bitmap(image)
	return result

def startMain(splash):
	mainWindow(None, title='Mazerunner 0.1')
	splash.Close()

def main():
	app = wx.App()
	splash = splashWindow(None, path= 'splash.jpg', title='Mazerunner 0.1')
	wx.CallLater(2000, startMain, splash)
	app.MainLoop()

if __name__ == '__main__':
	main()