from System.Drawing import (
    Color,
    ColorTranslator,
    Font,
    FontStyle)
from System.Linq import Enumerable
from Windawesome import (
    ILayout,
    TileLayout,
    FullScreenLayout,
    FloatingLayout,
    IPlugin,
    Workspace)
from Windawesome import (
    Bar,
    LayoutWidget,
    WorkspacesWidget,
    ApplicationTabsWidget,
    SystemTrayWidget,
    CpuMonitorWidget,
    RamMonitorWidget,
    LaptopBatteryMonitorWidget,
    LanguageBarWidget,
    CurrentlyPlayingWidget,
    SeparatorWidget)
from Windawesome import (
    LoggerPlugin,
    ShortcutsManager,
    InputLanguageChangerPlugin)
from Windawesome.NativeMethods import MOD
from System import Tuple
from System.Windows.Forms import Keys


config.WindowBorderWidth = 1
config.WindowPaddedBorderWidth = 0

config.CheckForUpdates = False


solarizedDarkFG = ColorTranslator.FromHtml("#657b83")
solarizedDarkBG = ColorTranslator.FromHtml("#002b36")
solarizedDarkHighlightedFG = ColorTranslator.FromHtml("#eee8d5")
solarizedDarkHighlightedBG = ColorTranslator.FromHtml("#859900")

workspacesWidgetForegroundColors = [solarizedDarkFG for i in range(0, 10)]
workspacesWidgetBackgroundColors = [solarizedDarkBG for i in range(0, 10)]


config.Bars = Enumerable.ToArray[Bar]([

    # MONITOR 1

	Bar(windawesome.monitors[0],
		[
			WorkspacesWidget(
				normalForegroundColor = workspacesWidgetForegroundColors,
				normalBackgroundColor = workspacesWidgetBackgroundColors,
				highlightedForegroundColor = solarizedDarkHighlightedFG,
				highlightedBackgroundColor = solarizedDarkHighlightedBG,
				highlightedInactiveForegroundColor = solarizedDarkHighlightedBG,
                highlightedInactiveBackgroundColor = solarizedDarkBG,
				flashingForegroundColor = Color.Black
			),
			LayoutWidget(
				foregroundColor = solarizedDarkHighlightedFG,
				backgroundColor = solarizedDarkBG,
			)
		],

		[
			SystemTrayWidget(True),
			LanguageBarWidget(
				foregroundColor = solarizedDarkFG,
				backgroundColor = solarizedDarkBG
			),
			SeparatorWidget(
				foregroundColor = solarizedDarkFG,
				backgroundColor = solarizedDarkBG
			),
			DateTimeWidget("ddd, d-MMM", "", "", solarizedDarkBG, solarizedDarkFG),
			SeparatorWidget(
				foregroundColor = solarizedDarkFG,
				backgroundColor = solarizedDarkBG
			),
			DateTimeWidget("hh:mm tt", "", "", solarizedDarkBG, solarizedDarkFG),
		],

        # do not show the opened application buttons (like i3)
		[
		],

		backgroundColor = solarizedDarkBG,
		font = Font("DejaVu Sans Mono", 8, FontStyle.Regular)
	),

    # MONITOR 2

	Bar(windawesome.monitors[1],
		[
			WorkspacesWidget(
				normalForegroundColor = workspacesWidgetForegroundColors,
				normalBackgroundColor = workspacesWidgetBackgroundColors,
				highlightedForegroundColor = solarizedDarkHighlightedFG,
				highlightedBackgroundColor = solarizedDarkHighlightedBG,
				highlightedInactiveForegroundColor = solarizedDarkFG,
                highlightedInactiveBackgroundColor = solarizedDarkBG,
				flashingForegroundColor = Color.Black
			),
			LayoutWidget(
				foregroundColor = solarizedDarkHighlightedFG,
				backgroundColor = solarizedDarkBG,
			)
		],

		[
			SystemTrayWidget(True),
			LanguageBarWidget(
				foregroundColor = solarizedDarkFG,
				backgroundColor = solarizedDarkBG
			),
			SeparatorWidget(
				foregroundColor = solarizedDarkFG,
				backgroundColor = solarizedDarkBG
			),
			DateTimeWidget("ddd, d-MMM", "", "", solarizedDarkBG, solarizedDarkFG),
			SeparatorWidget(
				foregroundColor = solarizedDarkFG,
				backgroundColor = solarizedDarkBG
			),
			DateTimeWidget("hh:mm tt", "", "", solarizedDarkBG, solarizedDarkFG),
		],

        # I don't show the opened application buttons
		[
		],

		backgroundColor = solarizedDarkBG,
		font = Font("DejaVu Sans Mono", 8, FontStyle.Regular)
	)
])

config.Workspaces = Enumerable.ToArray[Workspace]([
	Workspace(windawesome.monitors[0], TileLayout(masterAreaFactor = 0.6), [config.Bars[0]], name = '1: Main'),
	Workspace(windawesome.monitors[0], TileLayout(masterAreaFactor = 0.6), [config.Bars[0]], name = '2: System'),
	Workspace(windawesome.monitors[0], TileLayout(masterAreaFactor = 0.6), [config.Bars[0]], name = '3: Web'),
	Workspace(windawesome.monitors[0], TileLayout(masterAreaFactor = 0.6), [config.Bars[0]], name = '4: Chat'),
	Workspace(windawesome.monitors[0], TileLayout(masterAreaFactor = 0.6), [config.Bars[0]], name = '5: EMails'),
	Workspace(windawesome.monitors[0], TileLayout(masterAreaFactor = 0.6), [config.Bars[0]], name = '6: Scratch'),
	Workspace(windawesome.monitors[0], TileLayout(masterAreaFactor = 0.6), [config.Bars[0]], name = '7: Manage'),
	Workspace(windawesome.monitors[1], TileLayout(masterAreaFactor = 0.6), [config.Bars[1]], name = '8: Code'),
	Workspace(windawesome.monitors[0], TileLayout(masterAreaFactor = 0.6), [],               name = '9: Desktop')
])

config.StartingWorkspaces = [config.Workspaces[0], config.Workspaces[7]]

config.Plugins = [
	ShortcutsManager()
]
