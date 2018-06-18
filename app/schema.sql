drop table if exists users;
drop table if exists cargos;

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

create table usuarios (
  id integer primary key autoincrement,
  nome VARCHAR(45),
  funcao_id integer,
  empresa_id integer,
  grupo_sigla VARCHAR(10),
  cartorio_id integer not null,
  FOREIGN KEY(funcao_id) REFERENCES funcao(id),
  FOREIGN KEY(empresa_id) REFERENCES empresa(id),
  FOREIGN KEY(grupo_sigla) REFERENCES grupo(sigla),
  FOREIGN KEY(cartorio_id) REFERENCES cartorio(id)
);

create table empresas (
  id integer primary key autoincrement,
  nome VARCHAR(45),
  localizacao VARCHAR(45),
  setor VARCHAR(45)
);

create table funcoes (
  id integer primary key autoincrement,
  nome VARCHAR(45),
  descricao VARCHAR(45),
  setor VARCHAR(45)
);

create table grupos (
  sigla VARCHAR(10) primary key,
  nome VARCHAR(45),
  descricao VARCHAR(45),
  chefe VARCHAR(45)
);


--Criando tabela para testar a entidade voto - esta imcompleta

create table if not exists urnas (
  id integer primary key autoincrement,
  local VARCHAR(45)
);

/*
create table fabricantes (

);

create table engenheiros (

);

create table responsavel (

);

create table cartorios (

);

create table estado (

);

create table cargos_estado (

);

create table logs (

);

create table usuario_logs(

);
*/
