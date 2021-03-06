########## TABLES
# similars_src
# similars_dest_tmp
# similars_dest
# idx_src
# idx_dest
# songs
# billboard
# top2009
# foo
# top100
# dupes
# uniq_songs
# top100_similars
# top100_similars_mapped

# CLeanup special characters
SELECT YOUR_COLUMN FROM YOUR_TABLE WHERE replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace( lower(YOUR_COLUMN), 'á','a'), 'ã','a'), 'â','a'), 'é','e'), 'ê','e'), 'í','i'),'ó','o') ,'õ','o') ,'ô','o'),'ú','u'), 'ç','c') LIKE 'SEARCH_KEY%'

# top100_similars all top 100 songs with similarity data
create table top100_similars as select distinct track_id, target from top100 t join uniq_songs s on t.year - s.year between -1 and 1 and t.title = s.title join similars_src si on si.tid = s.track_id;

# Similarity Mappings
select distinct si.tid, si.target from top100_similars_mapped si join songs s on si.target = s.track_id join top100 t on s.title = t.title and s.year - t.year between -1 and 1  join songs s2 on si.target = s2.target join top100 t2 on s2.title = t2.title and s2.year - t2.year between -1 and 1

# Clean unicode artifacts
SELECT YOUR_COLUMN FROM YOUR_TABLE WHERE replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace( lower(YOUR_COLUMN), 'á','a'), 'ã','a'), 'â','a'), 'é','e'), 'ê','e'), 'í','i'), 'ó','o') ,'õ','o') ,'ô','o'),'ú','u'), 'ç','c') LIKE 'SEARCH_KEY%'
