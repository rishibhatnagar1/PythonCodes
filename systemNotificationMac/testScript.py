
import gntp.notifier

growl.notify(
    noteType = "New Messages",
		title = "You have a new message",
		description = "A longer message description",
		icon = "http://example.com/icon.png",
		sticky = False,
		priority = 1,
		)
