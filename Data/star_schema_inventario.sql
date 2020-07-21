CREATE TABLE IF NOT EXISTS sucursal(
    id_sucursal integer, 
    ubicacion varchar(20) not null, 
    primary key (id_sucursal)
);

CREATE TABLE IF NOT EXISTS estante_inteligente(
    id_estante integer,  
    capacidad integer, 
    no_pasillo integer, 
    primary key (id_estante)
);

CREATE TABLE IF NOT EXISTS producto(
    id_producto integer,  
    nombre varchar(20) not null, 
    categoria varchar(20) not null,  
    precio integer,
    primary key (id_producto)
);

CREATE TABLE IF NOT EXISTS tiempo(
    id_tiempo serial, 
    dia integer, 
    semana integer, 
    mes integer, 
    primary key (id_tiempo)
);

CREATE TABLE IF NOT EXISTS inventario(
    id_producto integer,
    id_sucursal integer,
    id_tiempo integer,
    id_estante integer,
    cantidad_inicial integer,
    cantidad_restante numeric(8,0),
    primary key (id_producto, id_sucursal, id_tiempo, id_estante),
    foreign key (id_producto) references producto,
    foreign key (id_sucursal) references sucursal,
    foreign key (id_tiempo) references tiempo,
    foreign key (id_estante) references estante_inteligente
);

