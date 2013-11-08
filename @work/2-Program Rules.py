from Windawesome import (
    Windawesome,
    ProgramRule,
    State,
    OnWindowCreatedOrShownAction,
    OnWindowCreatedOnWorkspaceAction)
from Windawesome.NativeMethods import WS, WS_EX


config.ProgramRules = [
    
    # Proto
	ProgramRule(
		processName = "^Proto$",
		isManaged = False
	),
    # Find and Run Robot
	ProgramRule(
		className = "^TApplication$",
		displayName = "^Find and Run Robot$",
		isManaged = False
	),
    # PrtScr
	ProgramRule(
		className = "^TPrtScrMainForm$",
		isManaged = False
	),
    
    # Explorer
	ProgramRule(
		className = "^CabinetWClass$",
	 	updateIcon = True,
		rules = [ProgramRule.Rule(workspace = 1, titlebar = State.SHOWN, windowBorders = State.SHOWN)]
	),
	ProgramRule(
		className = "^ExploreWClass$",
		updateIcon = True,
		rules = [ProgramRule.Rule(workspace = 1, titlebar = State.SHOWN, windowBorders = State.SHOWN)]
	),


    # Cygwin
	ProgramRule(
		className = "^mintty$",
		redrawDesktopOnWindowCreated = True,
		rules = [ProgramRule.Rule(workspace = 2, titlebar = State.HIDDEN, windowBorders = State.SHOWN)]
	),
    # MobaXTerm
	ProgramRule(
		className = "^TMobaXtermForm$",
		rules = [ProgramRule.Rule(workspace = 2, titlebar = State.HIDDEN, windowBorders = State.SHOWN)]
	),
    # Console, Git Bash, Powershell
	ProgramRule(
		className = "^ConsoleWindowClass$",
		rules = [ProgramRule.Rule(workspace = 2, titlebar = State.HIDDEN, windowBorders = State.SHOWN)]
	),
    # Process Hacker
	ProgramRule(
		className = "^ProcessHacker$",
		rules = [ProgramRule.Rule(workspace = 2, titlebar = State.HIDDEN, windowBorders = State.SHOWN)]
	),

    # Emacs
	ProgramRule(
		className = "^Emacs$",
		rules = [ProgramRule.Rule(workspace = 8, titlebar = State.HIDDEN, windowBorders = State.HIDDEN)]
	),
    # Yes, Emacs and Vim on the same workspace, it's possible :-)
	ProgramRule(
		className = "^Vim$",
		rules = [ProgramRule.Rule(workspace = 8, titlebar = State.HIDDEN, windowBorders = State.SHOWN)]
	),
    # Visual Studio
	ProgramRule(
		processName = "^devenv$",
		rules = [ProgramRule.Rule(workspace = 8, titlebar = State.HIDDEN, windowBorders = State.SHOWN)]
	),
    # Notepad
	ProgramRule(
		className = "^Notepad$",
		rules = [ProgramRule.Rule(workspace = 6, titlebar = State.HIDDEN, windowBorders = State.SHOWN)]
	),

    # Lync
	ProgramRule(
		className = "^CommunicatorMainWindowClass$",
		rules = [ProgramRule.Rule(workspace = 4, isFloating = True)]
	),
	ProgramRule(
		className = "^IMWindowClass$",
		redrawDesktopOnWindowCreated = True,
		onWindowCreatedAction = OnWindowCreatedOrShownAction.HideWindow,
		onWindowCreatedOnCurrentWorkspaceAction = OnWindowCreatedOnWorkspaceAction.PreserveTopmostWindow,
		onWindowCreatedOnInactiveWorkspaceAction = OnWindowCreatedOnWorkspaceAction.PreserveTopmostWindow,
		rules = [ProgramRule.Rule(workspace = 4, titlebar = State.HIDDEN, windowBorders = State.SHOWN)]
	),
    # Pigeon
	ProgramRule(
		className = "^gdkWindowToplevel$",
        processName= "^pidgin$",
		rules = [ProgramRule.Rule(workspace = 4, titlebar = State.HIDDEN, windowBorders = State.SHOWN)]
	),
    # Outlook
	ProgramRule(
		className = "^rctrl_renwnd32$",
		rules = [ProgramRule.Rule(workspace = 5, titlebar = State.HIDDEN, windowBorders = State.SHOWN)]
	),
    # Perforce
	ProgramRule(
		className = "^QWidget$",
        processName= "^p4v$",
		rules = [ProgramRule.Rule(workspace = 7, titlebar = State.HIDDEN, windowBorders = State.SHOWN)]
	),
	ProgramRule(
		className = "^QWidget$",
        processName= "^p4merge$",
		rules = [ProgramRule.Rule(workspace = 7, titlebar = State.HIDDEN, windowBorders = State.SHOWN)]
	),
	ProgramRule(
		className = "^QWidget$",
        processName= "^p4admin$",
		rules = [ProgramRule.Rule(workspace = 7, titlebar = State.HIDDEN, windowBorders = State.SHOWN)]
	),
    # Hansoft
	ProgramRule(
		className = "^QWidget$",
        processName= "^HPMClient_x64$",
		rules = [ProgramRule.Rule(workspace = 7, titlebar = State.HIDDEN, windowBorders = State.SHOWN)]
	),

    # Chrome
	ProgramRule(
		className = "^Chrome_WidgetWin_1$",
		rules = [ProgramRule.Rule(workspace = 3, titlebar = State.HIDDEN, windowBorders = State.SHOWN)]
	),
    # Internet Explorer
	ProgramRule(
		className = "^IEFrame$",
		rules = [ProgramRule.Rule(workspace = 3, titlebar = State.HIDDEN, windowBorders = State.SHOWN)]
	),

	ProgramRule(
		styleContains = WS.WS_POPUP,
		isManaged = False
	),
	ProgramRule(
		styleNotContains = WS.WS_MAXIMIZEBOX,
		rules = [ProgramRule.Rule(isFloating = True)]
	),
	ProgramRule() # an all-catching rule in the end to manage all other windows
]
