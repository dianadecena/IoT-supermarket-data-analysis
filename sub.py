import ssl
import sys
import psycopg2
import paho.mqtt.client
import paho.mqtt.publish
import json
import time 
from datetime import datetime

class suscriptor:

    def __init__(self, connection_db_ventas, connection_db_inventario):
        #se crea el cliente 
        self.client = paho.mqtt.client.Client()
        self.connection_db_ventas = connection_db_ventas
        self.connection_db_inventario = connection_db_inventario
        self.no_alarma = 0

    def on_connect(self, client, userdata, flags, rc):    
        print('connected (%s)' % client._client_id)
        #se suscribe al canal por donde los dispositivos reportan los valores de los contaminantes cada hora 
        client.subscribe(topic='sucursal1/estantes/#', qos = 2) 
        client.subscribe(topic='sucursal2/estantes/#', qos = 2) 
        client.subscribe(topic='sucursal1/sensores', qos = 2) 
        client.subscribe(topic='sucursal2/sensores', qos = 2) 
        client.subscribe(topic='sucursal1/facturas', qos = 2)
        client.subscribe(topic='sucursal2/facturas', qos = 2)  
        client.subscribe(topic='sucursal1/clientes', qos = 2)
        client.subscribe(topic='sucursal2/clientes', qos = 2)  
        client.subscribe(topic='sucursal1/visitas', qos = 2)
        client.subscribe(topic='sucursal2/visitas', qos = 2)  
        client.subscribe(topic='sucursal1/llenar', qos = 2)
        client.subscribe(topic='sucursal2/llenar', qos = 2)  
        client.subscribe(topic='sucursal1/charcuteria', qos = 2)
        client.subscribe(topic='sucursal2/charcuteria', qos = 2) 
        client.subscribe(topic='sucursal1/detalles', qos = 2)
        client.subscribe(topic='sucursal2/detalles', qos = 2) 

    def on_data_estante(self, client, userdata, message):  
        a = json.loads(message.payload)
        #imprimir los datos y guardar datos en la bd    
        print(a)  
        print('---------------------------------------------------------')
        self.guardar_datos(a)
        if self.check_estante(a) == True:
            self.enviar_alarma_estante(a)
        
    def on_data_sensor(self, client, userdata, message):  
        a = json.loads(message.payload)
        #imprimir los datos y guardar datos en la bd    
        print(a)  
        print('---------------------------------------------------------')
        cur = self.connection_db_ventas.cursor()
        cur.execute("SELECT id_cliente FROM cliente_charcuteria WHERE id_sucursal = %s ORDER BY no_fila ASC LIMIT 1", (a["id_sucursal"],))
        self.connection_db_ventas.commit()
        ids = cur.fetchall()
        cur.close()
        if a["id_cliente"] in ids:
            self.enviar_alarma_sensor(a["sucursal"], a["id_cliente"])
            
    def check_estante(self, a):
        cur = self.connection_db_inventario.cursor()
        cur.execute("SELECT verificar_cantidad(%s)", (a["id_estante"],))
        self.connection_db_inventario.commit()
        activar = cur.fetchone()[0]
        cur.close()
        return activar 

    def on_data_facturas(self, client, userdata, message):  
        a = json.loads(message.payload)
        #imprimir los datos y guardar datos en la bd    
        if a["no_cuenta"] == 1:
            cur = self.connection_db_ventas.cursor()
            cur.execute("SELECT realizar_pago((SELECT no_cuenta FROM cuenta_programa_fidelidad WHERE id_cliente = %s), %s, %s, %s, %s, %s, %s, %s, %s)", (a["id_cliente"], a["id_cliente"], a["banco"], a["sucursal"], a["cont_factura"], int(''.join(map(str, a["total"]))), 0, int(''.join(map(str, a["total"]))), a["hora"],))
            self.connection_db_ventas.commit()
            cur.close()
        else:
            cur = self.connection_db_ventas.cursor()
            cur.execute("SELECT realizar_pago(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (0, a["id_cliente"], a["banco"], a["sucursal"], a["cont_factura"], int(''.join(map(str, a["total"]))), 0, int(''.join(map(str, a["total"]))), a["hora"],))
            self.connection_db_ventas.commit()
            cur.close()

    def on_data_detalles(self, client, userdata, message):  
        a = json.loads(message.payload)

        cur = self.connection_db_ventas.cursor()
        cur.execute("INSERT INTO detalle_factura(id_factura, id_producto, cantidad, subtotal) VALUES (%s, %s, %s, %s)", (a["cont_factura"], a["id_producto"], a["cantidad"], int(a["precio"])*int(a["cantidad"])),)
        self.connection_db_ventas.commit()
        cur.close()

    def on_data_clientes(self, client, userdata, message):  
        a = json.loads(message.payload)

        cur = self.connection_db_ventas.cursor()
        cur.execute("INSERT INTO cliente(id_cliente, nombre, apellido, telefono, direccion) VALUES (%s, %s, %s, %s, %s)", (a["id_cliente"], a["nombre"], a["apellido"], a["telefono"], a["direccion"],))
        self.connection_db_ventas.commit()
        cur.close()

    def on_data_visitas(self, client, userdata, message):  
        a = json.loads(message.payload)

        if a["no_cuenta"] == 1:
            cur = self.connection_db_ventas.cursor()
            cur.execute("INSERT INTO visita(no_visita, no_cuenta, id_cliente, id_sucursal, fecha_hora) VALUES (%s, (SELECT no_cuenta FROM cuenta_programa_fidelidad WHERE id_cliente = %s), %s, %s, %s)", (a["no_visita"], a["id_cliente"], a["id_cliente"], a["sucursal"], a["hora"],))
            self.connection_db_ventas.commit()
            cur.close()
        else:
            cur = self.connection_db_ventas.cursor()
            cur.execute("INSERT INTO visita(no_visita, no_cuenta, id_cliente, id_sucursal, fecha_hora) VALUES (%s, (SELECT no_cuenta FROM cuenta_programa_fidelidad WHERE id_cliente = %s), %s, %s, %s)", (a["no_visita"], a["id_cliente"], a["id_cliente"], a["sucursal"], a["hora"],))
            self.connection_db_ventas.commit()
            cur.close()

    def on_data_llenar(self, client, userdata, message):  
        a = json.loads(message.payload)

        cur = self.connection_db_inventario.cursor()
        cur.execute("SELECT llenar_estante(%s, %s)", (a["id_estante"], a["hora"],))
        self.connection_db_inventario.commit()
        cur.close()

    def on_data_charcuteria(self, client, userdata, message):  
        a = json.loads(message.payload)

        if a["accion"] == "borrar":
            cur = self.connection_db_ventas.cursor()
            cur.execute("DELETE FROM cliente_charcuteria WHERE id_cliente = %s", (a["id_cliente"],))
            self.connection_db_ventas.commit()
            cur.close()
        if a["accion"] == "update":
            cur = self.connection_db_ventas.cursor()
            cur.execute("UPDATE cliente_charcuteria SET no_fila = cliente_charcuteria.no_fila+1 WHERE id_sucursal = %s", (a["id_cliente"],))
            self.connection_db_ventas.commit()
            cur.close()
        if a["accion"] == "insertar":
            cur = self.connection_db_ventas.cursor()
            cur.execute("INSERT INTO cliente_charcuteria(id_cliente, no_fila, id_sucursal) VALUES (%s, %s, %s)", (a["id_cliente"], a["no_fila"], a["id_sucursal"],))
            self.connection_db_ventas.commit()
            cur.close()

    def conectar_suscriptor(self):
        host = "broker.hivemq.com"
        self.client.on_connect = self.on_connect
        self.client.message_callback_add('sucursal1/estantes/#', self.on_data_estante)
        self.client.message_callback_add('sucursal2/estantes/#', self.on_data_estante)
        self.client.message_callback_add('sucursal1/sensores', self.on_data_sensor)
        self.client.message_callback_add('sucursal2/sensores', self.on_data_sensor)
        self.client.message_callback_add('sucursal1/facturas', self.on_data_facturas)
        self.client.message_callback_add('sucursal2/facturas', self.on_data_facturas)
        self.client.message_callback_add('sucursal1/detalles', self.on_data_detalles)
        self.client.message_callback_add('sucursal2/detalles', self.on_data_detalles)
        self.client.message_callback_add('sucursal1/clientes', self.on_data_clientes)
        self.client.message_callback_add('sucursal2/clientes', self.on_data_clientes)
        self.client.message_callback_add('sucursal1/visitas', self.on_data_visitas)
        self.client.message_callback_add('sucursal2/visitas', self.on_data_visitas)
        self.client.message_callback_add('sucursal1/llenar', self.on_data_llenar)
        self.client.message_callback_add('sucursal2/llenar', self.on_data_llenar)
        self.client.message_callback_add('sucursal1/charcuteria', self.on_data_charcuteria)
        self.client.message_callback_add('sucursal2/charcuteria', self.on_data_charcuteria)
        self.client.connect(host=host) 
        self.client.loop_forever()

    def guardar_datos(self, a):
        #se guardan los datos en la base de datos 
        cur = self.connection_db_inventario.cursor()
        cur.execute("SELECT update_estante(%s, %s, %s)", (a["id_producto"], a["cantidad"], a["hora"]))
        self.connection_db_inventario.commit()
        cur.close()
        print('datos guardados')
        
    def enviar_alarma_estante(self, a):
        #guardar alarma en la bd
        self.no_alarma += 1
        cur = self.connection_db_inventario.cursor()
        cur.execute("INSERT INTO activacion_alarma(no_alarma, id_estante, fecha_hora, activada) VALUES (%s, %s, %s, %s)", (self.no_alarma, a["id_estante"], a["hora"], True))
        self.connection_db_inventario.commit()
        cur.close()
        payload = {
                "activar": 'true',
                "id_estante": a["id_estante"]
        }
        print(payload)
        self.client.qos = 1
        self.client.publish(a["sucursal"]+'/alarmas/'+str(a["id_estante"]),json.dumps(payload),qos=1)
        
    def enviar_alarma_sensor(self, sucursal, id_cliente):
        payload = {
                "activar": 'true',
                "id_cliente": id_cliente
        }
        print(payload)
        self.client.qos = 1
        self.client.publish(sucursal+'alarmas/sensores',json.dumps(payload),qos=1)


