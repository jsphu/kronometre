import FreeSimpleGUIWeb as sg
import time

sg.theme('DarkAmber')
layout = [
    [sg.Text("00:00:00.000", key="-TIMER-")],
    [sg.Button("▶️"),sg.Button("⏹️"),sg.Button("❌")]
]

window = sg.Window("Chronometer",
                   layout,
                   element_justification='c',
                   finalize=True
)

running = False
start_time = 0

# Event loop
while True:
    event, values = window.read(timeout=10)  # Refresh every 10ms
    if event == sg.WINDOW_CLOSED or event == "❌":
        break

    if event == "▶️":
        # Start button
        if not running:
            running = True
            window['▶️'].update(text="⏸️")
            start_time = time.time() - start_time  # Resume from stopped time
        # Stop button
        else:
            running = False
            window["▶️"].update("▶️")
            start_time = time.time() - start_time  # Store elapsed time

    # Reset button
    if event == "⏹️":
        running = False
        window["▶️"].update("▶️")
        start_time = 0
        window["-TIMER-"].update("00:00:00.000")

    if running:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        hours, minutes = divmod(minutes, 60)
        milliseconds = int((elapsed_time % 1) * 1000)  # Get milliseconds
        window["-TIMER-"].update(f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}")

window.close()
