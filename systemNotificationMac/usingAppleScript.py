import subprocess

applescript = """
display dialog "Some message goes here..." ¬
with title "This is a pop-up window" ¬
with icon caution ¬
buttons {"OK"}
"""

subprocess.call("osascript -e '{}'".format(applescript), shell=True)
