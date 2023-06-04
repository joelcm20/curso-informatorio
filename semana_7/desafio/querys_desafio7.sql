--
-- Agregar el comando necesario que introduzca en la tabla usu es_colaborador=false, rio, 1 usuario con  nombreE)-- de admin, 4 con rol de colaborador y 5 con rol de público.
--
INSERT INTO usuario
(
nombre,
apellido,
telefono,
username,
email,
contrasenia,
es_publico,
es_colaborador,
es_admin)
VALUES
("lionel", "messi", "123456789", "lionelmessi", "lionel@messi", "lionelmessi", false, false, true),
("joel", "chavez","123456789", "joelchavez", "joel@chavez", "joelchavez", false, true, false),
("cristiano", "ronaldo", "123456789", "cristianoronaldo", "cristiano@ronaldo", "cristianoronaldo", false, true, false),
("neymar", "jr", "123456789", "neymarjr", "neymar@jr", "neymarjr", false, true, false),
("kylian", "mbappe", "123456789", "kylianmbappe", "kylian@mbappe", "kylianmbappe", false, true, false),
("paulo", "dybala", "123456789", "pauldybala", "paulo@dybala", "pauldybala", true, false, false),
("angel", "di maria", "123456789", "angoldimaria", "angel@di maria", "angoldimaria", true, false, false),
("jordi", "alba", "123456789", "jordialba", "jordi@alba", "jordialba", true, false, false),
("rodrigo", "de paul", "123456789", "rodpaul", "rodrigo@de_paul", "rodpaul", true, false, false),
("diego", "mradona", "123456789", "dgmradona", "diego@mradona", "dgmradona", true, false, false),
("lukita", "modric", "123456789", "lukimodric", "lukita@modric", "lukimodric", true, false, false);

--
-- Agregar el comando necesario para actualizar el rol a admin de uno de los usuarios agregado con rol de colaborador.
--
UPDATE usuario SET es_colaborador=false, es_admin=true WHERE es_colaborador=true LIMIT 1;

--
-- Agregar el comando necesario que introduzca en la tabla articulo, 3 artículos con estado TRUE y uno con estado FALSE.
--
INSERT INTO articulo
(
id_usuario,
titulo,
resumen,
contenido,
estado
)
VALUES
(3, "articulo 1", "resumen 1", "contenido 1", true),
(4, "articulo 2", "resumen 2", "contenido 2", true),
(5, "articulo 3", "resumen 3", "contenido 3", true),
(1, "articulo 4", "resumen 4", "contenido 4", false);

--
-- Agregar el comando necesario para eliminar el artículo que tenga estado FALSE.
--
DELETE FROM articulo WHERE estado=false;

--
-- Agregar el comando necesario que introduzca 3 comentarios al primer artículo agregado y 2 comentarios al segundo artículo.
--
INSERT INTO comentario
(
id_articulo,
id_usuario,
contenido
)
VALUES
(1, 1, "comentario 1"),
(2, 2, "comentario 2"),
(2, 3, "comentario 2");

-- 
-- Agregar el comando necesario para listar todos los artículos que tengan comentarios, mostrando el título del artículo, la fecha_publicacion del artículo, el nombre del usuario que realizo el comentario y la fecha_hora que realizó dicho comentario, agrupados por artículos.
--
SELECT articulo.titulo, articulo.fecha_publicacion, usuario.nombre, comentario.fecha_hora
FROM articulo
INNER JOIN usuario ON articulo.id_usuario=usuario.id
INNER JOIN comentario ON articulo.id=comentario.id_articulo;