# encoding: utf-8
# module Tekla.Structures.ModelInternal calls itself ModelInternal
# from Tekla.Structures.Model,Version=2017.0.0.0,Culture=neutral,PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes
from ModelInternal_parts.AreWeUnitTesting import AreWeUnitTesting
from ModelInternal_parts.BasePoint import BasePoint
from ModelInternal_parts.BentPlateTestingTool import BentPlateTestingTool
from ModelInternal_parts.BentPlateTools import BentPlateTools
from ModelInternal_parts.CDelegateSetter import CDelegateSetter
from ModelInternal_parts.CDelegateWrapper import CDelegateWrapper
from ModelInternal_parts.ChangeManager import ChangeManager
from ModelInternal_parts.ConversionLink import ConversionLink
from ModelInternal_parts.DelegateFake import DelegateFake
from ModelInternal_parts.dotAreaPolygons_t import dotAreaPolygons_t
from ModelInternal_parts.dotAssembly_t import dotAssembly_t
from ModelInternal_parts.dotBaseComponent_t import dotBaseComponent_t
from ModelInternal_parts.dotBasePointData_t import dotBasePointData_t
from ModelInternal_parts.dotBoltGroup_t import dotBoltGroup_t
from ModelInternal_parts.dotBoltPolygon_t import dotBoltPolygon_t
from ModelInternal_parts.dotBoltShapeData_t import dotBoltShapeData_t
from ModelInternal_parts.dotBooleanPart_t import dotBooleanPart_t
from ModelInternal_parts.dotBoolean_t import dotBoolean_t
from ModelInternal_parts.dotCamera_t import dotCamera_t
from ModelInternal_parts.dotChamfer_t import dotChamfer_t
from ModelInternal_parts.dotClash_t import dotClash_t
from ModelInternal_parts.dotClientId_t import dotClientId_t
from ModelInternal_parts.dotClipPlane_t import dotClipPlane_t
from ModelInternal_parts.dotColor_t import dotColor_t
from ModelInternal_parts.dotComponentAttribute_t import dotComponentAttribute_t
from ModelInternal_parts.dotComponentInputObject_t import dotComponentInputObject_t
from ModelInternal_parts.dotContourPoint_t import dotContourPoint_t
from ModelInternal_parts.dotContour_t import dotContour_t
from ModelInternal_parts.dotControlObject_t import dotControlObject_t
from ModelInternal_parts.dotConversionLink_t import dotConversionLink_t
from ModelInternal_parts.dotCreateIFCFromModel_t import dotCreateIFCFromModel_t
from ModelInternal_parts.dotCreateNCFromModel_t import dotCreateNCFromModel_t
from ModelInternal_parts.dotCreateReportFromModel_t import dotCreateReportFromModel_t
from ModelInternal_parts.dotDeformingData_t import dotDeformingData_t
from ModelInternal_parts.dotDrawPolygonSurface_t import dotDrawPolygonSurface_t
from ModelInternal_parts.dotDrawPolyLine_t import dotDrawPolyLine_t
from ModelInternal_parts.dotDrawText_t import dotDrawText_t
from ModelInternal_parts.dotEdgeChamfer_t import dotEdgeChamfer_t
from ModelInternal_parts.dotEdges_t import dotEdges_t
from ModelInternal_parts.dotEnumerator_t import dotEnumerator_t
from ModelInternal_parts.dotFittingOrCutPlane_t import dotFittingOrCutPlane_t
from ModelInternal_parts.dotFormingStates_t import dotFormingStates_t
from ModelInternal_parts.dotGetClipPlanes_t import dotGetClipPlanes_t
from ModelInternal_parts.dotGetProperties_t import dotGetProperties_t
from ModelInternal_parts.dotGraphicPolyLine_t import dotGraphicPolyLine_t
from ModelInternal_parts.dotGridPlane_t import dotGridPlane_t
from ModelInternal_parts.dotGrid_t import dotGrid_t
from ModelInternal_parts.dotGuideline_t import dotGuideline_t
from ModelInternal_parts.dotHierarchicDefinition_t import dotHierarchicDefinition_t
from ModelInternal_parts.dotHierarchicList_t import dotHierarchicList_t
from ModelInternal_parts.dotHierarchicObject_t import dotHierarchicObject_t
from ModelInternal_parts.dotIFC2X3_Application_t import dotIFC2X3_Application_t
from ModelInternal_parts.dotIFC2X3_Organization_t import dotIFC2X3_Organization_t
from ModelInternal_parts.dotIFC2X3_OwnerHistoryChangeAction_t import dotIFC2X3_OwnerHistoryChangeAction_t
from ModelInternal_parts.dotIFC2X3_OwnerHistoryState_t import dotIFC2X3_OwnerHistoryState_t
from ModelInternal_parts.dotIFC2X3_OwnerHistory_t import dotIFC2X3_OwnerHistory_t
from ModelInternal_parts.dotIFC2X3_ParametricObject_ShapeProfile_t import dotIFC2X3_ParametricObject_ShapeProfile_t
from ModelInternal_parts.dotIFC2X3_PersonAndOrganization_t import dotIFC2X3_PersonAndOrganization_t
from ModelInternal_parts.dotIFC2X3_Person_t import dotIFC2X3_Person_t
from ModelInternal_parts.dotIFC2X3_Product_t import dotIFC2X3_Product_t
from ModelInternal_parts.dotIntersectionPoints_t import dotIntersectionPoints_t
from ModelInternal_parts.dotIntersectionSolid_t import dotIntersectionSolid_t
from ModelInternal_parts.dotLegFace_t import dotLegFace_t
from ModelInternal_parts.dotLoadClassAttributes_t import dotLoadClassAttributes_t
from ModelInternal_parts.dotLoadCommonAttributes_t import dotLoadCommonAttributes_t
from ModelInternal_parts.dotLoadGroup_t import dotLoadGroup_t
from ModelInternal_parts.dotManipulateObject_t import dotManipulateObject_t
from ModelInternal_parts.dotMaterial_t import dotMaterial_t
from ModelInternal_parts.dotModelCommit_t import dotModelCommit_t
from ModelInternal_parts.dotModelInfoModeEnum import dotModelInfoModeEnum
from ModelInternal_parts.dotModelInfo_t import dotModelInfo_t
from ModelInternal_parts.dotModelObjectType_t import dotModelObjectType_t
from ModelInternal_parts.dotModelObject_t import dotModelObject_t
from ModelInternal_parts.dotModificationStamp_t import dotModificationStamp_t
from ModelInternal_parts.dotModStampCompare_t import dotModStampCompare_t
from ModelInternal_parts.dotModStamp_t import dotModStamp_t
from ModelInternal_parts.dotnetDoubleList_t import dotnetDoubleList_t
from ModelInternal_parts.dotnetEdgeList_t import dotnetEdgeList_t
from ModelInternal_parts.dotnetIntList_t import dotnetIntList_t
from ModelInternal_parts.DotNetModelProxy import DotNetModelProxy
from ModelInternal_parts.dotnetPointList_t import dotnetPointList_t
from ModelInternal_parts.dotnetStringList_t import dotnetStringList_t
from ModelInternal_parts.dotNumberingQuery_t import dotNumberingQuery_t
from ModelInternal_parts.dotNumberingSeries_t import dotNumberingSeries_t
from ModelInternal_parts.dotObjectOperationsEnum import dotObjectOperationsEnum
from ModelInternal_parts.dotObject_t import dotObject_t
from ModelInternal_parts.dotOffset_t import dotOffset_t
from ModelInternal_parts.dotPartLine_t import dotPartLine_t
from ModelInternal_parts.dotPartMark_t import dotPartMark_t
from ModelInternal_parts.dotPart_t import dotPart_t
from ModelInternal_parts.dotPhaseNumbers_t import dotPhaseNumbers_t
from ModelInternal_parts.dotPhase_t import dotPhase_t
from ModelInternal_parts.dotPlane_t import dotPlane_t
from ModelInternal_parts.dotPolygon_t import dotPolygon_t
from ModelInternal_parts.dotPolymeshObject_t import dotPolymeshObject_t
from ModelInternal_parts.dotPolymeshValidateInvalidInfo_t import dotPolymeshValidateInvalidInfo_t
from ModelInternal_parts.dotPolymesh_t import dotPolymesh_t
from ModelInternal_parts.dotPosition_t import dotPosition_t
from ModelInternal_parts.dotPourObject_t import dotPourObject_t
from ModelInternal_parts.dotProfile_t import dotProfile_t
from ModelInternal_parts.dotProgressBar_t import dotProgressBar_t
from ModelInternal_parts.dotProjectInfo_t import dotProjectInfo_t
from ModelInternal_parts.dotRebarEndDetailStrip_t import dotRebarEndDetailStrip_t
from ModelInternal_parts.dotRebarGroup_t import dotRebarGroup_t
from ModelInternal_parts.dotRebarHookData_t import dotRebarHookData_t
from ModelInternal_parts.dotRebarMesh_t import dotRebarMesh_t
from ModelInternal_parts.dotRebarProperties_t import dotRebarProperties_t
from ModelInternal_parts.dotRebarPropertyStrip_t import dotRebarPropertyStrip_t
from ModelInternal_parts.dotRebarSetAddition_t import dotRebarSetAddition_t
from ModelInternal_parts.dotRebarSet_t import dotRebarSet_t
from ModelInternal_parts.dotRebarSpacing_t import dotRebarSpacing_t
from ModelInternal_parts.dotRebarSplice_t import dotRebarSplice_t
from ModelInternal_parts.dotRebarSplitter_t import dotRebarSplitter_t
from ModelInternal_parts.dotRebarStrand_t import dotRebarStrand_t
from ModelInternal_parts.dotRebarStrip_t import dotRebarStrip_t
from ModelInternal_parts.dotRebarThreading_t import dotRebarThreading_t
from ModelInternal_parts.dotReferenceModelObjectAttributeEnumerator_t import dotReferenceModelObjectAttributeEnumerator_t
from ModelInternal_parts.dotReferenceModelObjectAttribute_t import dotReferenceModelObjectAttribute_t
from ModelInternal_parts.dotReferenceModelObject_t import dotReferenceModelObject_t
from ModelInternal_parts.dotReferenceModelRevision_t import dotReferenceModelRevision_t
from ModelInternal_parts.dotReferenceModel_t import dotReferenceModel_t
from ModelInternal_parts.dotReinforcement_t import dotReinforcement_t
from ModelInternal_parts.dotSaveAsWebModel_t import dotSaveAsWebModel_t
from ModelInternal_parts.dotSaveOperation_t import dotSaveOperation_t
from ModelInternal_parts.dotSetGetProperty_t import dotSetGetProperty_t
from ModelInternal_parts.dotSetProperty_t import dotSetProperty_t
from ModelInternal_parts.dotSetTemporaryColors_t import dotSetTemporaryColors_t
from ModelInternal_parts.dotSetTemporaryStates_t import dotSetTemporaryStates_t
from ModelInternal_parts.dotSharingOperation_t import dotSharingOperation_t
from ModelInternal_parts.dotSingleRebar_t import dotSingleRebar_t
from ModelInternal_parts.dotSolid_t import dotSolid_t
from ModelInternal_parts.dotSpacingZone_t import dotSpacingZone_t
from ModelInternal_parts.dotStringProperty_t import dotStringProperty_t
from ModelInternal_parts.dotSurfaceObject_t import dotSurfaceObject_t
from ModelInternal_parts.dotSurfaceTreatment_t import dotSurfaceTreatment_t
from ModelInternal_parts.dotTaskDependency_t import dotTaskDependency_t
from ModelInternal_parts.dotTaskObjectAttacher_t import dotTaskObjectAttacher_t
from ModelInternal_parts.dotTaskWorktype_t import dotTaskWorktype_t
from ModelInternal_parts.dotTask_t import dotTask_t
from ModelInternal_parts.dotTemporaryState import dotTemporaryState
from ModelInternal_parts.dotTemporaryStatesEnum import dotTemporaryStatesEnum
from ModelInternal_parts.dotTemporaryTransparenciesEnum import dotTemporaryTransparenciesEnum
from ModelInternal_parts.dotTransformationPlane_t import dotTransformationPlane_t
from ModelInternal_parts.dotUIModelObjectSelector_t import dotUIModelObjectSelector_t
from ModelInternal_parts.dotUIPicker_t import dotUIPicker_t
from ModelInternal_parts.dotUndoOperation_t import dotUndoOperation_t
from ModelInternal_parts.dotViewSelector_t import dotViewSelector_t
from ModelInternal_parts.dotViewVisibilitySettings_t import dotViewVisibilitySettings_t
from ModelInternal_parts.dotView_t import dotView_t
from ModelInternal_parts.dotWeldGeometry_t import dotWeldGeometry_t
from ModelInternal_parts.dotWeld_t import dotWeld_t
from ModelInternal_parts.dotWire_t import dotWire_t
from ModelInternal_parts.DoubleList import DoubleList
from ModelInternal_parts.EventHandlerWrapper import EventHandlerWrapper
from ModelInternal_parts.GeometryImporter import GeometryImporter
from ModelInternal_parts.GeometryTree import GeometryTree
from ModelInternal_parts.ICDelegate import ICDelegate
from ModelInternal_parts.IEventHandler import IEventHandler
from ModelInternal_parts.IntList import IntList
from ModelInternal_parts.ModelExtensions import ModelExtensions
from ModelInternal_parts.ModelObjectFactory import ModelObjectFactory
from ModelInternal_parts.NumberingQueryModeEnum import NumberingQueryModeEnum
from ModelInternal_parts.Operation import Operation
from ModelInternal_parts.PointList import PointList
from ModelInternal_parts.PolygonExtensions import PolygonExtensions
from ModelInternal_parts.RebarSetAction import RebarSetAction
from ModelInternal_parts.Remoter import Remoter
from ModelInternal_parts.ScopedCDelegateSetter import ScopedCDelegateSetter
from ModelInternal_parts.Serializer import Serializer
from ModelInternal_parts.StringList import StringList
from ModelInternal_parts.SurfaceObjectCreator import SurfaceObjectCreator
from ModelInternal_parts.SyncHandler import SyncHandler
from ModelInternal_parts.UDAChanges import UDAChanges
