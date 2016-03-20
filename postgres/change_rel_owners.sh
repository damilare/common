for tbl in `psql -qAt -c "select tablename from pg_tables where schemaname = 'public';" $0` ; do  psql -c "alter table $tbl owner to $1" $0 ; done


for tbl in `psql -qAt -c "select sequence_name from information_schema.sequences where sequence_schema = 'public';" $0` ; do  psql -c "alter table $tbl owner to $1" $0 ; done


for tbl in `psql -qAt -c "select table_name from information_schema.views where table_schema = 'public';" $0` ; do  psql -c "alter table $tbl owner to $1" $0 ; done
