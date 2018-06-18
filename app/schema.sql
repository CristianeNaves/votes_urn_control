drop table if exists users;
drop table if exists cargos;
drop table if exists engenheiros;
drop table if exists fabricantes;

create table users (
  id integer primary key autoincrement,
  name text not null,
  phone text not null,
  email text not null,
  password text not null
);

create table if not exists votos (
  id integer primary key autoincrement,
  horario timestamp not null,
  regiao text,
  urna_id integer not null,
  candidato_id integer not null,
  FOREIGN KEY(urna_id) REFERENCES urnas(id),
  FOREIGN KEY(candidato_id) REFERENCES candidatos(id)
);

create table if not exists candidatos (
  id integer primary key autoincrement,
  nome VARCHAR(100) not null,
  foto blob,
  vice_id integer,
  cargo_id integer not null,
  partido_id integer not null,
  FOREIGN KEY(vice_id) REFERENCES candidatos(id),
  FOREIGN KEY(cargo_id) REFERENCES cargos(id),
  FOREIGN KEY(partido_id) REFERENCES partidos(id)
);

create table cargos (
  id integer primary key autoincrement,
  nome VARCHAR(25) not null,
  descricao text,
  poder text,
  local_trabalho text
);

create table if not exists partidos (
  id integer primary key autoincrement,
  lider VARCHAR(50),
  data_fundacao date,
  nome VARCHAR(25) not null
);

create table engenheiros (
  cpf integer primary key,
  crea VARCHAR(45),
  nome VARCHAR(45) not null,
  formacao VARCHAR(45)
);

create table fabricantes (
  id integer primary key autoincrement,
  local VARCHAR(45),
  data_fabricacao DATETIME,
  empresa VARCHAR(45),
  engenheiro_cpf integer not null,
  FOREIGN KEY(engenheiro_cpf) REFERENCES engenheiros(cpf)
);


--Criando tabela para testar a entidade voto - esta imcompleta

create table if not exists urnas (
  id integer primary key autoincrement,
  local VARCHAR(45),
  fabricante_id integer not null,
  FOREIGN KEY(fabricante_id) REFERENCES fabricantes(id)
);

/*

create table responsavel (

);

create table cartorios (

);

create table estado (

);

create table cargos_estado (

);

create table usuarios (

);

create table logs (

);

create table usuario_logs(

);

create table empresa (

);

create table funcao (

);

create table grupo (

);
*/
