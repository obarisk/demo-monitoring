CREATE TABLE factories (
   id   BIGSERIAL UNIQUE NOT NULL
  ,name VARCHAR(20) NOT NULL
);

CREATE TABLE sensors (
   id   BIGSERIAL UNIQUE NOT NULL
  ,name VARCHAR(20)      NOT NULL
  ,factory_id INT        NOT NULL
  ,location VARCHAR(20)
  ,FOREIGN KEY (factory_id) REFERENCES factories(id)
);

CREATE TABLE labels (
   id SMALLINT UNIQUE NOT NULL
  ,name VARCHAR(20)   NOT NULL
);

CREATE TABLE records (
   t TIMESTAMP      WITHOUT TIME ZONE NOT NULL
  ,s BIGINT         NOT NULL
  ,l SMALLINT       NOT NULL
  ,v NUMERIC(18, 4) NOT NULL
);

CREATE INDEX records_t ON records USING BRIN(t)
;

CREATE INDEX records_s ON records USING BTREE(s)
;

CREATE INDEX records_l ON records USING BTREE(l)
;

INSERT INTO labels (id, name)
VALUES 
(1, 'temperature'),
(2, 'humidity'),
(3, 'electricity')
;