CREATE TABLE IF NOT EXISTS sucursal(
    id_sucursal serial, 
    ubicacion varchar(20) not null, 
    cant_pasillos integer, 
    capacidad integer, 
    primary key (id_sucursal)
);

CREATE TABLE IF NOT EXISTS estante_inteligente(
    id_estante serial, 
    id_sucursal serial, 
    capacidad integer, 
    no_pasillo integer, 
    primary key (id_estante), 
    foreign key (id_sucursal) references sucursal
);

CREATE TABLE IF NOT EXISTS activacion_alarma(
    no_alarma serial, 
    id_estante serial, 
    fecha_hora timestamp default current_timestamp, 
    activada Boolean default False, 
    primary key (no_alarma), 
    foreign key (id_estante) references estante_inteligente
);

CREATE TABLE IF NOT EXISTS producto(
    id_producto serial,  
    nombre varchar(20) not null, 
    categoria varchar(20) not null,  
    primary key (id_producto)
);

CREATE TABLE IF NOT EXISTS inventario(
    id_producto integer, 
    fecha_hora timestamp default current_timestamp,  
    cantidad_inicial integer, 
    cantidad_restante integer,
    primary key (id_producto, fecha_hora), 
    foreign key (id_producto) references producto
);

CREATE TABLE IF NOT EXISTS producto_asignado(
    id_producto integer, 
    fecha_hora timestamp default current_timestamp,  
    id_estante integer,
    cantidad_inicial integer, 
    cantidad_restante integer,
    primary key (id_producto, fecha_hora), 
    foreign key (id_producto) references producto,
    foreign key (id_estante) references estante_inteligente
);

CREATE TABLE IF NOT EXISTS cambio_precio(
    fecha_hora timestamp default current_timestamp,
    id_producto integer, 
    precio numeric(8,0), 
    primary key (fecha_hora, id_producto), 
    foreign key (id_producto) references producto 
);

