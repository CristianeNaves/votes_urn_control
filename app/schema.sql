drop table if exists users;
drop table if exists;
create table users (
  id integer primary key autoincrement,
  name text not null,
  phone text not null,
  email text not null,
  password text not null
);
"""
create table votos (
  id_voto integer primary key autoincrement,
  horario,
  regiao,
  id_urna,
  id_candidato,
);
"""
