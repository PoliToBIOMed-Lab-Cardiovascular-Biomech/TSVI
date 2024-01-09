# -*- coding: utf-8 -*-
"""
This Python code processes wall shear stress (WSS) data related to a surface mesh 
in Visualization Toolkit Polygonal (vtp) format, to calculate Topological Shear Variation Index (TSVI)

Created on Fri Sep 25 12:43:18 2020

@author: Maurizio Lodi Rizzini (Politecnico di Torino, Turin, Italy)
@comments by: Giuseppe De Nisco (Politecnico di Torino, Turin, Italy)
"""
# Import the VTK (Visualization Toolkit) library and the NumPy library in Python. 
# VTK is a powerful open-source software system for 3D computer graphics, image processing, and visualization, while NumPy is a fundamental package 
# for scientific computing with Python, providing support for large, multi-dimensional arrays and matrices, along with a collection of mathematical 
# functions to operate on these arrays.
import vtk
import numpy as np

# Import the vtk_to_numpy function from the vtk.util.numpy_support module and the vmtkscripts module from the vmtk package. 
# These modules are commonly used in scientific and medical visualization and simulation tasks.
from vtk.util.numpy_support import vtk_to_numpy
from vmtk import vmtkscripts

# Define several functions for working with VTK (Visualization Toolkit) data.
# WritePolyData function takes an input VTK polydata object and a filename, and writes the polydata to a file in XML format using the vtkXMLPolyDataWriter
def WritePolyData(input,filename):
   writer = vtk.vtkXMLPolyDataWriter()
   writer.SetInputData(input)
   writer.SetFileName(filename)
   writer.Write()

# ReadPolyData function takes a filename, reads the polydata from the file using the vtkXMLPolyDataReader, and returns the output.   
def ReadPolyData(filename):
   reader = vtk.vtkXMLPolyDataReader()
   reader.SetFileName(filename)
   reader.Update()
   return reader.GetOutput()

# writeScalarVTKarray function takes a 1D array and a name, and creates a VTK double array with the same values and name. 
# This array can be used to store scalar data in VTK polydata objects.
def writeScalarVTKarray(array,name):
    vtkArray = vtk.vtkDoubleArray()
    vtkArray.SetNumberOfComponents(1)
    vtkArray.SetNumberOfTuples(len(array))
    vtkArray.FillComponent(0,0.)
    vtkArray.SetName(name)
    for i in range(0,len(array)):
        vtkArray.SetTuple1(i,array[i])
    return vtkArray

# Initialize variables T, dt, and scale.
T = .. #cardiac cycle in sec
dt = .. #time-step size in sec
scale = 1 #scale factor for surface scaling (if geometry is in mm scale=0.001)

# Read the VTK PolyData from a file
surface = ReadPolyData('filename.vtp')
# Initialize lists to store intantaneous wall shear stress (WSS) vector and its magnitude
wss = list()
wssMag = list()
# Loop over each time step to calculate WSS vector and its magnitudes
for i in range(int(T/dt)):
    # Read the WSS vector data from surface for the current time step
    wss.append(vtk_to_numpy(surface.GetPointData().GetArray('WSS_'+'{0:03}'.format(i))))
    # Calculate the magnitude of the WSS vector
    wssMag.append(np.sqrt(wss[i][:,0]**2+wss[i][:,1]**2+wss[i][:,2]**2))

# Initialize an array to store the normalized WSS divergence for each time step
normWSSdiv = np.zeros([len(wssMag[0]),int(T/dt)])
# Loop over each time step to calculate the instantaneous normalized WSS divergence
for i in range(int(T/dt)):
    # Normalize the WSS vector components by its magnitude
    normalizedWSS_x = wss[i][:,0]/wssMag[i]
    normalizedWSS_y = wss[i][:,1]/wssMag[i]
    normalizedWSS_z = wss[i][:,2]/wssMag[i]
    # Combine the normalized components into a single array
    normalizedWSS = np.transpose(np.vstack([normalizedWSS_x, normalizedWSS_y, normalizedWSS_z]))
    # Convert the normalized WSS array to a VTK array
    normalizedWSS_VTK = writeVectorVTKarray(normalizedWSS,'normWSS')

    # Scale the surface by the specified scale factor
    scaleSurface = vmtkscripts.vmtkSurfaceScaling()
    scaleSurface.Surface = surface
    scaleSurface.ScaleFactor = scale
    scaleSurface.Execute()

    # Add the normalized WSS vector data to the scaled surface
    scaleSurface.Surface.GetPointData().AddArray(normalizedWSS_VTK)

    # Apply a gradient filter to calculate the Jacobian of the normalized WSS
    gradient = vtk.vtkGradientFilter()
    gradient.SetInputData(scaleSurface.Surface)
    gradient.SetInputScalars(0,'normWSS')
    gradient.SetResultArrayName('normWSSJacobian')
    gradient.Update()
    # Get the output of the gradient filter
    normWSSJ_surface = gradient.GetOutput()

    # Convert the Jacobian data to a NumPy array
    normWSSJ = vtk_to_numpy(normWSSJ_surface.GetPointData().GetArray('normWSSJacobian'))
    # Calculate the divergence of the normalized WSS for the current time step
    normWSSdiv[:,i] = normWSSJ[:,0]+normWSSJ[:,4]+normWSSJ[:,8]

# Calculate the mean divergence of the normalized WSS over all time steps
normWSSdiv_mean = np.mean(normWSSdiv,axis=1)
# Initialize a list to store the squared differences from the mean
normWSSdiv_diff = list()
# Loop over each time step to calculate the squared differences from the mean
for i in range(int(T/dt)):
    normWSSdiv_diff.append((normWSSdiv[:,i]-normWSSdiv_mean)**2)

# Calculate the Topological Shear Stress Variation Index (TSVI)
TSVI = np.sqrt((1/T)*sum(normWSSdiv_diff)*dt)
# Convert the TSVI data to a VTK array
TSVI_vtk = writeScalarVTKarray(TSVI,'TSVI')

# Retrieve the cells and points from the original surface
cells = surface.GetPolys()
points = surface.GetPoints()
# Create an empty VTK PolyData object
emptySurface = vtk.vtkPolyData()
emptySurface.SetPoints(points)
emptySurface.SetPolys(cells)

# Add the TSVI data to the empty surface
emptySurface.GetPointData().AddArray(TSVI_vtk)
# Write the updated surface data to a file
WritePolyData(emptySurface,'filename.vtp')