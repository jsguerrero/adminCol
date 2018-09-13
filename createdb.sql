CREATE ROLE adminapps LOGIN PASSWORD '4sA$Ftb..';

CREATE DATABASE appcolonias OWNER adminapps;

GRANT CONNECT ON DATABASE appcolonias TO adminapps;
