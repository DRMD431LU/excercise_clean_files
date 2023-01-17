import os
import tempfile

from read_clean_files import read_lines_and_create_set
from read_clean_files import remove_lines


def test_create_id_set():
    with tempfile.NamedTemporaryFile(mode='w') as tmp:
        tmp.write("""56803157598|1
                     56803157599|2
                     56803157600|56803157599
                     56803157602|4
                     56803157605|5"""
                 )
        tmp.seek(0)
        id_set = read_lines_and_create_set(tmp.name)
        assert id_set == {
                '56803157598', '56803157599',
                '56803157600', '56803157602',
                '56803157605'
                }


def test_remove_lines():
    
    with (tempfile.NamedTemporaryFile(mode="w") as file1,
          tempfile.NamedTemporaryFile(mode="w") as file2,
          tempfile.NamedTemporaryFile(mode="r+") as output):
        
        file1.write("""56803157598|1
                       56803157599|2
                       56803157600|56803157599
                       56803157602|4
                       56803157605|5"""
                   )

        file2.write("""56803157598|10386185969
                       56803157599|10386186061
                       56803157605|10386185978"""
                       )
        file1.seek(0)
        file2.seek(0)
        remove_lines(file1.name, file2.name, output.name)
        output.seek(0)
        out = output.readlines()
        new_out = []
        for line in out:
            new_out.append(line.strip())
        assert isinstance(out, list)
        assert new_out == ["56803157600|56803157599","56803157602|4"]
