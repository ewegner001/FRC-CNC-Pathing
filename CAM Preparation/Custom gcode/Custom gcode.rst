Manual gcode
==========================
There are instances in which you need to get the :term:`CNC` machine to do something beyond a :term:`Path`, such as stop at a certain portion of the program to change the workholding.  In these situations, instead of creating an entirely new program, manual gcode can be used to do this.  

How to use Manual gcode
+++++++++++++++++++++++


Manual gcode types
+++++++++++++++++++++++++

Stop
------------

**Stop**

.. warning:: 
    **Stop** must not be confused with **Optional Stop**, which may or may not result in the machine stopping as intended depending on the machine.  


Dwell
---------

Dwelling is similar to a **Stop** with the exception that it does not stop the :term:`spindle`, but does stop the feedrate.  This results in the tool still spinning, but the machine is stationary in the main axes. 