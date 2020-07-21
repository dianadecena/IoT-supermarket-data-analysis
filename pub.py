import ssl
import sys
import time
import paho.mqtt.client
import paho.mqtt.publish
import json
import datetime 
import random 
import numpy as np

class publicador:
    
    def __init__(self, connection_db_ventas, connection_db_inventario, nombre):
        #se crea el cliente 
        self.client = paho.mqtt.client.Client(nombre, False)
        self.connection_db_ventas = connection_db_ventas
        self.connection_db_inventario = connection_db_inventario
        self.activar_alarma_estante = False
        self.alarma_activada = 0
        
    def conectar_dispositivo(self):
        #se conecta al host publico de HiveMQ usando qos=2 para hacer que 
        #la informacion llegue exactamente una vez y así evitar errores cuando se guarden en la base de datos
        host = "broker.hivemq.com"
        self.client.qos = 2
        self.client.connect(host=host)

    def enviar_mensaje(self, sucursal, producto, cantidad, id_estante, hora):
        payload = {
                "id_producto": producto,
                "cantidad": cantidad,
                "id_estante": id_estante,
                "sucursal": sucursal,
                "hora": str(hora)
            }
        print(payload)
        self.client.publish(sucursal+'/estantes/'+str(id_estante),json.dumps(payload),qos=2)
        time.sleep(0.5)

    def enviar_mensaje_factura(self, sucur, no_cuenta, id_cliente, banco, sucursal, cont_factura, total, hora):
        payload = {
                "no_cuenta": no_cuenta,
                "id_cliente": id_cliente,
                "banco": banco,
                "sucursal": sucursal,
                "cont_factura": cont_factura,
                "total": str(total),
                "hora": str(hora)
            }
        self.client.publish(sucur+'/facturas',json.dumps(payload),qos=2)
        time.sleep(0.5)

    def enviar_mensaje_detalles(self, sucur, cont_factura, id_producto, cantidad, precio):
        payload = {
                "cont_factura": cont_factura,
                "id_producto": id_producto,
                "cantidad": cantidad,
                "precio": precio
            }
        self.client.publish(sucur+'/detalles',json.dumps(payload),qos=2)
        time.sleep(0.5)

    def enviar_mensaje_clientes(self, sucur, id_cliente, nombre, apellido, telefono, direccion):
        payload = {
                "id_cliente": id_cliente,
                "nombre": nombre,
                "apellido": apellido,
                "telefono": telefono,
                "direccion": direccion
            }
        self.client.publish(sucur+'/clientes',json.dumps(payload),qos=2)
        time.sleep(0.5)

    def enviar_mensaje_visitas(self, sucur, no_visita, no_cuenta, id_cliente, sucursal, hora):
        payload = {
                "no_visita": no_visita,
                "no_cuenta": no_cuenta,
                "id_cliente": id_cliente,
                "sucursal": sucursal,
                "hora": str(hora)
            }
        self.client.publish(sucur+'/visitas',json.dumps(payload),qos=2)
        time.sleep(0.5)
        
    def enviar_mensaje_sensor(self, sucursal, id_cliente, id_sucursal):
        payload = {
                "sucursal": sucursal,
                "id_cliente": id_cliente,
                "id_sucursal": id_sucursal
            }
        print(payload)
        self.client.publish(sucursal+'/sensores',json.dumps(payload),qos=2)
        time.sleep(0.5)

    def enviar_mensaje_llenar(self, sucur, id_estante, hora):
        payload = {
                "id_estante": id_estante,
                "hora": str(hora)
            }
        print(payload)
        self.client.publish(sucur+'/llenar',json.dumps(payload),qos=2)
        time.sleep(0.5)

    def enviar_mensaje_charcuteria(self, sucur, accion, id_cliente):
        payload = {
                "accion": accion,
                "id_cliente": id_cliente
            }
        print(payload)
        self.client.publish(sucur+'/charcuteria',json.dumps(payload),qos=2)
        time.sleep(0.5)

    def enviar_mensaje_fila(self, sucur, accion, no_fila, id_cliente, id_sucursal):
        payload = {
                "accion": accion,
                "no_fila": no_fila,
                "id_cliente": id_cliente,
                "id_sucursal": id_sucursal
            }
        print(payload)
        self.client.publish(sucur+'/charcuteria',json.dumps(payload),qos=2)
        time.sleep(0.5)

    def on_connect(self, client, userdata, flags, rc):    
        print('se ha suscrito correctamente (%s)' % client._client_id)
        #el dispositivo se suscribe al canal por donde se notificará que se debe activar la alarma 
        #de alguno o todos los dispositivos 
        self.client.subscribe(topic='sucursal1/alarmas/#',qos=1)
        self.client.subscribe(topic='sucursal2/alarmas/#',qos=1)

    def on_message(self, client, userdata, message):   
        a = json.loads(message.payload)
        print(a) 
        self.activar_alarma(a["id_estante"])
        if a["id_cliente"] != None:
            self.activar_alarma_sensor(a)
    
    def conectar_suscriptor(self):
        self.client = paho.mqtt.client.Client()
        host = "broker.hivemq.com"
        self.client.on_connect = self.on_connect
        self.client.message_callback_add('sucursal1/alarmas/#', self.on_message)  
        self.client.message_callback_add('sucursal2/alarmas/#', self.on_message)  
        self.client.connect(host=host) 
        self.client.loop_forever()
    
    def activar_alarma(self, id_estante):
        print('----------------------------------------------')
        print('    alarma activada estante: '+str(id_estante) )
        print('----------------------------------------------')
        self.activar_alarma_estante = True 
        
    def activar_alarma_sensor(self, a):
        self.alarma_activada = a["id_cliente"]
        
    def verificar_cliente_programa(self, id_cliente):
        cur = self.connection_db_ventas.cursor()
        cur.execute("SELECT verificar_pertenece_programa(%s)", (id_cliente,))
        self.connection_db_ventas.commit()
        pertenece = cur.fetchone()[0]
        cur.close()
        return pertenece 
    
    def pick_choice(self, lista):
        opciones = lista
        decision = random.choice(opciones)
        return decision

    def verificar_si_en_cola(self, id_cliente):
        cur = self.connection_db_ventas.cursor()
        cur.execute("SELECT verificar_cola(%s)", (id_cliente,))
        self.connection_db_ventas.commit()
        is_en_cola = cur.fetchone()[0]
        cur.close()
        return is_en_cola

    def elegir_producto(self, id_estante):
        cur = self.connection_db_inventario.cursor()
        cur.execute("SELECT nombre FROM producto_asignado AS A INNER JOIN producto AS P ON A.id_producto = P.id_producto WHERE id_estante = %s", (id_estante,))
        self.connection_db_inventario.commit()
        productos = cur.fetchall()
        cur.close()
        return productos
    
    def get_id_producto(self, producto):
        cur = self.connection_db_ventas.cursor()
        cur.execute("SELECT id_producto FROM producto WHERE nombre = %s", (producto,))
        self.connection_db_ventas.commit()
        id_producto = cur.fetchone()[0]
        cur.close()
        return id_producto

    def obtener_cantidad_restante(self, id_producto):
        cur = self.connection_db_inventario.cursor()
        cur.execute("SELECT cantidad_restante FROM producto_asignado WHERE id_producto = %s", (id_producto,))
        self.connection_db_inventario.commit()
        cant = cur.fetchone()[0]
        cur.close()
        return cant

    def obtener_precio(self, id_producto):
        cur = self.connection_db_ventas.cursor()
        cur.execute("SELECT precio FROM cambio_precio WHERE id_producto = %s", (id_producto,))
        self.connection_db_ventas.commit()
        precio = cur.fetchone()[0]
        cur.close()
        return precio

    def verificar_cliente(self, id_cliente):
        cur = self.connection_db_ventas.cursor()
        cur.execute("SELECT verificar_cliente(%s)", (id_cliente,))
        self.connection_db_ventas.commit()
        is_cliente = cur.fetchone()[0]
        cur.close()
        return is_cliente

    def obtener_pasillos(self, sucursal):
        cur = self.connection_db_inventario.cursor()
        cur.execute("SELECT no_pasillo FROM estante_inteligente WHERE id_sucursal = %s", (sucursal,))
        self.connection_db_inventario.commit()
        pasillos = cur.fetchall()
        cur.close()
        return pasillos 

    def obtener_estantes(self, sucursal, pasillo):
        cur = self.connection_db_inventario.cursor()
        cur.execute("SELECT id_estante FROM estante_inteligente WHERE id_sucursal = %s AND no_pasillo = %s AND id_estante NOT IN (2, 10)", (sucursal, pasillo,))
        self.connection_db_inventario.commit()
        estantes = cur.fetchall()
        cur.close()
        return estantes

    def iniciar_sucursal(self):
        #se carga el json con la data de los clientes
        with open('Data/clientes.json') as f:
            clientes = json.load(f)

        #se inicializan los contadores  
        day = 0
        no_fila = 0
        cont_tiempo = 0
        cont_factura = 0
        no_visita = 0
        cont_horas = 0
        horas = 0
        entran_mas = 0

        #se establece la hora inicial en que empieza a funcionar
        hora = datetime.datetime.now()

        #se elige una cantidad random de personas que van a entrar 
        cantidad = random.randint(30, 40)
        #aquí se guardan los indices de los clientes dentro de una sucursal (los que tienen en el json) para poder acceder a estos después
        indices = []

        #se eligen varios varios valores aleatorios según la cantidad de clientes que va a entrar 
        for i in range(cantidad):
            values = list(range(0, len(clientes)))
            for j in indices:
                values.remove(j)
            #se elige un valor random 
            r1 = random.choice(values)
            #se guardan los indices seleccionados 
            indices.append(r1)
            
        #se inicializa el contador de los clientes 
        for i in range(0, len(clientes)):
            clientes[i]["contador"] = 0
            clientes[i]["sucursal"] = 0

        while(day < 30): 
            #se ejecuta el proceso de compra para cada cliente cuyo indices en el json este en el array indices 
            for i in indices:
                #se actualiza el contador cuando entra por primera vez
                clientes[i]["contador"] += 1 
                #se cuenta cuando pase una vuelta completa del for
                if no_visita > 6:
                    cont_tiempo += 1
                    cont_horas += 1
                #actualizamos el estado de la persona 
                cliente_actual = json.dumps(clientes[i]["id_cliente"])
                print("Cliente id:", cliente_actual, " Indice: ", i)
                print("Indices: "+str(indices))
                #si el contador del cliente es igual a 1 es porque entro por primera vez
                if clientes[i]["contador"] == 1:
                    #aumentar contador de visitas 
                    no_visita += 1
                    #se elige de manera aleatoria la sucursal en la que está 
                    sucursal = random.randint(1, 2)
                    clientes[i]["sucursal"] = sucursal
                    #la cámara capta su rostro y verifica si pertenece al programa de fidelidad 
                    if self.verificar_cliente_programa(clientes[i]["id_cliente"]) == True:
                        #si pertenece se cuenta su visita 
                        hora = datetime.datetime.now()
                        if sucursal == 1:
                            self.enviar_mensaje_visitas('sucursal1', no_visita, 1, clientes[i]["id_cliente"], sucursal, hora)
                        else:
                            self.enviar_mensaje_visitas('sucursal2', no_visita, 1, clientes[i]["id_cliente"], sucursal, hora)
                    else:
                        #si no pertenece se cuenta la visita de un desconocido 
                        hora = datetime.datetime.now()
                        if sucursal == 1:
                            self.enviar_mensaje_visitas('sucursal1', no_visita, 0, 0, sucursal, hora)
                        else:
                            self.enviar_mensaje_visitas('sucursal2', no_visita, 0, 0, sucursal, hora)
                    #se inicializa el carrito donde guardaran los productos 
                    clientes[i]["carrito"] = []
                    #se elige de manera aleatoria si irá a un pasillo o a buscar un ticket para que lo atiendan el la charcutería
                    lista = list(["ir a un pasillo", "ir a la charcutería"])
                    decision = self.pick_choice(lista)
                    print("El cliente va a "+str(decision))
                    #se actualiza el estado del cliente
                    clientes[i]["currently"] = decision
                else: 
                    #si no es la primera vez que entra al supermercado se verifica si el cliente está en la cola para la charcutería 
                    sucursal = clientes[i]["sucursal"]
                    horas += 1
                    print("HORAS:"+str(horas))
                    if self.verificar_si_en_cola(clientes[i]["id_cliente"]) == True:
                        #si está en la cola se verifica si la alarma de su sensor se activó para que lo atiendan 
                        if sucursal == 1:
                            self.enviar_mensaje_sensor('sucursal1', clientes[i]["id_cliente"], clientes[i]["sucursal"])
                        else:
                            self.enviar_mensaje_sensor('sucursal2', clientes[i]["id_cliente"], clientes[i]["sucursal"])
                        if self.alarma_activada == clientes[i]["id_cliente"]:
                            #va a ser atendido en la charcutería
                            #se borra de la fila el cliente
                            if sucursal == 1:
                                self.enviar_mensaje_charcuteria('sucursal1', 'borrar', clientes[i]["id_cliente"])
                            else:
                                self.enviar_mensaje_charcuteria('sucursal2', 'borrar', clientes[i]["id_cliente"])
                            #actualizar fila 
                            if sucursal == 1:
                                self.enviar_mensaje_charcuteria('sucursal1', 'update', clientes[i]["id_cliente"])
                            else:
                                self.enviar_mensaje_charcuteria('sucursal2', 'update', clientes[i]["id_cliente"])
                            #el cliente elige el producto de la charcutería 
                            if sucursal == 1:
                                estante = 2
                                producto = self.elegir_producto(estante)
                            else:
                                estante = 10
                                producto = self.elegir_producto(estante)
                            #se elige aleatoriamente el producto
                            print("El cliente elige el producto: "+str(producto))
                            id_producto = self.get_id_producto(producto)
                            #se busca cuánta cantidad restante queda de ese producto 
                            cant = self.obtener_cantidad_restante(id_producto)
                            print(cant)
                            #si la cantidad es igual a cero el producto se acabó
                            if cant == 0:
                                print("El producto se acabó")
                            else:
                                #se elige de manera alteatoria cuánta cantidad de ese producto agarrá
                                cantidad = random.randint(1, 10)
                                print("El cliente compra "+str(cantidad)+" de este producto")
                                #se busca el precio de ese producto
                                precio = self.obtener_precio(id_producto)
                                #se mete el producto en su carrito
                                for k in range(0, len(clientes[i]["carrito"])):
                                    if producto == clientes[i]["carrito"][k]["nombre"]:
                                        print("ËNTRO")
                                        cantidad = int(clientes[i]["carrito"][k]["cantidad"]) + cantidad
                                        print("VALOR: "+str(k))
                                        clientes[i]["carrito"].remove(clientes[i]["carrito"][k])
                                        break
                                clientes[i]["carrito"].append({
                                    "nombre": producto,
                                    "cantidad": str(cantidad),
                                    "id_producto": id_producto,
                                    "precio": str(precio)
                                })
                                id_estante = int(''.join(map(str, estante)))
                                #se publica el mensaje en el canal correspondiente para indicar que se ha quitado cantidad de un producto en un estante 
                                if sucursal == 1:
                                    hora = datetime.datetime.now()
                                    if cont_horas > 1:
                                        print("AUMENTO HORAS")
                                        hora = hora + datetime.timedelta(hours=horas)
                                        if day >= 1:
                                            hora = hora + datetime.timedelta(days=day)
                                    self.enviar_mensaje('sucursal1', id_producto, cantidad, id_estante, hora)
                                else:
                                    hora = datetime.datetime.now() 
                                    if cont_horas > 1:
                                        print("AUMENTO HORAS")
                                        hora = hora + datetime.timedelta(hours=horas)
                                        if day >= 1:
                                            hora = hora + datetime.timedelta(days=day)
                                    self.enviar_mensaje('sucursal2', id_producto, cantidad, id_estante, hora)
                                time.sleep(3)
                                #si la alarma de un estante se activó los empleados vuelven a llenar el estante 
                                if self.activar_alarma_estante == True:
                                    hora = datetime.datetime.now()
                                    if cont_horas > 1:
                                        print("AUMENTO HORAS")
                                        hora = hora + datetime.timedelta(hours=horas)
                                        if day >= 1:
                                            hora = hora + datetime.timedelta(days=day)
                                    if sucursal == 1:
                                        self.enviar_mensaje_llenar('sucursal1', id_estante, hora)
                                    else:
                                        self.enviar_mensaje_llenar('sucursal2', id_estante, hora)
                                    self.activar_alarma_estante = False
                        else:
                            #si todavía no es su turno de va a otro pasillo 
                            clientes[i]["currently"] = "ir a un pasillo"
                    else:
                        #si no está en la cola de la charcutería va a un pasillo 
                        clientes[i]["currently"] = "ir a un pasillo"
                if clientes[i]["currently"] == "ir a la charcutería":
                    #el cliente agarra un sensor que puede tener en su carrito que le avisará cuando sea su turno para que lo atiendan 
                    no_fila += 1
                    #si no está registrado se guarda su información en la bd
                    if self.verificar_cliente(clientes[i]["id_cliente"]) == False:
                        if sucursal == 1:
                            self.enviar_mensaje_clientes('sucursal1', clientes[i]["id_cliente"], clientes[i]["nombre"], clientes[i]["apellido"], clientes[i]["telefono"], clientes[i]["direccion"])
                        else:
                            self.enviar_mensaje_clientes('sucursal2', clientes[i]["id_cliente"], clientes[i]["nombre"], clientes[i]["apellido"], clientes[i]["telefono"], clientes[i]["direccion"])
                        if sucursal == 1:
                            self.enviar_mensaje_fila('sucursal1', 'insertar', no_fila, clientes[i]["id_cliente"], clientes[i]["sucursal"])
                        else:
                            self.enviar_mensaje_fila('sucursal2', 'insertar', no_fila, clientes[i]["id_cliente"], clientes[i]["sucursal"])
                    #si está registrado se procede a guardarlo en la fila
                    else:
                        if sucursal == 1:
                            self.enviar_mensaje_fila('sucursal1', 'insertar', no_fila, clientes[i]["id_cliente"], clientes[i]["sucursal"])
                        else:
                            self.enviar_mensaje_fila('sucursal2', 'insertar', no_fila, clientes[i]["id_cliente"], clientes[i]["sucursal"])
                    #se publica el mensaje en el canal correspondiente para indicar que se agregó otro cliente a la cola
                    if sucursal == 1:
                        self.enviar_mensaje_sensor('sucursal1', clientes[i]["id_cliente"], clientes[i]["sucursal"])
                    else:
                        self.enviar_mensaje_sensor('sucursal2', clientes[i]["id_cliente"], clientes[i]["sucursal"])
                    time.sleep(3)
                    #si el estado del cliente es ir a un pasillo o seguir viendo
                if clientes[i]["currently"] == "ir a un pasillo" or clientes[i]["currently"] == "sigue viendo":
                    #se elige de manera random a que pasillo se dirigirá el cliente
                    pasillo = random.choice(self.obtener_pasillos(sucursal))
                    pasillo = int(''.join(map(str, pasillo)))
                    print("El cliente se dirige al pasillo "+str(pasillo))
                    #se elige de manera aleatoria el estante al que se dirigirá el cliente 
                    estante = random.choice(self.obtener_estantes(sucursal, pasillo))
                    print("El cliente se dirige al estante "+str(estante))
                    #se elige de manera alteatoria que producto de ese estante agarrará
                    producto = random.choice(self.elegir_producto(estante))
                    print("El cliente elige el producto: "+str(producto))
                    id_producto = self.get_id_producto(producto)
                    #se elige de manera alteatoria cuánta cantidad de ese producto agarrá
                    cant = self.obtener_cantidad_restante(id_producto)
                    print(cant)
                    #si la cantidad es 0 el producto se acabó
                    if cant == 0:
                        print("El producto se acabó")
                    else:
                        #se elige el manera aleatoria la cantidad que agarrará
                        cantidad = random.randint(1, 10)
                        print("El cliente agarra "+str(cantidad)+" de este producto")
                        #se elige de manera aleatoria si el cliente dejará el producto o lo comprará
                        lista = list(["lo compra"])
                        decision = self.pick_choice(lista)
                        print("El cliente "+str(decision))
                        if(decision == "lo compra"):
                            #se busca el precio del producto
                            precio = self.obtener_precio(id_producto)
                            for k in range(0, len(clientes[i]["carrito"])):
                                if producto == clientes[i]["carrito"][k]["nombre"]:
                                    print("ENTRO")
                                    cantidad = int(clientes[i]["carrito"][k]["cantidad"]) + cantidad
                                    print("VALOR: "+str(k))
                                    clientes[i]["carrito"].remove(clientes[i]["carrito"][k])
                                    break
                            clientes[i]["carrito"].append({
                                "nombre": producto,
                                "cantidad": str(cantidad),
                                "id_producto": id_producto,
                                "precio": str(precio)
                            })
                            #cuando se agarra un producto de un estante se hace un publish en el canal 
                            #para verificar que no queda el 20% de los productos 
                            #si queda el 20% se activa una alarma y los empleados lo vuelven a llenar
                            id_estante = int(''.join(map(str, estante)))
                            if sucursal == 1:
                                hora = datetime.datetime.now() 
                                if cont_horas > 1:
                                        print("AUMENTO HORAS")
                                        hora = hora + datetime.timedelta(hours=horas)
                                        if day >= 1:
                                            hora = hora + datetime.timedelta(days=day)
                                self.enviar_mensaje('sucursal1', id_producto, cantidad, id_estante, hora)
                            else:
                                hora = datetime.datetime.now()
                                if cont_horas > 1:
                                        print("AUMENTO HORAS")
                                        hora = hora + datetime.timedelta(hours=horas)
                                        if day >= 1:
                                            hora = hora + datetime.timedelta(days=day)
                                self.enviar_mensaje('sucursal2', id_producto, cantidad, id_estante, hora)
                            time.sleep(3)
                            if self.activar_alarma_estante == True:
                                hora = datetime.datetime.now()
                                if cont_horas > 1:
                                        print("AUMENTO HORAS")
                                        hora = hora + datetime.timedelta(hours=horas)
                                        if day >= 1:
                                            hora = hora + datetime.timedelta(days=day)
                                if sucursal == 1:
                                    self.enviar_mensaje_llenar('sucursal1', id_estante, hora)
                                else:
                                    self.enviar_mensaje_llenar('sucursal2', id_estante, hora)
                                self.activar_alarma_estante = False
                #se elige de manera aleatoria si el cliente sigue viendo más cosas o va a pagar
                if len(clientes[i]["carrito"]) > 0:
                    lista = list(["va a pagar"])
                    decision = self.pick_choice(lista)
                    print("El cliente "+str(decision))
                    clientes[i]["currently"] = decision
                else:
                    lista = list(["sigue viendo", "se va"])
                    decision = self.pick_choice(lista)
                    print("El cliente "+str(decision))
                    clientes[i]["currently"] = decision
                #si el cliente se va se quita su indice del array
                if clientes[i]["currently"] == "se va":
                    indices.remove(i)
                    if len(indices) == 0:
                        entran_mas += 1
                    if self.verificar_si_en_cola(clientes[i]["id_cliente"]) == True:
                        #se borra de la fila el cliente
                        if sucursal == 1:
                            self.enviar_mensaje_charcuteria('sucursal1', 'borrar', clientes[i]["id_cliente"])
                        else:
                            self.enviar_mensaje_charcuteria('sucursal2', 'borrar', clientes[i]["id_cliente"])
                        #actualizar fila 
                        if sucursal == 1:
                            self.enviar_mensaje_charcuteria('sucursal1', 'update', clientes[i]["id_cliente"])
                        else:
                            self.enviar_mensaje_charcuteria('sucursal2', 'update', clientes[i]["id_cliente"])
                #si el cliente va a pagar se hace todos el proceso de pago
                if clientes[i]["currently"] == "va a pagar":
                    total = 0 
                    indices.remove(i)
                    if len(indices) == 0:
                        entran_mas += 1
                    #se verifica si el cliente está registrado
                    if self.verificar_cliente(clientes[i]["id_cliente"]) == True:
                        #si es cliente regular 
                        cont_factura += 1
                        print("FACTURA: "+str(cont_factura))
                        for index in range(0, len(clientes[i]["carrito"])):   
                            #se calcula el total
                            precio = self.obtener_precio((clientes[i]["carrito"][index]["id_producto"]))
                            total += int(clientes[i]["carrito"][index]["cantidad"])*precio
                        print("El total a pagar es: "+str(total))
                        #se verifica si pertenece al programa
                        lista = list(["Banesco", "Provincial", "Mercantil"])
                        banco = self.pick_choice(lista)
                        hora = datetime.datetime.now()
                        if cont_horas > 1:
                            print("AUMENTO HORAS")
                            hora = hora + datetime.timedelta(hours=horas)
                            if day >= 1:
                                hora = hora + datetime.timedelta(days=day)
                        if self.verificar_cliente_programa(clientes[i]["id_cliente"]) == True:
                            num = 1
                        else:
                            num = 0
                        if sucursal == 1:
                            self.enviar_mensaje_factura('sucursal1', num, clientes[i]["id_cliente"], banco, sucursal, cont_factura, total, hora)
                        else:
                            self.enviar_mensaje_factura('sucursal2', num, clientes[i]["id_cliente"], banco, sucursal, cont_factura, total, hora)
                        time.sleep(3)
                        if sucursal == 1:
                            for index in range(0, len(clientes[i]["carrito"])):  
                                self.enviar_mensaje_detalles('sucursal1', cont_factura, clientes[i]["carrito"][index]["id_producto"], clientes[i]["carrito"][index]["cantidad"], clientes[i]["carrito"][index]["precio"])
                        else:
                            for index in range(0, len(clientes[i]["carrito"])):  
                                self.enviar_mensaje_detalles('sucursal2', cont_factura, clientes[i]["carrito"][index]["id_producto"], clientes[i]["carrito"][index]["cantidad"], clientes[i]["carrito"][index]["precio"])
                        time.sleep(3)
                    else:
                        cont_factura += 1
                        print("FACTURA: "+str(cont_factura))
                        #si no está registrado se registra
                        if sucursal == 1:
                            self.enviar_mensaje_clientes('sucursal1', clientes[i]["id_cliente"], clientes[i]["nombre"], clientes[i]["apellido"], clientes[i]["telefono"], clientes[i]["direccion"])
                        else:
                            self.enviar_mensaje_clientes('sucursal2', clientes[i]["id_cliente"], clientes[i]["nombre"], clientes[i]["apellido"], clientes[i]["telefono"], clientes[i]["direccion"])
                        #se calcula el total a pagar
                        for index in range(0, len(clientes[i]["carrito"])):   
                            precio = self.obtener_precio((clientes[i]["carrito"][index]["id_producto"]))
                            total += int(clientes[i]["carrito"][index]["cantidad"])*precio
                        print("El total a pagar es: "+str(total))
                        #se verifica si pertenece al programa de fidelidad
                        lista = list(["Banesco", "Provincial", "Mercantil"])
                        banco = self.pick_choice(lista)
                        hora = datetime.datetime.now() 
                        if cont_horas > 1:
                            print("AUMENTO HORAS")
                            hora = hora + datetime.timedelta(hours=1)
                            if day >= 1:
                                hora = hora + datetime.timedelta(days=day)
                        if self.verificar_cliente_programa(clientes[i]["id_cliente"]) == True:
                            num = 1
                        else:
                            num = 0
                        if sucursal == 1:
                            self.enviar_mensaje_factura('sucursal1', num, clientes[i]["id_cliente"], banco, sucursal, cont_factura, total, hora)
                        else:
                            self.enviar_mensaje_factura('sucursal1', num, clientes[i]["id_cliente"], banco, sucursal, cont_factura, total, hora)
                        time.sleep(3)
                        if sucursal == 1:
                            for index in range(0, len(clientes[i]["carrito"])):  
                                self.enviar_mensaje_detalles('sucursal1', cont_factura, clientes[i]["carrito"][index]["id_producto"], clientes[i]["carrito"][index]["cantidad"], clientes[i]["carrito"][index]["precio"])
                        else:
                            for index in range(0, len(clientes[i]["carrito"])):  
                                self.enviar_mensaje_detalles('sucursal2', cont_factura, clientes[i]["carrito"][index]["id_producto"], clientes[i]["carrito"][index]["cantidad"], clientes[i]["carrito"][index]["precio"])
                        time.sleep(3)
                if entran_mas == 1:
                    #decidir si entrarán más clientes
                    day += 1
                    entran_mas = 0
                    lista = list(["entran más clientes"])
                    decision = self.pick_choice(lista)
                    cont_tiempo = 0
                    print(decision)
                    if(decision == "entran más clientes"):
                        #se eligen varios varios valores aleatorios según la cantidad de clientes que va a entrar 
                        cantidad = random.randint(30, 40)
                        print("Cantidad: "+str(cantidad))
                        indices_aux = []
                        values = list(range(0, len(clientes)))#cantidad de clientes en total
                        for j in indices:
                            values.remove(j)
                        for i in range(cantidad):
                            for x in indices_aux:
                                if x in values:
                                    values.remove(x)
                            #se elige un valor random 
                            r1 = random.choice(values)
                            #se guardan los indices seleccionados en el array
                            indices.append(r1)
                            indices_aux.append(r1)
                        print("Entran los siguientes indices de clientes: "+str(indices))
                #si ya pasaron dos vueltas en el for se aumenta una hora 
                print("DIAS: "+str(day))
                time.sleep(3)

            

