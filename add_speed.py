import maya.cmds as cmds
import math

Psel = cmds.ls( selection=True )
try:

	nodeT = cmds.nodeType( Psel[0] )
	print nodeT
	if nodeT == 'transform':
		checkAttr = cmds.objExists(Psel[0]+'.speed')
		print checkAttr 
		if checkAttr == True:
			listexpr = cmds.listConnections(Psel[0]+'.speed')
			if listexpr == None :
			    ex1 = 'float $lastPosX = `getAttr -t (frame-1) '+Psel[0]+'.tx`;'
			    ex2 = 'float $lastPosY = `getAttr -t (frame-1) '+Psel[0]+'.ty`;'
			    ex3 = 'float $lastPosZ = `getAttr -t (frame-1) '+Psel[0]+'.tz`;'
			    ex4 = Psel[0]+'.speed = abs (mag (<<'+Psel[0]+'.translateX,'+Psel[0]+'.translateY,'+Psel[0]+'.translateZ>>)- mag (<<$lastPosX,$lastPosY,$lastPosZ>>) );'
			    exAll = ex1+ex2+ex3+ex4
			    cmds.expression( o=Psel[0], s=exAll)
			else:	
				cmds.delete(listexpr[0])
				ex1 = 'float $lastPosX = `getAttr -t (frame-1) '+Psel[0]+'.tx`;'
				ex2 = 'float $lastPosY = `getAttr -t (frame-1) '+Psel[0]+'.ty`;'
				ex3 = 'float $lastPosZ = `getAttr -t (frame-1) '+Psel[0]+'.tz`;'
				ex4 = Psel[0]+'.speed = abs (mag (<<'+Psel[0]+'.translateX,'+Psel[0]+'.translateY,'+Psel[0]+'.translateZ>>)- mag (<<$lastPosX,$lastPosY,$lastPosZ>>) );'
				exAll = ex1+ex2+ex3+ex4
				cmds.expression( o=Psel[0], s=exAll)
				
		else:
			print "test"
			cmds.addAttr( Psel[0],longName='speed' )
			ex1 = 'float $lastPosX = `getAttr -t (frame-1) '+Psel[0]+'.tx`;'
			ex2 = 'float $lastPosY = `getAttr -t (frame-1) '+Psel[0]+'.ty`;'
			ex3 = 'float $lastPosZ = `getAttr -t (frame-1) '+Psel[0]+'.tz`;'
			ex4 = Psel[0]+'.speed = abs (mag (<<'+Psel[0]+'.translateX,'+Psel[0]+'.translateY,'+Psel[0]+'.translateZ>>)- mag (<<$lastPosX,$lastPosY,$lastPosZ>>) );'
			exAll = ex1+ex2+ex3+ex4
			print exAll
			cmds.expression( o=Psel[0], s=exAll)
			
	else:
		print '---> select transform !'
					
except TypeError :
	print '---> select transform !'
		
		



