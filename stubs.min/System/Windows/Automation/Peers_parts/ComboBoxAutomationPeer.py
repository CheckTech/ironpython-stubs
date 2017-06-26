class ComboBoxAutomationPeer(SelectorAutomationPeer, IItemContainerProvider, ISelectionProvider, IValueProvider, IExpandCollapseProvider):
    """
    Exposes System.Windows.Controls.ComboBox types to UI Automation.
    
    ComboBoxAutomationPeer(owner: ComboBox)
    """
    def CreateItemAutomationPeer(self, *args): #cannot find CLR method
        """
        CreateItemAutomationPeer(self: ComboBoxAutomationPeer, item: object) -> ItemAutomationPeer
        
            Creates a new instance of the System.Windows.Automation.Peers.ItemAutomationPeer class.
        
            item: The System.Windows.Controls.ComboBoxItem that is associated with this System.Windows.Automation.Peers.ComboBoxAutomationPeer.
            Returns: A new instance of the System.Windows.Automation.Peers.ItemAutomationPeer class.
        """
        pass

    def FindOrCreateItemAutomationPeer(self, *args): #cannot find CLR method
        """ FindOrCreateItemAutomationPeer(self: ItemsControlAutomationPeer, item: object) -> ItemAutomationPeer """
        pass

    def GetAcceleratorKeyCore(self, *args): #cannot find CLR method
        """
        GetAcceleratorKeyCore(self: UIElementAutomationPeer) -> str
        
            Gets the accelerator key for the System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer. This method is called by 
             System.Windows.Automation.Peers.AutomationPeer.GetAcceleratorKey.
        
            Returns: The System.Windows.Automation.AutomationProperties.AcceleratorKey that is returned by System.Windows.Automation.AutomationProperties.GetAcceleratorKey(System.Windows.DependencyObject).
        """
        pass

    def GetAccessKeyCore(self, *args): #cannot find CLR method
        """
        GetAccessKeyCore(self: UIElementAutomationPeer) -> str
        
            Gets the access key for the System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer.This method is called by 
             System.Windows.Automation.Peers.AutomationPeer.GetAccessKey.
        
            Returns: The access key for the System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer.
        """
        pass

    def GetAutomationControlTypeCore(self, *args): #cannot find CLR method
        """
        GetAutomationControlTypeCore(self: ComboBoxAutomationPeer) -> AutomationControlType
        
            Gets the control type for this System.Windows.Automation.Peers.ComboBoxAutomationPeer. This method is called by System.Windows.Automation.Peers.AutomationPeer.GetAutomationControlType.
            Returns: The System.Windows.Automation.Peers.AutomationControlType.ComboBox enumeration value.
        """
        pass

    def GetAutomationIdCore(self, *args): #cannot find CLR method
        """
        GetAutomationIdCore(self: FrameworkElementAutomationPeer) -> str
        
            Gets the string that uniquely identifies the System.Windows.FrameworkElement that is associated with this System.Windows.Automation.Peers.FrameworkElementAutomationPeer. Called by 
             System.Windows.Automation.Peers.AutomationPeer.GetAutomationId.
        
            Returns: The automation identifier for the element associated with the System.Windows.Automation.Peers.FrameworkElementAutomationPeer, or System.String.Empty if there isn't an automation identifier.
        """
        pass

    def GetBoundingRectangleCore(self, *args): #cannot find CLR method
        """
        GetBoundingRectangleCore(self: UIElementAutomationPeer) -> Rect
        
            Gets the System.Windows.Rect that represents the bounding rectangle of the System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer. This method is 
             called by System.Windows.Automation.Peers.AutomationPeer.GetBoundingRectangle.
        
            Returns: The System.Windows.Rect that contains the coordinates of the element. Optionally, if the element is not both a System.Windows.Interop.HwndSource and a System.Windows.PresentationSource, this method returns 
             System.Windows.Rect.Empty.
        """
        pass

    def GetChildrenCore(self, *args): #cannot find CLR method
        """
        GetChildrenCore(self: ComboBoxAutomationPeer) -> List[AutomationPeer]
        
            Gets a collection of child elements. This method is called by System.Windows.Automation.Peers.AutomationPeer.GetChildren.
            Returns: A collection of child elements.
        """
        pass

    def GetClassNameCore(self, *args): #cannot find CLR method
        """
        GetClassNameCore(self: ComboBoxAutomationPeer) -> str
        
            Gets the name of the class that defines the type that is associated with this System.Windows.Automation.Peers.ComboBoxAutomationPeer. This method is called by 
             System.Windows.Automation.Peers.AutomationPeer.GetClassName.
        
            Returns: A string that contains "ComboBox".
        """
        pass

    def GetClickablePointCore(self, *args): #cannot find CLR method
        """
        GetClickablePointCore(self: UIElementAutomationPeer) -> Point
        
            Gets a System.Windows.Point that represents the clickable space that is on the System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer. This method is 
             called by System.Windows.Automation.Peers.AutomationPeer.GetClickablePoint.
        
            Returns: The System.Windows.Point on the element that allows a click. The point values are (System.Double.NaN, System.Double.NaN) if the element is not both a System.Windows.Interop.HwndSource and a 
             System.Windows.PresentationSource.
        """
        pass

    def GetHelpTextCore(self, *args): #cannot find CLR method
        """
        GetHelpTextCore(self: FrameworkElementAutomationPeer) -> str
        
            Gets the string that describes the functionality of the System.Windows.ContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer. Called by 
             System.Windows.Automation.Peers.AutomationPeer.GetHelpText.
        
            Returns: The help text, usually from the System.Windows.Controls.ToolTip, or System.String.Empty if there is no help text.
        """
        pass

    def GetHostRawElementProviderCore(self, *args): #cannot find CLR method
        """
        GetHostRawElementProviderCore(self: AutomationPeer) -> HostedWindowWrapper
        
            Tells UI Automation where in the UI Automation tree to place the hwnd being hosted by a Windows Presentation Foundation (WPF) element.
            Returns: This method returns the hosted hwnd to UI Automation for controls that host hwnd objects.
        """
        pass

    def GetItemStatusCore(self, *args): #cannot find CLR method
        """
        GetItemStatusCore(self: UIElementAutomationPeer) -> str
        
            Gets a string that communicates the visual status of the System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer. This method is called by 
             System.Windows.Automation.Peers.AutomationPeer.GetItemStatus.
        
            Returns: The string that contains the System.Windows.Automation.AutomationProperties.ItemStatus that is returned by System.Windows.Automation.AutomationProperties.GetItemStatus(System.Windows.DependencyObject).
        """
        pass

    def GetItemTypeCore(self, *args): #cannot find CLR method
        """
        GetItemTypeCore(self: UIElementAutomationPeer) -> str
        
            Gets a human-readable string that contains the item type that the System.Windows.UIElement for this System.Windows.Automation.Peers.UIElementAutomationPeer represents. This method is called by 
             System.Windows.Automation.Peers.AutomationPeer.GetItemType.
        
            Returns: The string that contains the System.Windows.Automation.AutomationProperties.ItemType that is returned by System.Windows.Automation.AutomationProperties.GetItemType(System.Windows.DependencyObject).
        """
        pass

    def GetLabeledByCore(self, *args): #cannot find CLR method
        """
        GetLabeledByCore(self: UIElementAutomationPeer) -> AutomationPeer
        
            Gets the System.Windows.Automation.Peers.AutomationPeer for the element that is targeted to the System.Windows.UIElement for this System.Windows.Automation.Peers.UIElementAutomationPeer. This method is 
             called by System.Windows.Automation.Peers.AutomationPeer.GetLabeledBy.
        
            Returns: The System.Windows.Automation.Peers.AutomationPeer for the element that is targeted to the System.Windows.UIElement for this System.Windows.Automation.Peers.UIElementAutomationPeer.
        """
        pass

    def GetLocalizedControlTypeCore(self, *args): #cannot find CLR method
        """
        GetLocalizedControlTypeCore(self: AutomationPeer) -> str
        
            When overridden in a derived class, is called by System.Windows.Automation.Peers.AutomationPeer.GetLocalizedControlType.
            Returns: The type of the control.
        """
        pass

    def GetNameCore(self, *args): #cannot find CLR method
        """
        GetNameCore(self: FrameworkElementAutomationPeer) -> str
        
            Gets the text label of the System.Windows.ContentElement that is associated with this System.Windows.Automation.Peers.ContentElementAutomationPeer. Called by 
             System.Windows.Automation.Peers.AutomationPeer.GetName.
        
            Returns: The text label of the element that is associated with this automation peer.
        """
        pass

    def GetOrientationCore(self, *args): #cannot find CLR method
        """
        GetOrientationCore(self: UIElementAutomationPeer) -> AutomationOrientation
        
            Gets a value that indicates whether the System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer is laid out in a specific direction. This method is 
             called by System.Windows.Automation.Peers.AutomationPeer.GetOrientation.
        
            Returns: The System.Windows.Automation.Peers.AutomationOrientation.None enumeration value.
        """
        pass

    def GetPattern(self, pattern):
        """
        GetPattern(self: ComboBoxAutomationPeer, pattern: PatternInterface) -> object
        
            Gets the control pattern for this System.Windows.Automation.Peers.ComboBoxAutomationPeer.
        
            pattern: One of the enumeration values.
            Returns: If pattern is System.Windows.Automation.Peers.PatternInterface.Value or System.Windows.Automation.Peers.PatternInterface.ExpandCollapse, this method returns a reference to the current instance of the 
             System.Windows.Automation.Peers.ComboBoxAutomationPeer; otherwise, this method calls the base implementation on System.Windows.Automation.Peers.SelectorAutomationPeer.
        """
        pass

    def GetPeerFromPointCore(self, *args): #cannot find CLR method
        """ GetPeerFromPointCore(self: AutomationPeer, point: Point) -> AutomationPeer """
        pass

    def HasKeyboardFocusCore(self, *args): #cannot find CLR method
        """
        HasKeyboardFocusCore(self: UIElementAutomationPeer) -> bool
        
            Gets a value that indicates whether the System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer currently has keyboard input focus. This method is 
             called by System.Windows.Automation.Peers.AutomationPeer.HasKeyboardFocus.
        
            Returns: true if the element has keyboard input focus; otherwise, false.
        """
        pass

    def IsContentElementCore(self, *args): #cannot find CLR method
        """
        IsContentElementCore(self: UIElementAutomationPeer) -> bool
        
            Gets a value that indicates whether the System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer is an element that contains data that is presented to 
             the user. This method is called by System.Windows.Automation.Peers.AutomationPeer.IsContentElement.
        
            Returns: true.
        """
        pass

    def IsControlElementCore(self, *args): #cannot find CLR method
        """
        IsControlElementCore(self: UIElementAutomationPeer) -> bool
        
            Gets or sets a value that indicates whether the System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer is understood by the end user as interactive. 
             Optionally, the user might understand the System.Windows.UIElement as contributing to the logical structure of the control in the GUI. This method is called by 
             System.Windows.Automation.Peers.AutomationPeer.IsControlElement.
        
            Returns: true.
        """
        pass

    def IsEnabledCore(self, *args): #cannot find CLR method
        """
        IsEnabledCore(self: UIElementAutomationPeer) -> bool
        
            Gets a value that indicates whether the System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer can accept keyboard focus. This method is called by 
             System.Windows.Automation.Peers.AutomationPeer.IsKeyboardFocusable.
        
            Returns: A boolean that contains the value of System.Windows.UIElement.IsEnabled.
        """
        pass

    def IsKeyboardFocusableCore(self, *args): #cannot find CLR method
        """
        IsKeyboardFocusableCore(self: UIElementAutomationPeer) -> bool
        
            Gets a value that indicates whether the System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer can accept keyboard focus. This method is called by 
             System.Windows.Automation.Peers.AutomationPeer.IsKeyboardFocusable.
        
            Returns: true if the element is focusable by the keyboard; otherwise false.
        """
        pass

    def IsOffscreenCore(self, *args): #cannot find CLR method
        """
        IsOffscreenCore(self: UIElementAutomationPeer) -> bool
        
            Gets a value that indicates whether the System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer is off the screen. This method is called by 
             System.Windows.Automation.Peers.AutomationPeer.IsOffscreen.
        
            Returns: true if the element is not on the screen; otherwise, false.
        """
        pass

    def IsPasswordCore(self, *args): #cannot find CLR method
        """
        IsPasswordCore(self: UIElementAutomationPeer) -> bool
        
            Gets a value that indicates whether the System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer contains protected content. This method is called by 
             System.Windows.Automation.Peers.AutomationPeer.IsPassword.
        
            Returns: false.
        """
        pass

    def IsRequiredForFormCore(self, *args): #cannot find CLR method
        """
        IsRequiredForFormCore(self: UIElementAutomationPeer) -> bool
        
            Gets a value that indicates whether the System.Windows.UIElement that is associated with this System.Windows.Automation.Peers.UIElementAutomationPeer is required to be completed on a form. This method is 
             called by System.Windows.Automation.Peers.AutomationPeer.IsRequiredForForm.
        
            Returns: A boolean that contains the value that is returned by System.Windows.Automation.AutomationProperties.GetIsRequiredForForm(System.Windows.DependencyObject), if it's set; otherwise false.
        """
        pass

    def PeerFromProvider(self, *args): #cannot find CLR method
        """
        PeerFromProvider(self: AutomationPeer, provider: IRawElementProviderSimple) -> AutomationPeer
        
            Gets an System.Windows.Automation.Peers.AutomationPeer for the specified System.Windows.Automation.Provider.IRawElementProviderSimple proxy.
        
            provider: The class that implements System.Windows.Automation.Provider.IRawElementProviderSimple.
            Returns: The System.Windows.Automation.Peers.AutomationPeer.
        """
        pass

    def ProviderFromPeer(self, *args): #cannot find CLR method
        """
        ProviderFromPeer(self: AutomationPeer, peer: AutomationPeer) -> IRawElementProviderSimple
        
            Gets the System.Windows.Automation.Provider.IRawElementProviderSimple for the specified System.Windows.Automation.Peers.AutomationPeer.
        
            peer: The automation peer.
            Returns: The proxy.
        """
        pass

    def SetFocusCore(self, *args): #cannot find CLR method
        """
        SetFocusCore(self: ComboBoxAutomationPeer)
            Sets the keyboard input focus on the System.Windows.Controls.ComboBox control that is associated with this System.Windows.Automation.Peers.ComboBoxAutomationPeer object. This method is called by 
             System.Windows.Automation.Peers.AutomationPeer.SetFocus.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, owner):
        """ __new__(cls: type, owner: ComboBox) """
        pass

    IsHwndHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the element that is associated with this System.Windows.Automation.Peers.AutomationPeer hosts hwnds in Windows Presentation Foundation (WPF).

"""

    IsVirtualized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

