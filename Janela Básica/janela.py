import tkinter as tk

#cria janela principal
root = tk.Tk()

#cria um rótulo com a mensagem "Hello, World!"
message = tk.Label(root, text="Hello, World!")

#posiciona o rótulo na janela
message.pack()


#define o tamanho da janela e a posição inicial
root.geometry("300x200+50+50")

root.title("Minha Janela")

root.configure(bg="black")

root.bind("<Button-1>", lambda event: print(f"Clique do mouse na posição ({event.x}, {event.y})"))

root.bind("<Key>", lambda event: print(f"Tecla pressionada: {event.char}"))

#inicia o loop principal da janela
root.mainloop()