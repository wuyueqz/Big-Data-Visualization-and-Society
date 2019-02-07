lib_path = "C:\\Users\\lenovo\\Anaconda3\\pkgs\\pyarrow-0.12.0-py36h8c67754_2\\Lib\\site-packages"
###My local location for pyarrow library
import sys
sys.path.append(lib_path)
import pyarrow as pa

table = pa.Table.from_pandas(df)
with open('file.arrow', 'bw') as f:
   writer = pa.RecordBatchFileWriter(f, table.schema)
   writer.write(table)
   writer.close()
