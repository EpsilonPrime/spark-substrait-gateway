# SPDX-License-Identifier: Apache-2.0
"""Simple test of the DuckDB ADBC Substrait interface."""
import adbc_driver_duckdb.dbapi
from google.protobuf import text_format
import pyarrow

from substrait.gen.proto import plan_pb2


PLAN_PROTOTEXT = """
relations {
  root {
    input {
      read {
        common {
          direct {
          }
        }
        base_schema {
          names: "mbid"
          names: "artist_mb"
          struct {
            types {
              string {
                nullability: NULLABILITY_REQUIRED
              }
            }
            types {
              string {
                nullability: NULLABILITY_NULLABLE
              }
            }
            nullability: NULLABILITY_REQUIRED
          }
        }
        local_files {
          items {
            uri_file: "somefile.parquet"
            parquet {
            }
          }
        }
      }
    }
  }
}
"""

def execute_with_duckdb_over_adbc(plan: 'plan_pb2.Plan') -> pyarrow.lib.Table:
    """Executes the given Substrait plan against DuckDB using ADBC."""
    with adbc_driver_duckdb.dbapi.connect() as conn, conn.cursor() as cur:
        plan_data = plan.SerializeToString()
        cur.adbc_statement.set_substrait_plan(plan_data)
        tbl = cur.fetch_arrow_table()
        return tbl


if __name__ == '__main__':
    plan = text_format.Parse(PLAN_PROTOTEXT, plan_pb2.Plan())
    table = execute_with_duckdb_over_adbc(plan)
    print(table)
