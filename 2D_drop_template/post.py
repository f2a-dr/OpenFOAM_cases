# state file generated using paraview version 5.6.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [915, 838]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.0, 0.0, 0.0005000000237487257]
renderView1.StereoType = 0
renderView1.CameraPosition = [0.0, 0.0, 0.027888723603147897]
renderView1.CameraFocalPoint = [0.0, 0.0, 0.0005000000237487257]
renderView1.CameraParallelScale = 0.007088723283396987
renderView1.CameraParallelProjection = 1
renderView1.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'PVFoamReader'
mI_05_01OpenFOAM = PVFoamReader(FileName='/home/fderoma/OpenFOAM/fderoma-8/run/2D/lambda1/MI_05_01/MI_05_01.OpenFOAM')
mI_05_01OpenFOAM.MeshParts = ['internalMesh']
mI_05_01OpenFOAM.Fields = ['alpha.water', 'p_rgh', 'U', 'p']

# create a new 'Cell Centers'
cellCenters1 = CellCenters(Input=mI_05_01OpenFOAM)

# create a new 'Slice'
slice1 = Slice(Input=mI_05_01OpenFOAM)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.0, 0.0, 0.0005000000237487257]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# create a new 'Contour'
contour1 = Contour(Input=slice1)
contour1.ContourBy = ['POINTS', 'alpha.water']
contour1.Isosurfaces = [0.5]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Glyph'
glyph1 = Glyph(Input=cellCenters1,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'U']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 0.0005
glyph1.GlyphTransform = 'Transform2'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from mI_05_01OpenFOAM
mI_05_01OpenFOAMDisplay = Show(mI_05_01OpenFOAM, renderView1)

# trace defaults for the display properties.
mI_05_01OpenFOAMDisplay.Representation = 'Surface'
mI_05_01OpenFOAMDisplay.ColorArrayName = [None, '']
mI_05_01OpenFOAMDisplay.OSPRayScaleArray = 'U'
mI_05_01OpenFOAMDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
mI_05_01OpenFOAMDisplay.SelectOrientationVectors = 'None'
mI_05_01OpenFOAMDisplay.ScaleFactor = 0.0009999999776482583
mI_05_01OpenFOAMDisplay.SelectScaleArray = 'None'
mI_05_01OpenFOAMDisplay.GlyphType = 'Arrow'
mI_05_01OpenFOAMDisplay.GlyphTableIndexArray = 'None'
mI_05_01OpenFOAMDisplay.GaussianRadius = 4.9999998882412914e-05
mI_05_01OpenFOAMDisplay.SetScaleArray = ['POINTS', 'U']
mI_05_01OpenFOAMDisplay.ScaleTransferFunction = 'PiecewiseFunction'
mI_05_01OpenFOAMDisplay.OpacityArray = ['POINTS', 'U']
mI_05_01OpenFOAMDisplay.OpacityTransferFunction = 'PiecewiseFunction'
mI_05_01OpenFOAMDisplay.DataAxesGrid = 'GridAxesRepresentation'
mI_05_01OpenFOAMDisplay.SelectionCellLabelFontFile = ''
mI_05_01OpenFOAMDisplay.SelectionPointLabelFontFile = ''
mI_05_01OpenFOAMDisplay.PolarAxes = 'PolarAxesRepresentation'
mI_05_01OpenFOAMDisplay.ScalarOpacityUnitDistance = 0.0010446031944472004

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
mI_05_01OpenFOAMDisplay.DataAxesGrid.XTitleFontFile = ''
mI_05_01OpenFOAMDisplay.DataAxesGrid.YTitleFontFile = ''
mI_05_01OpenFOAMDisplay.DataAxesGrid.ZTitleFontFile = ''
mI_05_01OpenFOAMDisplay.DataAxesGrid.XLabelFontFile = ''
mI_05_01OpenFOAMDisplay.DataAxesGrid.YLabelFontFile = ''
mI_05_01OpenFOAMDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
mI_05_01OpenFOAMDisplay.PolarAxes.PolarAxisTitleFontFile = ''
mI_05_01OpenFOAMDisplay.PolarAxes.PolarAxisLabelFontFile = ''
mI_05_01OpenFOAMDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
mI_05_01OpenFOAMDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from cellCenters1
cellCenters1Display = Show(cellCenters1, renderView1)

# trace defaults for the display properties.
cellCenters1Display.Representation = 'Surface'
cellCenters1Display.ColorArrayName = [None, '']
cellCenters1Display.OSPRayScaleArray = 'U'
cellCenters1Display.OSPRayScaleFunction = 'PiecewiseFunction'
cellCenters1Display.SelectOrientationVectors = 'None'
cellCenters1Display.ScaleFactor = 0.0009800000116229057
cellCenters1Display.SelectScaleArray = 'None'
cellCenters1Display.GlyphType = 'Arrow'
cellCenters1Display.GlyphTableIndexArray = 'None'
cellCenters1Display.GaussianRadius = 4.9000000581145285e-05
cellCenters1Display.SetScaleArray = ['POINTS', 'U']
cellCenters1Display.ScaleTransferFunction = 'PiecewiseFunction'
cellCenters1Display.OpacityArray = ['POINTS', 'U']
cellCenters1Display.OpacityTransferFunction = 'PiecewiseFunction'
cellCenters1Display.DataAxesGrid = 'GridAxesRepresentation'
cellCenters1Display.SelectionCellLabelFontFile = ''
cellCenters1Display.SelectionPointLabelFontFile = ''
cellCenters1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
cellCenters1Display.DataAxesGrid.XTitleFontFile = ''
cellCenters1Display.DataAxesGrid.YTitleFontFile = ''
cellCenters1Display.DataAxesGrid.ZTitleFontFile = ''
cellCenters1Display.DataAxesGrid.XLabelFontFile = ''
cellCenters1Display.DataAxesGrid.YLabelFontFile = ''
cellCenters1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
cellCenters1Display.PolarAxes.PolarAxisTitleFontFile = ''
cellCenters1Display.PolarAxes.PolarAxisLabelFontFile = ''
cellCenters1Display.PolarAxes.LastRadialAxisTextFontFile = ''
cellCenters1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from glyph1
glyph1Display = Show(glyph1, renderView1)

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', '']
glyph1Display.DiffuseColor = [0.0, 0.0, 0.0]
glyph1Display.OSPRayScaleArray = 'U'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 0.001080000028014183
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 5.400000140070915e-05
glyph1Display.SetScaleArray = ['POINTS', 'U']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'U']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.SelectionCellLabelFontFile = ''
glyph1Display.SelectionPointLabelFontFile = ''
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
glyph1Display.DataAxesGrid.XTitleFontFile = ''
glyph1Display.DataAxesGrid.YTitleFontFile = ''
glyph1Display.DataAxesGrid.ZTitleFontFile = ''
glyph1Display.DataAxesGrid.XLabelFontFile = ''
glyph1Display.DataAxesGrid.YLabelFontFile = ''
glyph1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
glyph1Display.PolarAxes.PolarAxisTitleFontFile = ''
glyph1Display.PolarAxes.PolarAxisLabelFontFile = ''
glyph1Display.PolarAxes.LastRadialAxisTextFontFile = ''
glyph1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from slice1
slice1Display = Show(slice1, renderView1)

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = [None, '']
slice1Display.OSPRayScaleArray = 'U'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 0.0009999999776482583
slice1Display.SelectScaleArray = 'None'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'None'
slice1Display.GaussianRadius = 4.9999998882412914e-05
slice1Display.SetScaleArray = ['POINTS', 'U']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'U']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.SelectionCellLabelFontFile = ''
slice1Display.SelectionPointLabelFontFile = ''
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice1Display.DataAxesGrid.XTitleFontFile = ''
slice1Display.DataAxesGrid.YTitleFontFile = ''
slice1Display.DataAxesGrid.ZTitleFontFile = ''
slice1Display.DataAxesGrid.XLabelFontFile = ''
slice1Display.DataAxesGrid.YLabelFontFile = ''
slice1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice1Display.PolarAxes.PolarAxisTitleFontFile = ''
slice1Display.PolarAxes.PolarAxisLabelFontFile = ''
slice1Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from contour1
contour1Display = Show(contour1, renderView1)

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = [None, '']
contour1Display.LineWidth = 3.0
contour1Display.OSPRayScaleArray = 'U'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 0.0004000000189989805
contour1Display.SelectScaleArray = 'None'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'None'
contour1Display.GaussianRadius = 2.0000000949949027e-05
contour1Display.SetScaleArray = ['POINTS', 'U']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'U']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.SelectionCellLabelFontFile = ''
contour1Display.SelectionPointLabelFontFile = ''
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
contour1Display.DataAxesGrid.XTitleFontFile = ''
contour1Display.DataAxesGrid.YTitleFontFile = ''
contour1Display.DataAxesGrid.ZTitleFontFile = ''
contour1Display.DataAxesGrid.XLabelFontFile = ''
contour1Display.DataAxesGrid.YLabelFontFile = ''
contour1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
contour1Display.PolarAxes.PolarAxisTitleFontFile = ''
contour1Display.PolarAxes.PolarAxisLabelFontFile = ''
contour1Display.PolarAxes.LastRadialAxisTextFontFile = ''
contour1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# setup the color legend parameters for each legend in this view

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')
uLUT.RGBPoints = [5.200000146032835e-07, 0.231373, 0.298039, 0.752941, 1.312000043185435e-05, 0.865003, 0.865003, 0.865003, 2.5720000849105418e-05, 0.705882, 0.0156863, 0.14902]
uLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)
uLUTColorBar.Title = 'U'
uLUTColorBar.ComponentTitle = 'Magnitude'
uLUTColorBar.TitleFontFile = ''
uLUTColorBar.LabelFontFile = ''

# set color bar visibility
uLUTColorBar.Visibility = 0

# hide data in view
Hide(mI_05_01OpenFOAM, renderView1)

# hide data in view
Hide(cellCenters1, renderView1)

# hide data in view
Hide(slice1, renderView1)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')
uPWF.Points = [5.200000146032835e-07, 0.0, 0.5, 0.0, 2.5720000849105418e-05, 1.0, 0.5, 0.0]
uPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(mI_05_01OpenFOAM)
# ----------------------------------------------------------------