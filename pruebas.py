from ordenes.mod1 import orden
import tkinter as tk

app = tk.Tk()
app.title("Burritos_Norteños")

class Burritos:
    def __init__(self):
        #Suma del dia
        self.totaldia = 0
        #Número de orden
        self.numpedido = 0
        # Listas
            #Ordenes
        self.ordenes = []
            # "" v. numérica
        self.lista = []
            #Conteo de burros
        self.lista_asa = []
        self.lista_coch = []
        self.lista_des = []
        #Pedidos de botones
        self.asa = 0
        self.coch = 0
        self.des = 0
        self.ado = 0
    #Botones agregar
    def ag_coch(self):
        self.coch += 1
        cochina_label["text"] = f'Burros de cochina: {self.coch}'
    def ag_asa(self):
        self.asa += 1
        asa_label["text"] = f'Burros de asada: {self.asa}'
    def ag_des(self):
        self.des += 1
        des_label["text"] = f'Burros de deshebrada: {self.des}'
    #Botones quitar
    def qu_coch(self):
        self.coch -= 1
        cochina_label["text"] = f'Burros de cochina: {self.coch}'
    def qu_asa(self):
        self.asa -= 1
        asa_label["text"] = f'Burros de asada: {self.asa}'
    def qu_des(self):
        self.des -= 1
        des_label["text"] = f'Burros de deshebrada: {self.des}'
    #Orden
    def tomar_orden(self):
        #Cantidad a cobrar
        pedido = orden(asa=self.asa, des=self.des, coch=self.coch)
        #Orden por escrito
        temp = f"Asada: {self.asa} Cochinita: {self.coch} Deshebrada: {self.des} Total: {pedido} Número de orden {self.numpedido}"
        #Agregar orden a la lista de ordenes
        self.ordenes.append(temp)
        #Establecer número de pedido
        self.numpedido += 1
        #Agregar a la listas
            #Lista pedidos (activos y v. numérica)
        ordenes_activas.insert(tk.END, f'Asada: {self.asa} Cochinita: {self.coch} Deshebrada: {self.des} Total: {pedido}  Número de orden: {self.numpedido}')
        self.lista.append([self.asa, self.coch, self.des, pedido])
            #listas de burros
        self.lista_asa.append(self.asa)
        self.lista_coch.append(self.coch)
        self.lista_des.append(self.des)
        #Contadores volviendo a 0
        self.clear()
    def mod_orden(self):
        index = ordenes_activas.curselection()
        if index:
            selected = ordenes_activas.get(index)
            n_pedido = int(index[-1])
            edited = f"Asada: {self.lista[n_pedido][0] + self.asa} Cochinita: {self.lista[n_pedido][1] + self.coch} Deshebrada: {self.lista[n_pedido][2] + self.des} Total: {self.lista[n_pedido][3] + orden(asa=self.asa, des=self.des, coch=self.coch)}  Número de orden: {n_pedido + 1}"
            ordenes_activas.delete(index)
            ordenes_activas.insert(index, edited)
            self.ordenes[n_pedido] = edited
            self.lista[n_pedido] = [self.lista[n_pedido][0] + self.asa, self.lista[n_pedido][1] + self.coch, self.lista[n_pedido][2] + self.des, self.lista[n_pedido][3] + orden(asa=self.asa, des=self.des, coch=self.coch)]
        self.clear()
    def clear(self):
        self.coch = 0
        cochina_label["text"] = f'Burros de cochina: {self.coch}'
        self.asa = 0
        asa_label["text"] = f'Burros de asada: {self.asa}'
        self.des = 0
        des_label["text"] = f'Burros de deshebrada: {self.des}'
    def fin_orden(self):
        index = ordenes_activas.curselection()
        if index:
            ordenes_activas.delete(index)
    def borrar(self):
        index = ordenes_activas.curselection()
        if index:
            selected = ordenes_activas.get(index)
            n_pedido = int(index[-1])
            edited = 'Pedido eliminado'
            ordenes_activas.delete(index)
            self.ordenes[n_pedido] = edited
            self.lista[n_pedido] = [0, 0, 0, 0]
        self.clear()
    def cierre(self): #Debe tener suma de self.ordenes[3], crear la listbox abajo
        final_dia_label.pack()
        final_dia.pack()
        ordenes_activas.insert(tk.END, self.totaldia)
        ordenes_activas.pack_forget()
        ordenes_activas_label.pack_forget()
        for ped in self.lista:
            self.totaldia += int(ped[-1])
        for ord in self.ordenes:
            final_dia.insert(tk.END, ord)
        final_dia.insert(tk.END, f'El total del día fue: {self.totaldia}')
        self.clear()


dia = Burritos()
total_dia = 0


nombree = tk.Label(app, text="Bienvenido al robot Burrito3000", font=('Helvetiva', 16))
nombree.pack()

#Frames
main_agregar = tk.Frame(app)
main_agregar.pack()
    #Frame agregar o quitar burros
botones_ordenar = tk.Frame(main_agregar)
botones_ordenar.pack(side=tk.LEFT)
        #Frames burros
seccion_ordenar = tk.Label(botones_ordenar, text="Ingresa burritos", font=('Helvetiva', 16))
seccion_ordenar.pack()

asa_ordenar = tk.Frame(botones_ordenar)
asa_ordenar.pack()

coch_ordenar = tk.Frame(botones_ordenar)
coch_ordenar.pack()

des_ordenar = tk.Frame(botones_ordenar)
des_ordenar.pack()

    #Frame conteo burritos
n_burro_frame = tk.Frame(main_agregar)
n_burro_frame.pack(side=tk.RIGHT)
    #Frame ordenar o limpiar
burriros = tk.Frame(app)
burriros.pack()


#Botones

boton_ag_asa = tk.Button(asa_ordenar, text='agregar asada', command=dia.ag_asa, font=('Helvetiva', 10))
boton_ag_asa.pack(side=tk.LEFT, padx=5)
boton_qu_asa = tk.Button(asa_ordenar, text='-asada', command=dia.qu_asa, font=('Helvetiva', 10))
boton_qu_asa.pack(side=tk.RIGHT, padx=3)
asa_label = tk.Label(n_burro_frame, text=f' Burros de asada: {dia.asa}', font=('Helvetiva', 10))
asa_label.pack(padx=5)

boton_ag_coch = tk.Button(coch_ordenar, text='agregar cochinita', command=dia.ag_coch, font=('Helvetiva', 10))
boton_ag_coch.pack(side=tk.LEFT, padx=5)
boton_qu_coch = tk.Button(coch_ordenar, text='-cochinita', command=dia.qu_coch, font=('Helvetiva', 10))
boton_qu_coch.pack(side=tk.RIGHT, padx=3)
cochina_label = tk.Label(n_burro_frame, text=f' Burros de cochina: {dia.coch}', font=('Helvetiva', 10))
cochina_label.pack(padx=5)

boton_ag_des = tk.Button(des_ordenar, text='agregar deshebrada', command=dia.ag_des, font=('Helvetiva', 10))
boton_ag_des.pack(side=tk.LEFT, padx=5)
boton_qu_des = tk.Button(des_ordenar, text='-deshebrada', command=dia.qu_des, font=('Helvetiva', 10))
boton_qu_des.pack(side=tk.RIGHT, padx=3)
des_label = tk.Label(n_burro_frame, text=f' Burros de asada: {dia.des}', font=('Helvetiva', 10))
des_label.pack(padx=5)

    #Ordenar
boton_ordenar = tk.Button(burriros, text='Agregar orden', command=dia.tomar_orden, font=('Helvetiva', 13))
boton_ordenar.pack(side=tk.LEFT, padx=6, pady=6)
    #Limpiar valores
boton_limpiar = tk.Button(burriros, text='Limpiar', command=dia.clear, font=('Helvetiva', 10))
boton_limpiar.pack(side=tk.RIGHT, padx=5, pady=5)

    #Boton modificar ordenes
boton_mod = tk.Button(app, text='Modificar orden seleccionada', command=dia.mod_orden, font=('Helvetiva', 13))
boton_mod.pack()
    #Finalizar orden
boton_fin = tk.Button(app, text='Finalizar orden seleccionada', command=dia.fin_orden, font=('Helvetiva', 13))
boton_fin.pack()
    #Borrar orden
boton_borrar = tk.Button(app, text='Borrar orden seleccionada', command=dia.borrar, font=('Helvetica', 11))
boton_borrar.pack()
    #Boton cerrar dia
boton_cerrar = tk.Button(app, text='Cerrar el día', command=dia.cierre)
boton_cerrar.pack(padx=7, pady=7)

#Listbox (ordenes)
ordenes_activas_label = tk.Label(app, text='Órdenes activas', font=('Helvetiva', 16))
ordenes_activas_label.pack()

ordenes_activas = tk.Listbox(app, selectmode=tk.SINGLE, width=80, height=30, font=('Helvetiva', 12))
ordenes_activas.pack()

#Listbox (final del día)
final_dia_label = tk.Label(app, text='Ordenes finales', font=('Helvetiva', 16))
final_dia = tk.Listbox(app, selectmode=tk.SINGLE, width=80, height=30, font=('Helvetiva', 12))


app.mainloop()
