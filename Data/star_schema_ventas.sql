CREATE TABLE IF NOT EXISTS sucursal(
    id_sucursal integer, 
    ubicacion varchar(20) not null, 
    primary key (id_sucursal)
);

CREATE TABLE IF NOT EXISTS producto(
    id_producto integer,  
    nombre varchar(20) not null, 
    categoria varchar(20) not null,  
    precio integer,
    primary key (id_producto)
);

CREATE TABLE IF NOT EXISTS cliente(
    id_cliente integer, 
    nombre varchar(20) not null, 
    apellido varchar(20) not null, 
    telefono varchar(20), 
    direccion varchar(40) not null, 
    primary key (id_cliente)
);

CREATE TABLE IF NOT EXISTS tiempo(
    id_tiempo serial, 
    dia integer, 
    semana integer, 
    mes integer, 
    primary key (id_tiempo)
);

CREATE TABLE IF NOT EXISTS ventas(
    id_cliente integer,
    id_sucursal integer,
    id_producto integer,
    id_tiempo integer,
    cantidad_vendida integer,
    total numeric(8,0),
    primary key (id_cliente, id_sucursal, id_producto, id_tiempo),
    foreign key (id_cliente) references cliente,
    foreign key (id_sucursal) references sucursal,
    foreign key (id_producto) references producto,
    foreign key (id_tiempo) references tiempo
);

