class CodeCheckingParameterServiceData(object, IDisposable):
    """ The data needed by code checking server to perform code checking. """
    def Dispose(self):
        """ Dispose(self: CodeCheckingParameterServiceData) """
        pass

    def GetCurrentElements(self):
        """
        GetCurrentElements(self: CodeCheckingParameterServiceData) -> IList[ElementId]
        
            Returns the list of Ids of the current elements.
            Returns: Ids of the current elements. Contains the analytical model element to which the 
             code checking parameter belongs.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: CodeCheckingParameterServiceData, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current document.

Get: Document(self: CodeCheckingParameterServiceData) -> Document

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: CodeCheckingParameterServiceData) -> bool

"""

