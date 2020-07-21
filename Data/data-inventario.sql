INSERT INTO sucursal (id_sucursal, ubicacion, cant_pasillos, capacidad) VALUES (1, 'Terrazas del Ávila', 8, 10);
INSERT INTO sucursal (id_sucursal, ubicacion, cant_pasillos, capacidad) VALUES (2, 'Los Palos Grandes', 8, 10);

INSERT INTO estante_inteligente(id_estante, id_sucursal, capacidad, no_pasillo) VALUES (1, 1, 100, 1);
INSERT INTO estante_inteligente(id_estante, id_sucursal, capacidad, no_pasillo) VALUES (2, 1, 100, 2); 
INSERT INTO estante_inteligente(id_estante, id_sucursal, capacidad, no_pasillo) VALUES (3, 1, 100, 2);
INSERT INTO estante_inteligente(id_estante, id_sucursal, capacidad, no_pasillo) VALUES (4, 1, 100, 3);
INSERT INTO estante_inteligente(id_estante, id_sucursal, capacidad, no_pasillo) VALUES (5, 1, 100, 3);
INSERT INTO estante_inteligente(id_estante, id_sucursal, capacidad, no_pasillo) VALUES (6, 1, 100, 4);
INSERT INTO estante_inteligente(id_estante, id_sucursal, capacidad, no_pasillo) VALUES (7, 1, 100, 4);
INSERT INTO estante_inteligente(id_estante, id_sucursal, capacidad, no_pasillo) VALUES (8, 1, 100, 5);
INSERT INTO estante_inteligente(id_estante, id_sucursal, capacidad, no_pasillo) VALUES (9, 2, 100, 1);
INSERT INTO estante_inteligente(id_estante, id_sucursal, capacidad, no_pasillo) VALUES (10, 2, 100, 2);
INSERT INTO estante_inteligente(id_estante, id_sucursal, capacidad, no_pasillo) VALUES (11, 2, 100, 2);
INSERT INTO estante_inteligente(id_estante, id_sucursal, capacidad, no_pasillo) VALUES (12, 2, 100, 3);
INSERT INTO estante_inteligente(id_estante, id_sucursal, capacidad, no_pasillo) VALUES (13, 2, 100, 3);
INSERT INTO estante_inteligente(id_estante, id_sucursal, capacidad, no_pasillo) VALUES (14, 2, 100, 4);
INSERT INTO estante_inteligente(id_estante, id_sucursal, capacidad, no_pasillo) VALUES (15, 2, 100, 4);
INSERT INTO estante_inteligente(id_estante, id_sucursal, capacidad, no_pasillo) VALUES (16, 2, 100, 5);

INSERT INTO producto(id_producto, nombre, categoria) VALUES (1, 'Leche', 'Lácteos');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (2, 'Yogurt', 'Lácteos');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (3, 'Mantequilla', 'Lácteos');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (4, 'Queso Amarillo', 'Charcutería');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (5, 'Queso Blanco', 'Charcutería');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (6, 'Queso Duro', 'Charcutería');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (7, 'Crema de Leche', 'Lácteos');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (8, 'Pan de Trigo', 'Panadería');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (9, 'Pan Integral', 'Panadería');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (10, 'Jugo de Naranja', 'Bebidas');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (11, 'Jugo de Manzana', 'Bebidas');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (12, 'Jugo de Mango', 'Bebidas');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (13, 'Coca-cola', 'Bebidas');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (14, 'Cerveza', 'Bebidas');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (15, 'Golden Naranja', 'Bebidas');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (16, 'Lucky Charms', 'Cereales');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (17, 'Froot Loops', 'Cereales');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (18, 'Zucaritas', 'Cereales');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (19, 'Chorizo', 'Charcutería');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (20, 'Salchicha', 'Charcutería');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (21, 'Jamón', 'Charcutería');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (22, 'Salami', 'Charcutería');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (23, 'Oreo', 'Galletas');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (24, 'Galletas de Avena', 'Galletas');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (25, 'Atún', 'Enlatados');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (26, 'Maíz', 'Enlatados');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (27, 'Salsa de Tomate', 'Enlatados');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (28, 'Sopa', 'Enlatados');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (29, 'Azúcar', 'No Perecederos');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (30, 'Sal', 'No Perecederos');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (31, 'Café', 'No Perecederos');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (32, 'Harina', 'No Perecederos');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (33, 'Pasta', 'No Perecederos');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (34, 'Arroz', 'No Perecederos');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (35, 'Leche en Polvo', 'No Perecederos');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (36, 'Zanahoria', 'Vegetales');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (37, 'Tomate', 'Vegetales');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (38, 'Lechuga', 'Vegetales');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (39, 'Pimentón', 'Vegetales');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (40, 'Fresas', 'Frutas');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (41, 'Patilla', 'Frutas');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (42, 'Piña', 'Frutas');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (43, 'Durazno', 'Frutas');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (44, 'Limón', 'Frutas');
INSERT INTO producto(id_producto, nombre, categoria) VALUES (45, 'Huevos', 'Frescos');

INSERT INTO cambio_precio(id_producto,precio) VALUES (1,49);
INSERT INTO cambio_precio(id_producto,precio) VALUES (2,32);
INSERT INTO cambio_precio(id_producto,precio) VALUES (3,41);
INSERT INTO cambio_precio(id_producto,precio) VALUES (4,22);
INSERT INTO cambio_precio(id_producto,precio) VALUES (5,27);
INSERT INTO cambio_precio(id_producto,precio) VALUES (6,6);
INSERT INTO cambio_precio(id_producto,precio) VALUES (7,19);
INSERT INTO cambio_precio(id_producto,precio) VALUES (8,15);
INSERT INTO cambio_precio(id_producto,precio) VALUES (9,5);
INSERT INTO cambio_precio(id_producto,precio) VALUES (10,14);
INSERT INTO cambio_precio(id_producto,precio) VALUES (11,20);
INSERT INTO cambio_precio(id_producto,precio) VALUES (12,1);
INSERT INTO cambio_precio(id_producto,precio) VALUES (13,15);
INSERT INTO cambio_precio(id_producto,precio) VALUES (14,14);
INSERT INTO cambio_precio(id_producto,precio) VALUES (15,26);
INSERT INTO cambio_precio(id_producto,precio) VALUES (16,2);
INSERT INTO cambio_precio(id_producto,precio) VALUES (17,26);
INSERT INTO cambio_precio(id_producto,precio) VALUES (18,12);
INSERT INTO cambio_precio(id_producto,precio) VALUES (19,31);
INSERT INTO cambio_precio(id_producto,precio) VALUES (20,4);
INSERT INTO cambio_precio(id_producto,precio) VALUES (21,5);
INSERT INTO cambio_precio(id_producto,precio) VALUES (22,40);
INSERT INTO cambio_precio(id_producto,precio) VALUES (23,42);
INSERT INTO cambio_precio(id_producto,precio) VALUES (24,37);
INSERT INTO cambio_precio(id_producto,precio) VALUES (25,24);
INSERT INTO cambio_precio(id_producto,precio) VALUES (26,28);
INSERT INTO cambio_precio(id_producto,precio) VALUES (27,23);
INSERT INTO cambio_precio(id_producto,precio) VALUES (28,43);
INSERT INTO cambio_precio(id_producto,precio) VALUES (29,13);
INSERT INTO cambio_precio(id_producto,precio) VALUES (30,28);
INSERT INTO cambio_precio(id_producto,precio) VALUES (31,2);
INSERT INTO cambio_precio(id_producto,precio) VALUES (32,9);
INSERT INTO cambio_precio(id_producto,precio) VALUES (33,41);
INSERT INTO cambio_precio(id_producto,precio) VALUES (34,24);
INSERT INTO cambio_precio(id_producto,precio) VALUES (35,4);
INSERT INTO cambio_precio(id_producto,precio) VALUES (36,23);
INSERT INTO cambio_precio(id_producto,precio) VALUES (37,22);
INSERT INTO cambio_precio(id_producto,precio) VALUES (38,5);
INSERT INTO cambio_precio(id_producto,precio) VALUES (39,35);
INSERT INTO cambio_precio(id_producto,precio) VALUES (40,44);
INSERT INTO cambio_precio(id_producto,precio) VALUES (41,25);
INSERT INTO cambio_precio(id_producto,precio) VALUES (42,41);
INSERT INTO cambio_precio(id_producto,precio) VALUES (43,35);
INSERT INTO cambio_precio(id_producto,precio) VALUES (44,13);
INSERT INTO cambio_precio(id_producto,precio) VALUES (45,28);

insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (1, 240, 230);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (2, 99, 69);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (3, 368, 348);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (4, 169, 159);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (5, 205, 185);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (6, 407, 377);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (7, 273, 263);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (8, 81, 61);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (9, 436, 406);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (10, 252, 242);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (11, 396, 376);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (12, 314, 284);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (13, 128, 118);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (14, 241, 221);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (15, 278, 248);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (16, 490, 480);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (17, 93, 73);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (18, 95, 65);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (19, 169, 159);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (20, 175, 155);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (21, 158, 125);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (22, 247, 237);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (23, 272, 252);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (24, 499, 469);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (25, 144, 114);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (26, 303, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (27, 296, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (28, 399, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (29, 126, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (30, 156, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (31, 205, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (32, 329, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (33, 123, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (34, 458, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (35, 322, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (36, 399, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (37, 172, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (38, 282, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (39, 302, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (40, 314, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (41, 336, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (42, 465, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (43, 479, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (44, 560, 0);
insert into inventario (id_producto, cantidad_inicial, cantidad_restante) values (45, 371, 0);

insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (1, 1, 10, 10);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (2, 1, 30, 30);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (3, 1, 20, 20);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (4, 2, 10, 10);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (5, 2, 20, 20);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (6, 2, 30, 30);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (7, 3, 10, 10);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (8, 3, 20, 20);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (9, 3, 30, 30);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (10, 4, 10, 10);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (11, 4, 20, 20);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (12, 4, 30, 30);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (13, 5, 10, 10);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (14, 5, 20, 20);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (15, 5, 30, 30);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (16, 6, 10, 10);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (17, 6, 20, 20);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (18, 6, 30, 30);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (27, 7, 10, 10);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (28, 7, 20, 20);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (29, 7, 30, 30);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (22, 8, 10, 10);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (23, 8, 20, 20);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (24, 9, 30, 30);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (25, 9, 30, 30);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (26, 9, 20, 20);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (19, 10, 70, 70);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (20, 10, 30, 30);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (21, 10, 20, 20);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (30, 11, 30, 30);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (31, 11, 70, 70);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (32, 11, 20, 20);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (33, 12, 90, 90);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (34, 12, 180, 180);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (35, 12, 120, 120);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (36, 13, 90, 90);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (37, 13, 120, 120);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (38, 13, 180, 180);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (39, 14, 180, 180);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (40, 14, 120, 120);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (41, 14, 90, 90);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (42, 15, 180, 180);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (43, 15, 120, 120);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (44, 16, 150, 150);
insert into producto_asignado (id_producto, id_estante, cantidad_inicial, cantidad_restante) VALUES (45, 16, 150, 150);




















