CREATE TABLE cursos (
  codigo int NOT NULL,
  nombre varchar(50) NOT NULL,
  creditos int NOT NULL
) 

INSERT INTO cursos (codigo, nombre, creditos) VALUES
(1, 'Tendencias de software', 5),
(2, 'Ingles V', 0),
(3, 'Matematicas operativas', 2);

ALTER TABLE cursos
  ADD PRIMARY KEY (codigo);