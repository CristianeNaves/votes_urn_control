drop table if exists users;
drop table if exists cargos;
drop table if exists empresas;
drop table if exists grupos;
drop table if exists funcoes;
drop table if exists usuarios;
drop table if exists engenheiros;
drop table if exists fabricantes;
drop table if exists cartorios;
drop table if exists estado;
drop table if exists logs;
drop table if exists responsaveis;

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

create table cartorios(
  id integer primary key autoincrement,
  nome VARCHAR(45),
  estado_id integer,
  FOREIGN KEY(estado_id) REFERENCES estado(id)
);  

create table estado(
  id integer primary key autoincrement,
  nome VARCHAR(50),
  sigla char(2),
  cargos_id integer,
  FOREIGN KEY(cargos_id) REFERENCES cargos(id)
);

create table if not exists usuario_logs(
  log_id integer,
  usuarios_id integer,
  FOREIGN KEY(log_id) REFERENCES logs(id),
  FOREIGN KEY(usuarios_id) REFERENCES usuarios(id)
);

create table if not exists logs(
  id integer primary key autoincrement,
  data_ DATETIME,
  tipo_requisicao VARCHAR(45),
  parametros VARCHAR(45),
  resultado VARCHAR(45)
);

create table responsaveis (
  cpf integer primary key,
  nome VARCHAR(45) not null,
  data_nasc DATETIME,
  cartorio_id integer not null,
  FOREIGN KEY(cartorio_id) REFERENCES cartorios(id)
);


/*

create table cargos_estado ();

*/
