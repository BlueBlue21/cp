import tkinter as tk

app = tk.Tk()

app.title("어두운")
app.config(
    cursor="none", background="black"
)  # 왜 config, configure 두개로 나뉨? 그리고 걍 app["cursor"] = "none" 해도 됨
app.attributes("-fullscreen", True)


def key_event(event):
    if event.keysym == "Escape":
        app.destroy()  # 부숴버리기 (exit는 위젯은 남긴다고 함)


app.bind("<KeyRelease>", key_event)
app.mainloop()
