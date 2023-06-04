--
-- item 1: Modificar la base de datos para registrar que `Luis Torres' se mudó a `Málaga'.
-- 
UPDATE empleado SET ciudad = 'Málaga' WHERE nombre_empleado = 'Luis Torres';

--
-- item 2: Dar a todos los empleados de la empresa `Oracle' un 10 % de aumento.
-- 
UPDATE trabaja SET sueldo = sueldo * 1.1 WHERE nombre_empresa = 'Oracle';

--
-- item 3: Dar a todos los supervisores de la empresa `Netflix' un 10 % de aumento.
-- 
-- select * from supervisa where nombre_supervisor in (select nombre_empleado from supervisa where supervisa.nombre_empleado in (select nombre_empresa from trabaja where nombre_empresa="Netflix"))
UPDATE trabaja SET sueldo = sueldo * 1.1 WHERE empresa = 'Microsoft';