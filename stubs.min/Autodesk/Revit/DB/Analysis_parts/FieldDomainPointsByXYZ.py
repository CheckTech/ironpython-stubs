class FieldDomainPointsByXYZ(FieldDomainPoints, IDisposable):
    """
    Represents a set of three-dimensional point coordinates
    
    FieldDomainPointsByXYZ(points: IList[XYZ])
    """
    def Dispose(self):
        """ Dispose(self: FieldDomainPoints, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FieldDomainPoints, disposing: bool) """
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

    @staticmethod # known case of __new__
    def __new__(self, points):
        """ __new__(cls: type, points: IList[XYZ]) """
        pass
