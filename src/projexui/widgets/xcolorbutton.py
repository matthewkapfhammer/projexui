#!/usr/bin/python

"""
Extends the base QPushButton class to support color selection.
"""

# define authorship information
__authors__         = ['Eric Hulser']
__author__          = ','.join(__authors__)
__credits__         = []
__copyright__       = 'Copyright (c) 2011, Projex Software'
__license__         = 'LGPL'

# maintanence information
__maintainer__      = 'Projex Software'
__email__           = 'team@projexsoftware.com'

#------------------------------------------------------------------------------

from projexui.qt        import Signal, Property
from projexui.qt.QtGui  import QPushButton,\
                               QColor,\
                               QColorDialog

class XColorButton(QPushButton):
    colorChanged = Signal(QColor)
    
    def __init__( self, parent ):
        super(XColorButton, self).__init__(parent)
        
        # initialize the color
        color       = QColor('black')
        self._color = color
        palette     = self.palette()
        palette.setColor(palette.Button, color)
        self.setPalette(palette)
        
        # create connections
        self.clicked.connect(self.pickColor)
    
    def color( self ):
        """
        Returns the color value for this button.
        
        :return     <QColor>
        """
        return self._color
    
    def pickColor( self ):
        """
        Prompts the user to select a color for this button.
        """
        color = QColorDialog.getColor( self.color(), self )
        
        if ( color.isValid() ):
            self.setColor(color)
    
    def setColor( self, color ):
        """
        Sets the color value for this button to the given color.
        
        :param      color | <QColor>
        """
        self._color = color
        palette     = self.palette()
        palette.setColor(palette.Button, color)
        self.setPalette(palette)
        
        if ( not self.signalsBlocked() ):
            self.colorChanged.emit(color)
    
    x_color = Property(QColor, color, setColor)
    
__designer_plugins__ = [XColorButton]